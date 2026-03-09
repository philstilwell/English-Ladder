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
    2. Section III must be an interactive 7-item multiple-choice quiz. 
    3. Use the exact inline structure provided below. Do not alter the onclick JavaScript. 
    4. CRITICAL: When filling in the data-feedback attribute, DO NOT use double quotes (") in your explanations, as it will break the HTML attribute. Single quotes and apostrophes are perfectly fine. Do NOT provide a separate answer key section.
    
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
                        <button style="text-align: left; padding: 10px; border: 1px solid #d2b48c; border-radius: 5px; background: #fff; cursor: pointer; font-size: 1em; transition: 0.2s;" 
                                data-bg="#ffe6e6" data-color="#b22222" data-feedback="❌ <strong>Incorrect:</strong> [Explain why this option is wrong]" 
                                onclick="let p = this.parentElement; Array.from(p.children).forEach(b => b.style.backgroundColor='#fff'); this.style.backgroundColor=this.dataset.bg; let f = p.nextElementSibling; f.innerHTML=this.dataset.feedback; f.style.color=this.dataset.color;">
                            a) [Option A]
                        </button>
                        <button style="text-align: left; padding: 10px; border: 1px solid #d2b48c; border-radius: 5px; background: #fff; cursor: pointer; font-size: 1em; transition: 0.2s;" 
                                data-bg="#e6ffe6" data-color="#2e8b57" data-feedback="✅ <strong>Correct:</strong> [Explain why this option is right]" 
                                onclick="let p = this.parentElement; Array.from(p.children).forEach(b => b.style.backgroundColor='#fff'); this.style.backgroundColor=this.dataset.bg; let f = p.nextElementSibling; f.innerHTML=this.dataset.feedback; f.style.color=this.dataset.color;">
                            b) [Option B]
                        </button>
                        <button style="text-align: left; padding: 10px; border: 1px solid #d2b48c; border-radius: 5px; background: #fff; cursor: pointer; font-size: 1em; transition: 0.2s;" 
                                data-bg="#ffe6e6" data-color="#b22222" data-feedback="❌ <strong>Incorrect:</strong> [Explain why this option is wrong]" 
                                onclick="let p = this.parentElement; Array.from(p.children).forEach(b => b.style.backgroundColor='#fff'); this.style.backgroundColor=this.dataset.bg; let f = p.nextElementSibling; f.innerHTML=this.dataset.feedback; f.style.color=this.dataset.color;">
                            c) [Option C]
                        </button>
                    </div>
                    <div class="feedback" style="margin-top: 12px; font-size: 0.95em; min-height: 1.5em;"></div>
                </div>
            </div>
        </div>
    </div>
    """
    
    model = genai.GenerativeModel('gemini-2.5-flash')
    response = model.generate_content(prompt)
    
    raw_html = response.text.strip()
    if raw_html.startswith("```html"):
        raw_html = raw_html[7:]
    if raw_html.endswith("```"):
        raw_html = raw_html[:-3]
        
    return raw_html.strip()
