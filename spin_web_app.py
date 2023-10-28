import streamlit as st
import pandas as pd
from PIL import Image

def domain_filter(domain, difficulty):
    domain_data = data.groupby('Domain')
    given_domain_data = domain_data.get_group(domain)
    
    diff_domain_data = given_domain_data.groupby('Difficulty Level')
    return diff_domain_data.get_group(difficulty)

try: 
    img = Image.open('lightbulb.jpeg')
    st.image(img)

    st.header("SPIN - Simple Project Idea Navigator")
    st.subheader("Fill the following to get required Project Idea :bulb:")

    data = pd.read_csv('project_ideas_dataset.csv')

    st.subheader(":pushpin: 1. Enter Domain")
    domain_options = data['Domain'].unique()
    selected_domain = st.selectbox("Select the domain you are interested in", domain_options)

    st.subheader(":pushpin: 2. Enter Difficulty Level")
    selected_difficulty_level = st.selectbox("Choose a difficulty level", ['Beginner','Intermediate','Advanced'])

    filtered_data = domain_filter(selected_domain, selected_difficulty_level)

    st.subheader(":pushpin: 3. Choose Output size")
    with st.expander("Output size"):    
        num_unique_projects = len(filtered_data['Project Name'].unique())
        data_size = st.slider('Enter Output size', 1, num_unique_projects, 2)

    shuffled_data = filtered_data.sample(frac=1, random_state=42)
    random_rows = shuffled_data.sample(data_size)

    shuffle_button = st.button("Shuffle")

    if shuffle_button:
        shuffled_data = filtered_data.sample(frac=1, random_state=42)
        random_rows = shuffled_data.sample(data_size)

    st.header("Results :mega:")
    if random_rows.empty:
        st.error("No projects found. Please try different filters.")
    else:
        for _, row in random_rows.iterrows():
            with st.expander(f'**{row["Project Name"]}**'):
                st.markdown(f"**Description:** {row['Description']}")
                st.markdown(f"**Type of Model:** {row['Type of Model']}")
                st.markdown(f"**Type of Data used:** {row['Data Type']}")
                st.markdown(f"**Tools/Libraries Used:** {row['Tools/Libraries Used']}")
                st.markdown(f"**Keywords/Tags:** {row['Keywords/Tags']}")

except Exception:
    st.error("No projects found. Please try different filters.")