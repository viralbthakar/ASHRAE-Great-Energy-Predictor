import streamlit as st


st.set_page_config(
    page_title="Energy Consumption Estimation",
    page_icon=":zap:",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.linkedin.com/in/viralbthakar/',
        'Report a bug': "https://github.com/viralbthakar/fire-and-blood-qa/issues/new/choose",
        'About': "This is an *extremely* cool app!"
    }
)

st.title("Energy Consumption Estimation")
st.write("Counterfactual Model Development for Energy Consumption Estimation")
