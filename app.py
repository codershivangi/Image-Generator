import streamlit as st
import requests

st.set_page_config(page_title="Text-to-Image Generator")
st.title("🖼️ Text-to-Image Generator (Streamlit Cloud Friendly)")

API_URL = "https://api.deepai.org/api/text2img"
API_KEY = "quickstart-QUdJIGlzIGNvbWluZy4uLi4K"  # free demo key

prompt = st.text_input("Enter prompt:", "A beautiful mountain landscape")
generate = st.button("Generate Image")

if generate:
    with st.spinner("Generating image..."):
        response = requests.post(
            API_URL,
            data={"text": prompt},
            headers={"api-key": API_KEY}
        )

        data = response.json()

        if "output_url" in data:
            st.image(data["output_url"], caption="Generated Image")
        else:
            st.error("Error generating image. Try another prompt.")
