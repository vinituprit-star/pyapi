import os
import streamlit as st
from google import genai

# Streamlit Secrets से API Key उठाना
api_key = os.environ.get("GEMINI_API_KEY")

if not api_key:
    st.error("Error: GEMINI_API_KEY missing!")
else:
    # नए SDK के हिसाब से क्लाइंट बनाना
    client = genai.Client(api_key=api_key)

    st.title("Gemini AI Assistant")
    st.write("Ask anything to Gemini...")

    user_input = st.text_input("Your Message:", "")

    if st.button("Send"):
        if user_input:
            with st.spinner("Thinking..."):
                # नए 3.5-flash मॉडल को कॉल करना
                response = client.models.generate_content(
                    model="gemini-3.5-flash",
                    contents=user_input,
                )
                st.success(response.text)
        else:
            st.warning("Please enter a message first.")
