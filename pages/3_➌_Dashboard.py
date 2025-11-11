import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime
import pytz

denver_tz = pytz.timezone("America/Denver")
local_time = datetime.now(denver_tz)

# --- Page Setup ---
st.set_page_config(page_title="Health Risk Dashboard", page_icon="📈")

# --- Title & Intro ---
st.title("📈 Health Risk Dashboard")
st.markdown(
    '<p style="color:#5E636C;">Interactive summary of lifestyle factors and health risk patterns.</p>',
    unsafe_allow_html=True
)

# --- Load Data ---
df = pd.read_csv("data/Lifestyle_and_Health_Risk_Prediction_Synthetic_Dataset.csv")

# Convert health_risk to numeric score
risk_map = {"low": 1, "medium": 2, "high": 3}
df["risk_score"] = df["health_risk"].map(risk_map)

# --- Sidebar Filters ---
st.sidebar.header("Filter Options")
exercise_filter = st.sidebar.multiselect(
    "Exercise Level",
    df["exercise"].unique(),
    default=df["exercise"].unique()
)
age_filter = st.sidebar.slider(
    "Select Age Range",
    int(df["age"].min()),
    int(df["age"].max()),
    (20, 60)
)
alcohol_filter = st.sidebar.radio(
    "Alcohol Consumption",
    ["All", "Yes", "No"],
    index=0
)

# --- Apply Filters ---
filtered_df = df[
    (df["exercise"].isin(exercise_filter))
    & (df["age"].between(age_filter[0], age_filter[1]))
]
if alcohol_filter != "All":
    filtered_df = filtered_df[
        filtered_df["alcohol"].str.lower() == alcohol_filter.lower()
    ]

# --- KPI Section ---
col1, col2, col3 = st.columns(3)

col1.metric("Average BMI", f"{filtered_df['bmi'].mean():.1f}")
col2.metric("Average Sleep Duration (hrs)", f"{filtered_df['sleep'].mean():.1f}")

high_risk_percent = (
    filtered_df['health_risk'].value_counts(normalize=True).get('high', 0) * 100
)
col3.metric("Individuals at Higher Health Risk (%)", f"{high_risk_percent:.1f}%")

# Custom horizontal line with tight spacing
st.markdown(
    "<hr style='margin-top:8px; margin-bottom:18px;'>",
    unsafe_allow_html=True
)


# --- Chart 1: Scatter (Age vs BMI) ---
st.markdown("### ➊ BMI vs Age by Health Risk")
fig1 = px.scatter(
    filtered_df,
    x="age",
    y="bmi",
    color="health_risk",
    opacity=0.7,
    title="BMI vs Age by Health Risk",
    color_discrete_map={
        "high": "#ec5300",
        "low": "#7FBF7F",
    },
    render_mode="svg"
)
st.plotly_chart(fig1, use_container_width=True)


# --- Chart 2: Bar (Sleep vs Exercise) ---
st.markdown("### ➋ Average Sleep Duration by Exercise Level")
sleep_exercise = filtered_df.groupby("exercise", as_index=False)["sleep"].mean()

fig2 = px.bar(
    sleep_exercise,
    x="exercise",
    y="sleep",
    color="exercise",
    title="Average Sleep Hours by Exercise Level",
    text_auto=".1f",
    color_discrete_map={
        "none": "#6fa8dc",   
        "low": "#5886b0",    
        "medium": "#37546e", 
        "high": "#0b1016"    
    },
    category_orders={"exercise": ["none", "low", "medium", "high"]}
)
st.plotly_chart(fig2, use_container_width=True)



# --- Chart 3: Pie (Health Risk Distribution) ---
st.markdown("### ➌ Health Risk Distribution")
fig3 = px.pie(
    filtered_df,
    names="health_risk",
    title="Proportion of Health Risk Levels",
    color="health_risk",
    color_discrete_map={
        "high": "#ec5300",
        "low": "#7FBF7F",
    }
)
st.plotly_chart(fig3, use_container_width=True)


# --- Insights ---
st.markdown("**Insights:**")
st.markdown("""
- Adults aged 40–70 who engage in little or no exercise tend to show higher BMI and greater health risk levels overall.  
- Alcohol consumption appears to amplify this trend, suggesting that inactivity and alcohol use together may raise health vulnerability.  
- Average sleep duration remains relatively consistent across groups, indicating that sleep alone does not significantly alter health outcomes.  
- Compared to the overall dataset, this subset highlights how combined lifestyle factors—age, exercise, and alcohol—interact to influence health risk.  
- These results emphasize moderation and balanced habits rather than a single determining factor of health.
""")


# --- Footer / Reproducibility Section ---
st.markdown("---")
st.markdown("### 🔍 Data Source & Reproducibility")

st.markdown(
    """
    **Dataset:** [Lifestyle and Health Risk Prediction (Synthetic)](https://www.kaggle.com/datasets/miadul/lifestyle-and-health-risk-prediction)    
    **Data Notes:** Synthetic dataset generated for educational use.  
    Charts and KPIs update dynamically based on sidebar filters to ensure reproducibility.
    """
)

# One-line “Last Refreshed” timestamp (dynamic)
st.caption(f"Last refreshed: {local_time.strftime('%B %d, %Y at %I:%M %p')}")


# -----------------------------
# Accessibility & Ethics Footer
# -----------------------------
st.markdown("---")
st.caption(
    "🧭 Ethics & Accessibility Note: This dataset is synthetic and does not include real individuals. "
    "All visuals use color-blind-safe palettes, clear labeling, and descriptive titles for accessibility. "
    "Charts illustrate general trends only and are not intended for individual-level prediction."
)