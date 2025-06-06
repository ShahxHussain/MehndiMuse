from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO
import base64
import streamlit as st
from dotenv import load_dotenv
import os
import random


# Step 1: Configure your API key
# Load environment variables from .env file
load_dotenv()

# Access the API key
api_key = os.getenv("API_KEY")
client = genai.Client(api_key=api_key)  # Replace with your actual API key

# Set custom page config and theme
st.set_page_config(
    page_title="MehndiMuse ",
    page_icon="🌸",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for colors
st.markdown(
    """
    <style>
    /* Main background */
    .stApp {
        background-color: #f9fafb;
    }
    /* Sidebar background */
    section[data-testid="stSidebar"] {
        background-color: #f3f4f6;
    }
    /* Main title */
    .main-title {
        color: #2d3748;
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        margin-top: 1.5rem;
    }
    /* Subtitle */
    .subtitle {
        color: #2563eb;
        font-size: 1.5rem;
        text-align: center;
        margin-bottom: 2rem;
    }
    /* Widget label color */
    label, .stSlider label, .stSelectbox label {
        color: #1a202c !important;
        font-weight: 600;
    }
    /* Button color */
    .stButton>button {
        background-color: #2563eb;
        color: white;
        border-radius: 8px;
        font-weight: bold;
        border: none;
        padding: 0.5rem 1.5rem;
    }
    .stButton>button:hover {
        background-color: #1e40af;
        color: #f9fafb;
    }
    /* Image border */
    .element-container img {
        border: 4px solid #2563eb;
        border-radius: 16px;
        background: #fff;
    }
    /* Sidebar toggler (hamburger/arrow) */
    [data-testid="collapsedControl"] svg {
        color: #111 !important;
        fill: #111 !important;
    }
    [data-testid="collapsedControl"] {
        background: #fff !important;
        border: 1.5px solid #111 !important;
        border-radius: 8px !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Main Title and Subtitle
st.markdown('<div class="main-title">🌸 MehndiMuse </div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle" style="color:#e75480;">Eid Mubarak - Let us color your hands :) </div>', unsafe_allow_html=True)

# Quotes for girls
mehndi_quotes = [
    "Mehndi adorns the hands and life takes on a new color.",
    "Let your hands do the talking with beautiful Mehndi designs!",
    "Every girl is incomplete without the fragrance of Mehndi on Eid.",
    "Eid is incomplete without the beauty of Mehndi on your hands.",
    "The deeper the Mehndi, the stronger the love!"
]

# Sidebar for all settings
with st.sidebar:
    st.markdown('<h2 style="color: #000;">Customize Your Mehndi Design</h2>', unsafe_allow_html=True)
    mehndi_type = st.selectbox(
        "Select the Type of Mehndi Design",
        [
            "Pakistani Mehndi Design - Intricate patterns with floral and geometric motifs.",
            "Arabic Mehndi Design - Bold, floral patterns with long, flowing lines.",
            "Indian Mehndi Design - Detailed designs with peacock motifs and rich patterns.",
            "Portrait Mehndi Design - Artistic designs with portraits or faces.",
            "Moroccan Mehndi Design - Geometric and symmetric designs with bold patterns.",
            "Bridal Mehndi Design - Complex designs typically used for weddings, covering hands and feet.",
            "Jewellery Mehndi Design - Mehndi designs inspired by jewelry patterns, often with elegant curves.",
            "Tattoo Mehndi Design - Modern, minimalist designs often resembling tattoos.",
            "Western-style Mehndi - Contemporary designs with a fusion of mehndi and Western art.",
            "African Mehndi Design - Bold and simple designs with circular and linear patterns.",
            "Punjabi Mehndi Design - Vibrant, bold patterns with motifs from Punjabi culture."
        ]
    )
    hand_type = st.selectbox(
        "Select the Age Range of the Hand Type",
        [
            "Toddlerhood (2-4 years)",
            "Childhood (5-12 years)",
            "Adolescence (13-19 years)",
            "Young Adulthood (20-39 years)",
            "Middle Adulthood (40-59 years)",
            "Senior Adulthood (60+ years)"
        ]
    )
    occasion = st.selectbox(
        "Select Occasion",
        ['Eid', 'Wedding', 'Festival', 'Party', 'Casual', 'Other'],
        index=0
    )
    complexity = st.slider(
        "Select the Complexity of Design",
        1,  # Minimum complexity
        5,  # Maximum complexity
        1,  # Default value now 1
        step=1,  # Step size
        format="%d",  # Display format
        help="1 is Simple, 5 is Complex"
    )
    user_command = st.text_input("If you want to write something on your hand also Enter here (optional):", value="")
    num_images = st.slider("Select Number of Images", min_value=1, max_value=10, value=3)

# Custom CSS for black Generate button
st.markdown(
    """
    <style>
    .stButton>button {
        background-color: #111 !important;
        color: white !important;
        border-radius: 8px;
        font-weight: bold;
        border: none;
        padding: 0.5rem 1.5rem;
    }
    .stButton>button:hover {
        background-color: #333 !important;
        color: #f9fafb !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Function to add a white background to images with transparency
def add_white_background(img):
    # Ensure the image is in RGBA format (it will include transparency)
    img = img.convert("RGBA")

    # Check if the image has an alpha channel (transparency)
    if img.mode == 'RGBA':
        # Create a white background image with the same size as the original image
        background = Image.new("RGBA", img.size, (255, 255, 255, 255))
        # Paste the original image onto the white background using its alpha channel as mask
        background.paste(img, (0, 0), img)
        # Convert back to RGB (no alpha channel, no transparency)
        img = background.convert("RGB")
    else:
        # If no alpha channel exists, just convert directly to RGB
        img = img.convert("RGB")
    return img

# Function to determine the hand description based on the hand type selected
def get_hand_description(hand_type):
    if hand_type == "Toddlerhood (2-4 years)":
        return "a toddler's hand, including both the palm and the back of the hand"
    elif hand_type == "Childhood (5-12 years)":
        return "a child's hand, including both the palm and the back of the hand"
    elif hand_type == "Adolescence (13-19 years)":
        return "a teenager's hand, including both the palm and the back of the hand"
    elif hand_type == "Young Adulthood (20-39 years)":
        return "an adult's hand, including both the palm and the back of the hand"
    elif hand_type == "Middle Adulthood (40-59 years)":
        return "a middle-aged adult's hand, including both the palm and the back of the hand"
    elif hand_type == "Senior Adulthood (60+ years)":
        return "a senior adult's hand, including both the palm and the back of the hand"
    else:
        return "an adult's hand, including both the palm and the back of the hand"  # Default case for adult hands

# Button to generate the content
if st.button("Generate"):
    # Show loader and quotes while generating
    with st.spinner("Generating your beautiful Mehndi design..."):
        st.markdown(
            f'<div style="color:#2563eb; font-size:1.1rem; margin-bottom:1rem; text-align:center;">'
            + '<br>'.join(random.sample(mehndi_quotes, 3)) + '</div>',
            unsafe_allow_html=True
        )
        # Get the hand type description based on the user's selection
        hand_description = get_hand_description(hand_type)

        # Build the base prompt
        detailed_command = (
            f"You are an expert Mehndi artist. Generate a clear and realistic image of ONE human hand only — "
            "the hand must have EXACTLY 5 distinct fingers: 1 thumb and 4 fingers. No extra fingers, double thumbs, or merged fingers. "
            "The fingers and thumb should be naturally spaced, and the arm must be included. Do NOT show two hands or mirrored views. "
            f"The hand must clearly resemble this description: {hand_description}. "
            "Show only a single hand with a white background — no home or parlor backgrounds. "
            "Ensure the palm AND the back of the hand are visible in the design (you may use a 3D-style view or split-view layout). "
            f"Generate a  {mehndi_type} style Mehndi design suitable for a {occasion}, "
            f"with a {complexity} complexity level. "
            "Do NOT generate more than one hand or any other object in the image."
        )

        # If user_command is provided, append it to the prompt
        if user_command.strip():
            detailed_command += f" Also, write the following text on the hand: '{user_command.strip()}'."

        # Initialize list to hold images
        images = []

        # Loop to generate multiple images
        for _ in range(num_images):
            try:
                # Call the AI model to generate content based on the user command
                response = client.models.generate_content(
                    model="gemini-2.0-flash-exp-image-generation",
                    contents=detailed_command,
                    config=genai.types.GenerateContentConfig(
                        response_modalities=['Text', 'Image']  # Requesting both Text and Image
                    )
                )

                # Process the response to get images
                for part in response.candidates[0].content.parts:
                    if part.inline_data is not None:
                        image = Image.open(BytesIO(part.inline_data.data))  # Convert byte data to image
                        # Ensure the image has a white background
                        image = add_white_background(image)
                        images.append(image)  # Add image to the list

            except Exception as e:
                st.error(f"Error: {e}")
                break

        # Check if images were generated
        if images:
            # Set the fixed width and height for each image (larger size now)
            image_width = 600  # Larger width in pixels
            image_height = 700  # Larger height in pixels

            # Display images in a single row, with fixed width and height
            cols = st.columns(len(images))  # Create columns equal to the number of images

            for idx, img in enumerate(images):
                # Resize the image to fit the desired width and height
                img = img.resize((image_width, image_height))

                with cols[idx]:
                    st.image(img, caption=f"Generated Mehndi Design {idx + 1}", use_container_width=False)

        else:
            st.error("No images generated. Please try again.")
