import streamlit as st
from PIL import Image

def main():
    st.set_page_config(page_title="Decovision", layout="wide")
    
    st.title("🌟 Decovision: AI-Based Home Interior Design 🌟")
    st.write("### Experience the future of home interiors with AI and Augmented Reality")
    
    # Product Description
    st.markdown(
        """
        **Decovision** leverages cutting-edge technology to enhance the home design experience.
        Built using Unity 3D, it features Augmented Reality (AR) models representing diverse interior styles across different states of India. 
        
        🌍 **Explore interiors inspired by:**
        - 🏡 **Tamil Nadu**
        - 🎨 **Bengal**
        - 🏠 **Karnataka**
        
        Each state showcases three distinct interior modes:
        - 🛋 **Living Room**
        - 🛏 **Bedroom**
        - 🍽 **Kitchen**
        """,
        unsafe_allow_html=True,
    )
    
    # Add decorative images
    st.image("decorative_image.jpg", use_column_width=True)  # Replace with a colorful banner image
    
    # QR Code Integration with buttons
    st.subheader("🔍 Explore AR Models")
    st.write("Click on a button to view the QR code for the respective interior designs.")
    
    state_options = {"Tamil Nadu": "tn_qr.jpg", "Bengal": "bengal_qr.jpg", "Karnataka": "karnataka_qr.jpg"}
    room_types = {"Living Room": "livingroom.jpg", "Bedroom": "bedroom.jpg", "Kitchen": "kitchen.jpg"}
    
    selected_state = st.selectbox("Choose a State:", list(state_options.keys()))
    selected_room = st.selectbox("Choose a Room Type:", list(room_types.keys()))
    
    if st.button("Show QR Code"):
        qr_code_image = Image.open(state_options[selected_state])
        st.image(qr_code_image, caption=f"Scan to View {selected_room} in {selected_state}", use_column_width=False)
    
    # AI Guide Integration
    st.subheader("🤖 AI Guide: Your Virtual Design Assistant")
    st.write(
        """
        Our AI-powered virtual guide, integrated with ConvAI, assists users in making design choices.
        Engage in conversations with the AI NPC to receive insights about interior aesthetics and personalized recommendations.
        """
    )
    
    st.write("### ✨ Key Features of AI Guide ✨")
    st.write("- 🏡 Provides explanations on different interior styles and elements.")
    st.write("- 🎨 Offers personalized guidance based on user preferences.")
    st.write("- 🗣 Enhances interactivity through natural language processing.")
    
    # Call-to-action
    st.subheader("🚀 Get Started Today!")
    st.write("Download our app and bring your dream home to life with AI-powered design suggestions and AR visualization.")
    
    st.markdown("[📥 Download App](#)")  # Replace '#' with actual download link
    
if __name__ == "__main__":
    main()
