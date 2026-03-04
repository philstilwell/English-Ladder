import os
import requests
import feedparser
from bs4 import BeautifulSoup
from google import genai
from datetime import datetime

# --- 1. Configuration & Secrets ---
STATIC_APP_KEY = os.environ.get("STATIC_APP_KEY")
STATIC_SITE_ID = os.environ.get("STATIC_SITE_ID")
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=GEMINI_API_KEY)

# --- 2. Fetch Daily News ---
def get_daily_news():
    feed_url = "http://feeds.bbci.co.uk/news/world/rss.xml"
    feed = feedparser.parse(feed_url)
    if not feed.entries:
        return "No news found today."
    top_entry = feed.entries[0]
    return f"Title: {top_entry.title}\nSummary: {top_entry.description}"

# --- 3. Generate ESL Content ---
def generate_lesson_html(news_text):
    today_str = datetime.now().strftime("%B %d, %Y")
    
    prompt = f"""
    You are an advanced ESL curriculum writer. Based on the following news:
    {news_text}
    
    Write a 3-part advanced ESL lesson. 
    Format the output STRICTLY as raw HTML (no markdown blocks).
    Wrap the entire lesson in a single <article class="daily-lesson"> tag.
    
    Structure:
    <h2>📅 {today_str} - [Catchy Title]</h2>
    <h3>I. The News Brief</h3>
    <p>[Formal summary using advanced vocabulary]</p>
    <h3>II. Vocabulary & Grammar Focus</h3>
    <p>[Define 3-4 advanced terms and 1 advanced grammar concept]</p>
    <h3>III. Mastery Quiz</h3>
    <p>[3-5 MCQs with a hidden answer key]</p>
    """
    
    # Updated model string to the standard version
    response = client.models.generate_content(
        model="gemini-1.5-flash-002",
        contents=prompt
    )
    return response.text.strip()

# --- 4. Update the Static Site ---
def update_static_site(new_lesson_html):
    # CLEANED URL - No brackets or extra formatting
    api_url = f"https://api.static.app/v1/sites/{STATIC_SITE_ID}/files/index.html"
    headers = {
        "Authorization": f"Bearer {STATIC_APP_KEY}",
        "Content-Type": "text/html"
    }

    print(f"Connecting to: {api_url}")
    response = requests.get(api_url, headers={"Authorization": f"Bearer {STATIC_APP_KEY}"})
    
    if response.status_code != 200:
        print(f"Failed to fetch site. Status: {response.status_code}")
        return

    soup = BeautifulSoup(response.text, "html.parser")
    container = soup.find(id="lesson-container")
    
    if not container:
        print("Error: Could not find <div id='lesson-container'> in your index.html")
        return

    new_lesson_soup = BeautifulSoup(new_lesson_html, "html.parser")
    container.insert(0, new_lesson_soup)

    lessons = container.find_all("article", class_="daily-lesson")
    if len(lessons) > 7:
        for old_lesson in lessons[7:]:
            old_lesson.decompose()

    put_response = requests.put(api_url, headers=headers, data=str(soup))
    
    if put_response.status_code == 200:
        print("Successfully updated Static.app!")
    else:
        print(f"Failed to push: {put_response.text}")

if __name__ == "__main__":
    print("Fetching news...")
    news = get_daily_news()
    print("Generating ESL lesson...")
    lesson = generate_lesson_html(news)
    print("Updating Static.app...")
    update_static_site(lesson)