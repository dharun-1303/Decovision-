import streamlit as st
from PIL import Image

def main():
    st.set_page_config(page_title="Decovision", layout="wide")
    
    st.title("AI-Based Home Interior Design")
    st.write("### Experience the future of home interiors with AI and Augmented Reality")
    
    # Product Description
    st.write("""
    Our AI-Based Home Interior Design application leverages cutting-edge technology to enhance the home design experience. 
    Built using Unity 3D, it features Augmented Reality (AR) models representing diverse interior styles across different states of India. 
    
    Explore interiors inspired by:
    - **Tamil Nadu**
    - **Bengal**
    - **Karnataka**
    
    Each state showcases three distinct interior modes:
    - **Living Room**
    - **Bedroom**
    - **Kitchen**
    """)
    
    # AR Model Visualization
    st.subheader("Explore AR Models")
    st.write("Scan the QR code below to visualize the interior designs in Augmented Reality.")
    
    
    
    # AI Guide Integration
    st.subheader("AI Guide: Your Virtual Design Assistant")
    st.write("""
    Our AI-powered virtual guide, integrated with ConvAI, assists users in making design choices. Engage in conversations with 
    the AI NPC to receive insights about interior aesthetics and personalized recommendations.
    """)
    
    st.write("### Key Features of AI Guide")
    st.write("- Provides explanations on different interior styles and elements.")
    st.write("- Offers personalized guidance based on user preferences.")
    st.write("- Enhances interactivity through natural language processing.")
    
    # Call-to-action
    st.subheader("Get Started Today!")
    st.write("Download our app and bring your dream home to life with AI-powered design suggestions and AR visualization.")
    
    st.markdown("[Download App](#)")  # Replace '#' with actual download link
    
if __name__ == "__main__":
    main()
