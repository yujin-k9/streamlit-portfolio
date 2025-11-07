import streamlit as st
from PIL import Image

st.set_page_config(page_title="Professional Bio", page_icon="🪐")

# --- Title ---
st.title("Professional Bio")
st.markdown(
    "<h4 style='color:#828B9E;'>Data Analytics & Visualization Enthusiast</h4>",
    unsafe_allow_html=True
)


# --- Profile Section ---
col1, col2 = st.columns([1.2, 2.8])

with col1:
    try:
        profile_img = Image.open("assets/hammy.png")
        st.image(profile_img, caption="Yujin Kim", width=220)
        # Alt-text
        st.markdown(
            """
            <span style="font-size:0px;" aria-label="Profile photo of Yujin Kim"></span>
            """,
            unsafe_allow_html=True
        )
    except:
        st.write("_Profile image not available._")

with col2:
    st.markdown(
    """
    <div style='padding-left:20px; margin-top:25px;'>
    I am a <b>senior Computer Science student</b> at <b>Metropolitan State University of Denver</b>.<br>
    I am passionate about transforming raw information into clear, meaningful insights.<br>
    My main interests include <b>data visualization</b> and <b>human-centered analytics design</b>.<br>
    I enjoy creating interactive dashboards that balance <b>storytelling</b>, <b>accuracy</b>, and <b>accessibility</b>.
    </div>
    """,
    unsafe_allow_html=True,
)


# --- Highlights ---
st.markdown("### 🪐༘⋆ Professional Highlights")
st.write(
    """
    - Coursework in **Python**, **Pandas**, **Plotly**, **Altair**, and **Streamlit**  
    - Hands-on experience with **data cleaning**, **EDA**, and **dashboard design**  
    - Familiar with **cloud-based environments** (AWS, GitHub, Google Colab)  
    - Strong focus on **data ethics** and **accessibility standards**  
    - Enthusiastic about **data storytelling and education**
    """
)

# --- Visualization Philosophy ---
st.markdown("### 🪐༘⋆ Visualization Philosophy")
st.write(
    """
    My visualization philosophy centers on **clarity**, **accessibility**, and **integrity**.  
    Every visual must communicate the story behind the data without distortion or unnecessary decoration.  
    I use color-blind-safe palettes, consistent scales, and descriptive labels to ensure fairness and readability for all viewers.  
    Ethical presentation and transparency guide all of my work.  
    """
)

# --- Accessibility Note ---
st.caption(
    "All visuals and images in this portfolio include descriptive alt-text and use contrast-safe color palettes to ensure accessibility."
)
