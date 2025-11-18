import streamlit as st
import requests
from io import BytesIO
from PIL import Image
import urllib.parse

st.set_page_config(page_title="Free Text-to-Image Generator")
st.title("🎨 Text-to-Image Generator")

prompt = st.text_input("Enter your prompt:", "A fantasy castle on floating islands")
generate = st.button("Generate Image")

if generate:
    if prompt.strip() == "":
        st.error("Please enter a valid prompt!")
    else:
        st.info("Generating image... please wait 3–5 seconds")

        # Encode prompt for URL
        encoded_prompt = urllib.parse.quote(prompt)

        # Pollinations API (free)
        url = f"https://image.pollinations.ai/prompt/{encoded_prompt}"

        try:
            response = requests.get(url)

            if response.status_code == 200:
                img = Image.open(BytesIO(response.content))
                st.image(img, caption="Generated Image", use_container_width=True)
            else:
                st.error("Image generation failed. Try again.")
        except Exception as e:
            st.error("Error generating image.")
