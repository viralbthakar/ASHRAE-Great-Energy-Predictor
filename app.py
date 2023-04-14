import streamlit as st
import joblib
import os


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

building_id = st.number_input('Building ID')
meter = st.selectbox('Meter Type', ('electricity',
                     'steam', 'chilledwater', 'hotwater'))
primary_use = st.selectbox('Primary Use', ('Education', 'Lodging/residential', 'Office',
                                           'Entertainment/public assembly', 'Other', 'Retail', 'Parking',
                                           'Public services', 'Warehouse/storage', 'Food sales and service',
                                           'Religious worship', 'Healthcare', 'Utility', 'Technology/science',
                                           'Manufacturing/industrial', 'Services'))
square_feet = st.number_input('Square Feet')
air_temperature = st.number_input('Air Temperature')
cloud_coverage = st.number_input('Cloud Coverage')
precip_depth_1_hr = st.number_input('Percipitation')
sea_level_pressure = st.number_input('Sea Level Pressure')
wind_direction = st.number_input('Wind Direction')
wind_speed = st.number_input('Wind Speed')
hour = st.number_input('Hour')
dayofweek = st.number_input('Day of Week')
month = st.number_input('Month')
day = st.number_input('Day')
isholiday = st.number_input('Holiday')
season = st.number_input('Season')
isdaytime = st.number_input('Day Time')
relative_humidity = st.number_input('Relative Humidity')


data_dict = {
    'building_id': building_id,
    'meter': meter,
    'primary_use': primary_use,
    'square_feet': square_feet,
    'air_temperature': air_temperature,
    'cloud_coverage': cloud_coverage,
    'precip_depth_1_hr': precip_depth_1_hr,
    'sea_level_pressure': sea_level_pressure,
    'wind_direction': wind_direction,
    'wind_speed': wind_speed,
    'hour': hour,
    'dayofweek': dayofweek,
    'month': month,
    'day': day,
    'isHoliday': isholiday,
    'season': season,
    'IsDayTime': isdaytime,
    'relative_humidity': relative_humidity
}
st.write(data_dict)

model_dir = "./models"
models = [f for f in os.listdir(model_dir) if os.path.splitext(f)[
    1] == '.joblib']
model = st.selectbox('Select Model', models)
estimate = st.button("Estimate")

if estimate:
    st.write(os.path.join(model_dir, model))
