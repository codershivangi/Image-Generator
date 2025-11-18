import streamlit as st
import torch
from diffusers import StableDiffusionPipeline

# ----------------------------------------------------
# Streamlit UI
# ----------------------------------------------------
st.set_page_config(page_title="Text-to-Image Generator", layout="centered")
st.title("🎨 Text-to-Image Generator")
st.write("Enter a prompt and generate an AI image using Stable Diffusion v1.5.")

# ----------------------------------------------------
# Load Model (cached to avoid reloading every run)
# ----------------------------------------------------
@st.cache_resource
def load_model():
    model_id = "runwayml/stable-diffusion-v1-5"
    pipe = StableDiffusionPipeline.from_pretrained(
        model_id,
        torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
    )
    if torch.cuda.is_available():
        pipe = pipe.to("cuda")
    return pipe

pipe = load_model()

# ----------------------------------------------------
# User Input
# ----------------------------------------------------
prompt = st.text_input("Enter your prompt:", "A cute baby elephant wearing a hat")

generate_btn = st.button("Generate Image")

# ----------------------------------------------------
# Generate Image
# ----------------------------------------------------
if generate_btn:
    if prompt.strip() == "":
        st.warning("Please enter a valid prompt!")
    else:
        with st.spinner("Generating image..."):
            image = pipe(prompt).images[0]
            st.image(image, caption="Generated Image", use_container_width=True)
