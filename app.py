import streamlit as st
from PIL import Image

# App Configuration
st.set_page_config(
    page_title="Lifestyle & Health Risk Portfolio",
    page_icon="🤸‍♀️",
    layout="wide",
)

# --- Branding Header ---
st.title("🤸‍♀️ Lifestyle & Health Risk Prediction")
st.subheader("A Streamlit Portfolio by Yujin Kim")

# Optional profile image or logo
try:
    logo = Image.open("assets/logo.png")
    st.sidebar.image(logo, width=120)
except:
    st.sidebar.write("")

# --- Sidebar Navigation ---
st.sidebar.title("📂 Navigation")
st.sidebar.info(
    "Use the sidebar to explore pages:\n\n"
    "1️⃣ Professional Bio\n"
    "2️⃣ EDA Gallery\n"
    "3️⃣ Dashboard\n"
    "4️⃣ Future Work"
)

st.markdown("---")

# --- Main Introduction ---
st.header("Welcome to My Streamlit Portfolio")
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
st.header("📬 Contact")
col1, col2 = st.columns([1, 3])

with col1:
    try:
        profile = Image.open("assets/hammy.png")
        st.image(profile, caption="Yujin Kim", width=180)
    except:
        st.write("")

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

