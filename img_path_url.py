import streamlit as st
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# Set Streamlit page config
st.set_page_config(page_title="FERRARI Image Processor", layout="wide")

# Title
st.title("FERRARI Image - Multi-Color Channel Visualizer")

# Load image from URL
@st.cache_data
def load_image():
    path = r"C:\Users\Tharuni\Desktop\NIT\july month\22nd_Advance python Funtions\23rd_Adv python proj\ferrari.jpg"
    return Image.open(path).convert("RGB")
# Load and display image
elephant = load_image()
st.image(elephant, caption="Original FERRARI Image", use_container_width=True)

# Convert to NumPy array
elephant_np = np.array(elephant)
R, G, B = elephant_np[:, :, 0], elephant_np[:, :, 1], elephant_np[:, :, 2]

# Create channel images
red_img = np.zeros_like(elephant_np)
green_img = np.zeros_like(elephant_np)
blue_img = np.zeros_like(elephant_np)

red_img[:, :, 0] = R
green_img[:, :, 1] = G
blue_img[:, :, 2] = B

# Display RGB channels
st.subheader("RGB Channel Visualization")
col1, col2, col3 = st.columns(3)

with col1:
    st.image(red_img, caption="Red Channel", use_container_width=True)

with col2:
    st.image(green_img, caption="Green Channel", use_container_width=True)

with col3:
    st.image(blue_img, caption="Blue Channel", use_container_width=True)

# Grayscale + Colormap
st.subheader("Colormapped Grayscale Image")

colormap = st.selectbox(
    "Choose a Matplotlib colormap",
    ["viridis", "plasma", "inferno", "magma", "cividis", "hot", "cool", "gray"]
)

elephant_gray = elephant.convert("L")
elephant_gray_np = np.array(elephant_gray)

# Plot using matplotlib with colormap
fig, ax = plt.subplots(figsize=(6, 4))
im = ax.imshow(elephant_gray_np, cmap=colormap)
plt.axis("off")

# DO NOT USE: plt.show()
# USE THIS INSTEAD:
st.pyplot(fig)