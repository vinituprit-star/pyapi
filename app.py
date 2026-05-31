import os
import streamlit as st
import google.generativeai as genai

# Streamlit Secrets या Environment Variable से API Key उठाना
api_key = os.environ.get("GEMINI_API_KEY")

if not api_key:
    st.error("Error: GEMINI_API_KEY missing!")
else:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-pro')

    # वेबसाइट का इंटरफेस (UI)
    st.title("Gemini AI Assistant")
    st.write("Ask anything to Gemini...")

    user_input = st.text_input("Your Message:", "")

    if st.button("Send"):
        if user_input:
            with st.spinner("Thinking..."):
                response = model.generate_content(user_input)
                st.success(response.text)
        else:
            st.warning("Please enter a message first.")
