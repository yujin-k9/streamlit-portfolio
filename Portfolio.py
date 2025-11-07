import streamlit as st
from PIL import Image

# App Configuration
st.set_page_config(
    page_title="Lifestyle & Health Risk Portfolio",
    page_icon="🤸‍♀️",
    layout="wide",
)

# --- Branding Header ---
st.markdown(
    "<h1 style='color:black'>🤸‍♀️ Lifestyle & Health Risk Prediction</h1>",
    unsafe_allow_html=True
)
st.markdown(
    "<h4 style='color:#91A3B4;'>A Streamlit Portfolio by Yujin Kim</h4>",
    unsafe_allow_html=True
)

# Optional profile image or logo
try:
    logo = Image.open("assets/logo.png")
    st.sidebar.image(logo, width=120)
except:
    st.sidebar.write("")

# --- Sidebar Navigation ---
st.sidebar.title("🔍 Navigation")
st.sidebar.markdown(
    "Curious to learn more? Explore each section through the tabs above.",
)

# --- Main Introduction ---
st.markdown(
    "<h3 style='color:#234769;'>Welcome to My Streamlit Portfolio!</h3>",
    unsafe_allow_html=True
)
st.write(
    """
    This multi-page Streamlit application demonstrates my ability to perform data-driven storytelling 
    using Python, Pandas, Plotly, and Streamlit.

    The dataset used here represents **5,000 individuals’ lifestyle factors** (age, exercise, sleep, sugar intake, 
    BMI, smoking, alcohol, etc.) and their corresponding **health risk levels**.

    Each page highlights a key aspect of my analytics process:
    - **Bio Page:** My background, interests, and visualization philosophy  
    - **EDA Gallery:** Exploratory data analysis with interactive charts  
    - **Dashboard:** Filters, KPIs, and actionable insights  
    - **Future Work:** Next steps and reflection
    """
)

st.markdown("---")

# --- Contact / Branding Section ---
st.markdown(
    "<h3 style='color:black;'>📬 Contact</h3>",
    unsafe_allow_html=True
)

col1, col2 = st.columns([1, 3])

with col1:
    st.image("assets/hammy.png", caption="Yujin Kim", width=180)
    # Alt-text
    st.markdown(
        """
        <span style="font-size:0px;" aria-label="Profile photo of Yujin Kim"></span>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.write("**Email:** ykim20@msudenver.edu")  
    st.write("**LinkedIn:** [linkedin.com/in/yujinkimdev](https://www.linkedin.com/in/yujinkimdev/)")
    st.write("**GitHub:** [github.com/yujin-k9](https://github.com/yujin-k9)")
    st.write(
        """
        **Visualization Philosophy:**  
        Clarity, accessibility, and integrity are my guiding principles.  
        I use color-blind-safe palettes, balanced layouts, and clear labeling 
        to ensure all visuals remain interpretable and ethical.
        """
    )

st.markdown("---")
st.caption("© 2025 Yujin Kim | Streamlit Portfolio Project | MSU Denver – Data Visualization")

