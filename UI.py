import streamlit as st

# Set the page configuration
st.set_page_config(page_title="Sokyoku-Chat with multiple PDFs", page_icon="🤖")

# Custom CSS for the frosted, translucent effect on the main area and sidebar
st.markdown(
    """
    <style>
    /* Apply a translucent gradient background to the main app area */
    .stApp {
        # background: linear-gradient(135deg, rgba(30, 30, 50, 0.8), rgba(10, 10, 20, 0.8));
        background: radial-gradient(ellipse at top, #081a32, #000000);
        padding: 20px;
        border-radius: 15px;
    }

    /* Style for the sidebar container */
    section[data-testid="stSidebar"] {
        background-color: radial-gradient(#e66465, #9198e5);
        border-radius: 15px;
        padding: 20px;
        background: rgba( 255, 255, 255, 0.05 );
        box-shadow: 0 8px 32px 0 rgba( 31, 38, 135, 0.37 );
        backdrop-filter: blur( 4px );
        -webkit-backdrop-filter: blur( 4px );
        border-radius: 10px;
        border: 1px solid rgba( 255, 255, 255, 0.18 );
    }

    /* Style the header and file uploader in the sidebar */
    section[data-testid="stSidebar"] h2, section[data-testid="stSidebar"] label {
        color: #ffffff;
        font-size: 1.1em;
        text-align: center;
        
    }

    /* Style file uploader box */
    .stFileUploader {
        background-color: #081a32;
        color: #ffffff;
        border-radius: 8px;
        padding: 10px;
        border-style:solid;
        border-width:1px;
        border-color: #ffffff
    }
    .stFileUploader>button {
        background-color: rgba(60, 60, 80, 0.1);
        color: #ffffff;
        border-radius: 8px;
    }

    /* Style input box and buttons */
    .stInput, .stButton>button {
        background-color: rgba(60, 60, 80, 0.1);
        color: #ffffff;
        border-radius: 8px;
    }

    /* Center-align the title and adjust font for clarity */
    h1 {
        text-align: center;
        color: #ffffff;
        font-size: 2em;
    }

    /* Optional: Add box shadow to enhance the "floating" effect */
    .stApp, section[data-testid="stSidebar"] {
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.5);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Your Streamlit content
st.title("Sokyoku-Chat with multiple PDFs:books:")
st.text_input("What can I help with?")

st.sidebar.header("Your Files")
st.sidebar.file_uploader("Upload your files")
st.sidebar.button("Process")
st.button("main area")