import os
import google.generativeai as genai

# GitHub Actions या लोकल सिस्टम से API Key उठाना
api_key = os.environ.get("GEMINI_API_KEY")

if not api_key:
    print("Error: GEMINI_API_KEY environment variable missing!")
else:
    # Gemini को कॉन्फ़िगर करना
    genai.configure(api_key=api_key)
    
    # मॉडल सेटअप
    model = genai.GenerativeModel('gemini-pro')
    
    # एक छोटा सा टेस्ट प्रॉम्प्ट
    response = model.generate_content("Hello! System check okay.")
    print("Gemini Response:", response.text)
