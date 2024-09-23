import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn')


st.title('California Housing Data (1990)')
df = pd.read_csv('housing.csv')

# note that you have to use 0.0 and 40.0 given that the data type of population is float
min_price, max_price = st.slider(
    'Select Price Range',
    int(df['median_house_value'].min()),
    int(df['median_house_value'].max()),
    (50000, 500000)  # Default range
)

# Filter the dataframe based on the slider value
df_filtered = df[(df['median_house_value'] >= min_price) & (df['median_house_value'] <= max_price)]
  # min, max, default
# Filter the necessary columns for the map
st.map(df_filtered[['latitude', 'longitude']])
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.hist(df_filtered['median_house_value'], bins=30)
ax.set_xlabel('Median House Value')
ax.set_ylabel('Frequency')

st.pyplot(fig)

location_types = df['location_type'].unique()
selected_types = st.sidebar.multiselect('Filter by Location Type', location_types, default=location_types)
df_filtered = df_filtered[df_filtered['location_type'].isin(selected_types)]
income_level = st.sidebar.radio(
    "Filter by Income Level",
    ('Low (≤2.5)', 'Medium (2.5 - 4.5)', 'High (>4.5)')
)

if income_level == 'Low (≤2.5)':
    df_filtered = df_filtered[df_filtered['median_income'] <= 2.5]
elif income_level == 'Medium (2.5 - 4.5)':
    df_filtered = df_filtered[(df_filtered['median_income'] > 2.5) & (df_filtered['median_income'] < 4.5)]
else:
    df_filtered = df_filtered[df_filtered['median_income'] >= 4.5]
