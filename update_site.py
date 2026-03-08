import os
import feedparser
from bs4 import BeautifulSoup
import google.generativeai as genai
from datetime import datetime

# --- 1. Configuration & Secrets ---
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)

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
    Format the output STRICTLY as raw HTML (no markdown blocks like ```html).
    Wrap the entire lesson in a single <details class="daily-lesson"> tag.
    
    IMPORTANT REQUIREMENTS:
    1. The reading passage in Section I MUST be a minimum of 7 sentences long.
    2. Section III must be an interactive 7-item multiple-choice quiz. Use the exact inline JavaScript provided in the structure below so that when a student clicks an option, they receive immediate correct/incorrect feedback. Toggle the answer boxes light green (correct) or light red when clicked. Do NOT provide a separate answer key section.
    
    Structure:
    <summary class="lesson-date">📅 {today_str} - [Catchy Title]</summary>
    <div class="lesson-description">[1-sentence overview]</div>
    <div class="lesson-content">
        <div class="header"><h2>Advanced ESL: [Topic]</h2></div>
        <div class="section">
            <h2>I. The News Brief</h2>
            <p>[Write a formal summary using advanced vocabulary. MUST BE AT LEAST 7 SENTENCES LONG.]</p>
        </div>
        <div class="section">
            <h2>II. Vocabulary & Grammar Focus</h2>
            <div class="vocab-box">
                <span class="vocab-term">1. [Term] (part of speech):</span> [Definition]<br>
                <span class="vocab-term">2. [Term] (part of speech):</span> [Definition]<br>
                <span class="vocab-term">3. [Term] (part of speech):</span> [Definition]<br>
                <span class="vocab-term">4. [Term] (part of speech):</span> [Definition]
            </div>
            <p><strong>Advanced Grammar: [Concept]</strong><br>[Brief explanation and example from text]</p>
        </div>
        <div class="section">
            <h2>III. Comprehension & Mastery Quiz</h2>
            <p><em>Click on an option to check your answer.</em></p>
            <div class="quiz-card">
                <div class="quiz-question" style="margin-bottom: 25px;">
                    <p style="font-weight: bold; color: #8b4513; margin-bottom: 10px;">[Question Number]. [Question Text]</p>
                    <div style="display: flex; flex-direction: column; gap: 8px;">
                        <button style="text-align: left; padding: 10px; border: 1px solid #d2b48c; border-radius: 5px; background: #fff; cursor: pointer; font-size: 1em; transition: 0.2s;" onclick="this.parentElement.nextElementSibling.innerHTML='❌ <strong>Incorrect:</strong> [Explain why this option is wrong]'; this.parentElement.nextElementSibling.style.color='#b22222';">a) [Option A]</button>
                        <button style="text-align: left; padding: 10px; border: 1px solid #d2b48c; border-radius: 5px; background: #fff; cursor: pointer; font-size: 1em; transition: 0.2s;" onclick="this.parentElement.nextElementSibling.innerHTML='✅ <strong>Correct:</strong> [Explain why this option is right]'; this.parentElement.nextElementSibling.style.color='#2e8b57';">b) [Option B]</button>
                        <button style="text-align: left; padding: 10px; border: 1px solid #d2b48c; border-radius: 5px; background: #fff; cursor: pointer; font-size: 1em; transition: 0.2s;" onclick="this.parentElement.nextElementSibling.innerHTML='❌ <strong>Incorrect:</strong> [Explain why this option is wrong]'; this.parentElement.nextElementSibling.style.color='#b22222';">c) [Option C]</button>
                    </div>
                    <div class="feedback" style="margin-top: 12px; font-size: 0.95em; min-height: 1.5em;"></div>
                </div>
            </div>
        </div>
    </div>
    """
    
    model = genai.GenerativeModel('gemini-2.5-flash')
    response = model.generate_content(prompt)
    
    # Strip out any potential markdown blocks Gemini might accidentally include
    raw_html = response.text.strip()
    if raw_html.startswith("```html"):
        raw_html = raw_html[7:]
    if raw_html.endswith("```"):
        raw_html = raw_html[:-3]
        
    return raw_html.strip()

# --- 4. Update the Local HTML File ---
def update_local_html(new_lesson_html):
    file_path = "index.html"
    
    if not os.path.exists(file_path):
        print(f"Error: {file_path} not found. Make sure index.html is in the same folder.")
        return

    # Read the existing HTML
    with open(file_path, "r", encoding="utf-8") as file:
        soup = BeautifulSoup(file, "html.parser")
    
    container = soup.find(id="lesson-container")
    
    if not container:
        print("Error: Could not find <div id='lesson-container'> in index.html")
        return

    # Insert the new lesson
    new_lesson_soup = BeautifulSoup(new_lesson_html, "html.parser")
    container.insert(0, new_lesson_soup)

    # Keep only the 7 most recent lessons to prevent the page from getting too long
    lessons = container.find_all("details", class_="daily-lesson")
    if len(lessons) > 7:
        for old_lesson in lessons[7:]:
            old_lesson.decompose()

    # Save the modified HTML back to the file
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(str(soup))
    
    print("Successfully updated local index.html!")

if __name__ == "__main__":
    print("Fetching news...")
    news = get_daily_news()
    print("Generating ESL lesson...")
    lesson = generate_lesson_html(news)
    print("Updating local HTML file...")
    update_local_html(lesson)
