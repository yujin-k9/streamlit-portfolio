import streamlit as st

# --- Page Setup ---
st.set_page_config(page_title="Future Work", page_icon="☘️")

# --- Title & Intro ---
st.title("☘️ Future Work")
st.markdown(
    '<p style="color:#5E636C;">Planned improvements and reflections on the development process.</p>',
    unsafe_allow_html=True
)
st.markdown("<hr style='margin-top:8px; margin-bottom:18px;'>", unsafe_allow_html=True)

# --- Section 1: Next Steps ---
st.subheader("➊ Next Steps")
st.markdown("""
This dashboard can evolve into a more advanced analytics product.  
The following next steps outline areas for expansion and refinement:
""")

st.markdown("""
1. **Add Predictive Modeling (Forecasting):**  
   Integrate regression or classification models to predict future health risk scores based on lifestyle factors.


2. **Data Enrichment:**  
   Combine with external datasets (e.g., nutrition or activity trackers) to increase data granularity and improve accuracy.

3. **Enhanced User Interactivity:**  
   Include dynamic sliders, multi-page drill-downs, and live comparison between user groups.

4. **Accessibility and Usability Audit:**  
   Conduct color-contrast and screen-reader tests to ensure inclusivity and adherence to accessibility guidelines.

5. **A/B Layout Experimentation:**  
   Test alternate layouts for KPI positioning and visual hierarchy to identify the most intuitive design.
""")

st.markdown("<hr style='margin-top:15px; margin-bottom:18px;'>", unsafe_allow_html=True)

# --- Section 2: Reflection ---
st.subheader("➋ Reflection on Design Evolution")
st.markdown("""
From **Lab 4.3 Paper Prototype** to the final build, several design and technical improvements were implemented:
""")

st.markdown("""
- **Prototype → Implementation:**  
  The paper prototype outlined basic chart concepts; the final version added full interactivity, filters, and KPIs.

- **Design Refinement:**  
  Early sketches used static visuals, while the final dashboard applies consistent color schemes and responsive layouts.

- **User Experience Focus:**  
  Feedback from lab exercises led to simplified navigation and clear “How to read this chart” sections for accessibility.

- **Reproducibility Emphasis:**  
  The final build integrates a data source link and auto-refresh timestamp to ensure transparent analytics.
""")

st.markdown("<hr style='margin-top:15px; margin-bottom:15px;'>", unsafe_allow_html=True)

# --- Closing Note ---
st.markdown("""
*This project will continue evolving toward a more data-driven, user-focused portfolio product integrating prediction and personalization.*
""")

st.caption("© 2025 Yujin Kim | Streamlit Portfolio Project | MSU Denver – Data Visualization")
