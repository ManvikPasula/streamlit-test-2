import streamlit as st
from PIL import Image
import moondream as md

st.title("API Image Prompt App")

# Step 1: API Key Input
api_key = st.text_input("Enter your API Key", type="password").strip()

# Step 2: Image Upload
uploaded_image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

# Display the uploaded image right away
if uploaded_image:
    image = Image.open(uploaded_image)
    st.image(image, caption="Uploaded Image", use_container_width=True)

# Step 3: Prompt Input
prompt = st.text_area("Enter your prompt")

# Step 4: Run Button
if st.button("Run"):
    if api_key and uploaded_image and prompt:
        try:
            model = md.vl(api_key=api_key)
            response = model.query(image, prompt)["answer"]

            # Display the response
            st.subheader("Response:")
            st.write(response)
        except Exception as e:
            st.error(f"❌ API Error: {e}")
    else:
        st.warning("Please fill in all fields before running.")
