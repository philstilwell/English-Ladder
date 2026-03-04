import os
import requests
import feedparser
from bs4 import BeautifulSoup
import google.generativeai as genai
from datetime import datetime

# --- 1. Configuration & Secrets ---
STATIC_APP_KEY = os.environ.get("STATIC_APP_KEY")
STATIC_SITE_ID = os.environ.get("STATIC_SITE_ID")
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")

genai.configure(api_key=GEMINI_API_KEY)

# --- 2. Fetch Daily News (Using an RSS Feed) ---
def get_daily_news():
    # Using a standard world news RSS feed
    feed_url = "http://feeds.bbci.co.uk/news/world/rss.xml"
    feed = feedparser.parse(feed_url)
    
    # Grab the top story
    top_entry = feed.entries[0]
    return f"Title: {top_entry.title}\nSummary: {top_entry.description}"

# --- 3. Generate ESL Content with Gemini ---
def generate_lesson_html(news_text):
    model = genai.GenerativeModel('gemini-2.5-flash') # Or gemini-2.5-pro
    
    today_str = datetime.now().strftime("%B %d, %Y")
    
    prompt = f"""
    You are an advanced ESL curriculum writer. Based on the following news:
    {news_text}
    
    Write a 3-part advanced ESL lesson. 
    Format the output STRICTLY as raw HTML (no markdown blocks like ```html).
    Wrap the entire lesson in a single <article class="daily-lesson"> tag.
    
    Structure:
    <h2>📅 {today_str} - [Catchy Title]</h2>
    <h3>I. The News Brief</h3>
    <p>[Formal summary of the event using advanced vocabulary]</p>
    <h3>II. Vocabulary & Grammar Focus</h3>
    <p>[Define 3-4 advanced terms and 1 advanced grammar concept used in the brief]</p>
    <h3>III. Comprehension & Mastery Quiz</h3>
    <p>[3-5 multiple choice questions with a hidden/revealable answer key at the bottom]</p>
    """
    
    response = model.generate_content(prompt)
    return response.text.strip()

# --- 4. Update the Static Site HTML ---
def update_static_site(new_lesson_html):
    api_url = f"[https://api.static.app/v1/sites/](https://api.static.app/v1/sites/){STATIC_SITE_ID}/files/index.html"
    headers = {
        "Authorization": f"Bearer {STATIC_APP_KEY}",
        "Content-Type": "text/html"
    }

    # A. Get the current index.html
    response = requests.get(api_url, headers={"Authorization": f"Bearer {STATIC_APP_KEY}"})
    if response.status_code != 200:
        print("Failed to fetch current site HTML")
        return

    current_html = response.text
    soup = BeautifulSoup(current_html, "html.parser")

    # B. Find the container holding the lessons (Assuming a <div id="lesson-container">)
    container = soup.find(id="lesson-container")
    
    if not container:
        print("Could not find lesson container in HTML. Make sure your index.html has a <div id='lesson-container'>")
        return

    # C. Insert the new lesson at the top
    new_lesson_soup = BeautifulSoup(new_lesson_html, "html.parser")
    container.insert(0, new_lesson_soup)

    # D. Enforce the 7-day rolling window
    lessons = container.find_all("article", class_="daily-lesson")
    if len(lessons) > 7:
        for old_lesson in lessons[7:]:
            old_lesson.decompose() # Removes the HTML element

    # E. Push the updated HTML back to Static.app
    updated_html = str(soup)
    put_response = requests.put(api_url, headers=headers, data=updated_html)
    
    if put_response.status_code == 200:
        print("Successfully updated Static.app!")
    else:
        print(f"Failed to push update: {put_response.text}")

# --- 5. Main Execution ---
if __name__ == "__main__":
    print("Fetching news...")
    news_text = get_daily_news()
    
    print("Generating ESL lesson...")
    lesson_html = generate_lesson_html(news_text)
    
    print("Updating Static.app...")
    update_static_site(lesson_html)