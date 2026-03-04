import os
import google.generativeai as genai

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")

genai.configure(api_key=GEMINI_API_KEY)

print("Authenticating with Google and checking available models...")

try:
    available_models = False
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(f"AVAILABLE: {m.name}")
            available_models = True
            
    if not available_models:
        print("RESULT: Your API key is valid, but it has no models available for content generation.")
        
except Exception as e:
    print(f"CRITICAL ERROR: {e}")
    print("This usually means the API key itself is invalid or not being passed correctly from GitHub.")