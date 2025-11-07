import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px

st.set_page_config(page_title="EDA Gallery", page_icon="📊")

st.title("📊 EDA Gallery")
st.write("### Exploratory Data Analysis on Lifestyle and Health Risk Dataset")

# Load dataset
df = pd.read_csv("data/Lifestyle_and_Health_Risk_Prediction_Synthetic_Dataset.csv")
sns.set_palette("colorblind")

st.markdown(
    """
    <p style="color:#5E636C; margin-bottom:6px;">
    This gallery explores relationships between lifestyle habits and overall health risk among 5,000 individuals.
    </p>
    <hr style="margin-top:10px; margin-bottom:15px;">
    """,
    unsafe_allow_html=True
)

# -----------------------------
# 1️⃣ Chart 1: Exercise vs Health Risk (Bar Chart)
# -----------------------------
st.markdown("### ➊ Exercise Frequency vs Health Risk")
st.markdown(
    '<p style="color:#CD404B;"><i>Question: How does exercise level relate to overall health risk?</i></p>',
    unsafe_allow_html=True
)

risk_map = {"low": 1, "medium": 2, "high": 3}
df["risk_score"] = df["health_risk"].map(risk_map)

exercise_risk = df.groupby("exercise", as_index=False)["risk_score"].mean()

order = ["none", "low", "medium", "high"]
exercise_risk["exercise"] = pd.Categorical(exercise_risk["exercise"], categories=order, ordered=True)
exercise_risk = exercise_risk.sort_values("exercise")


bar_fig = go.Figure(
    data=[
        go.Bar(
            x=exercise_risk["exercise"],
            y=exercise_risk["risk_score"],
            marker_color=px.colors.qualitative.Safe,
            width=[0.8, 0.8, 0.8, 0.8], 
            hovertemplate="<b>%{x}</b><br>Health Risk Score: %{y:.4f}<extra></extra>"
        )
    ]
)

bar_fig.update_layout(
    title="Average Health Risk Score by Exercise Level",
    xaxis_title="exercise",
    yaxis_title="risk_score",
    bargap=0.1,
)

st.plotly_chart(bar_fig, use_container_width=True)

st.markdown("**How to read this chart:**")
st.markdown("""
- The x-axis represents weekly exercise frequency categories.  
- The y-axis shows the average numeric health risk score (1=Low, 3=High).  
- Each color corresponds to an exercise group.  
- Shorter bars indicate lower average risk.
""")

st.markdown("**Insights:**")
st.markdown("""
- Individuals who exercise more frequently show lower average health risk scores.  
- Sedentary and low-exercise groups have the highest mean risk.  
- This suggests a clear inverse relationship between physical activity and health risk.
""")



# -----------------------------
# 2️⃣ Chart 2: Sleep Duration vs BMI (Clean Scatter)
# -----------------------------
st.markdown("### ➋ Sleep Duration vs BMI")
st.markdown(
    '<p style="color:#CD404B;"><i>Question: How does sleep duration relate to body mass index (BMI)?</i></p>',
    unsafe_allow_html=True
)

# Reduce points for better visibility
scatter_df = df.sample(200, random_state=42)

# Simple 2-variable scatter plot
scatter_fig = px.scatter(
    scatter_df,
    x="sleep",
    y="bmi",
    color_discrete_sequence=["#1f77b4"],
    opacity=0.8,
    title="Sleep Duration vs BMI",
    render_mode="svg"
)

# Style adjustments for clarity
scatter_fig.update_traces(marker=dict(size=8))
scatter_fig.update_layout(
    xaxis_title="Average Sleep Hours per Night",
    yaxis_title="Body Mass Index (BMI)",
    plot_bgcolor="white",
    paper_bgcolor="white"
)

st.plotly_chart(scatter_fig, use_container_width=True)

st.markdown("**How to read this chart:**")
st.markdown("""
- Each dot represents one person in the dataset.  
- The x-axis shows the average number of sleep hours per night.  
- The y-axis shows each person’s body mass index (BMI).  
- The spread of points indicates how BMI varies with different sleep durations.  
- Clusters or gaps reveal where most individuals fall in the sleep–BMI range.
""")

st.markdown("**Insights:**")
st.markdown("""
- Most people cluster around 7 hours of sleep and BMI between 18 and 30.  
- No clear linear trend, but moderate sleep links to stable BMI.  
- Regular sleep supports weight balance, not direct BMI prediction.
""")

# -----------------------------
# 3️⃣ Chart 3: Alcohol vs BMI (Box Plot)
# -----------------------------
st.markdown("### ➌ Alcohol vs BMI")
st.markdown(
    '<p style="color:#CD404B;"><i>Question: How does BMI vary between drinkers and non-drinkers?</i></p>',
    unsafe_allow_html=True
)

fig3 = px.box(
    df,
    x="alcohol",
    y="bmi",
    color="alcohol",
    color_discrete_sequence=px.colors.qualitative.Set2,
    title="Distribution of BMI by Alcohol Consumption",
    points="outliers"
)

fig3.update_layout(
    xaxis_title="Alcohol Consumption",
    yaxis_title="Body Mass Index (BMI)",
    plot_bgcolor="white",
    paper_bgcolor="white",
    showlegend=False
)

st.plotly_chart(fig3, use_container_width=True)

st.markdown("**How to read this chart:**")
st.markdown("""
- Each box shows the BMI distribution for drinkers and non-drinkers.  
- The line in the box is the median BMI.  
- Taller boxes mean more variation; dots represent outliers.
""")

st.markdown("**Insights:**")
st.markdown("""
- Both groups show nearly identical medians and distributions.  
- Alcohol consumption does not have a significant effect on BMI changes.  
- However, the non-drinker group shows extremely high BMI outliers.  
→ This suggests that while the average difference is minimal, some non-drinkers may have severe obesity.
""")


# -----------------------------
# 4️⃣ Chart 4: Correlation Between Numeric Variables (Heatmap)
# -----------------------------
st.markdown("### ➍ Correlation Between Numeric Variables")
st.markdown(
    '<p style="color:#CD404B;"><i>Question: Do older individuals tend to have higher health risk scores?</i></p>',
    unsafe_allow_html=True
)

corr = df.corr(numeric_only=True)
fig4, ax4 = plt.subplots()
sns.heatmap(corr, cmap="YlGnBu", annot=True, fmt=".2f", linewidths=0.5)
st.pyplot(fig4)

st.markdown("**How to read this chart:**")
st.markdown("""
- Each cell shows the Pearson correlation coefficient between two numeric variables.  
- Darker blue means a stronger positive relationship, while lighter colors indicate weaker or negative correlations.  
- Values close to 1.00 or -1.00 show strong associations, while those near 0.00 indicate little to no relationship.
""")

st.markdown("**Insights:**")
st.markdown("""
- **Older individuals tend to have slightly higher health risk scores**, as shown by the weak positive correlation between age and risk_score (r = **0.38**).  
- Weight and BMI have the strongest positive relationship (r = 0.78), which is expected since BMI is derived from weight.  
- BMI also shows a modest positive correlation with health risk (r = 0.36).  
- Sleep shows a weak negative correlation with health risk (r = -0.14), suggesting more sleep may slightly reduce risk.
""")



# -----------------------------
# Accessibility Footer
# -----------------------------
st.caption("All visuals use color-blind-safe palettes and descriptive titles for accessibility.")
