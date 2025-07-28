import streamlit as st
from src.core.planner import TravelPlanner
from dotenv import load_dotenv



st.set_page_config(page_title="AI Travel Agent", page_icon=":airplane:")

st.title("AI Travel Agent :airplane:")
st.write("Plan your Day trip itineary by entering your city and interests with AI!")

load_dotenv()

with st.form("planner_form"):
    city = st.text_input("Enter the city you want to visit:")
    interests = st.text_input("Enter your interests (comma separated):")
    
    submit_button = st.form_submit_button("Generate Itinerary")

    if submit_button:
        if city and interests:
            planner = TravelPlanner()
            try:
                planner.set_city(city)
                planner.set_interests(interests)
                itinerary = planner.create_itinerary()
                st.subheader("Itinerary created successfully!")
                st.markdown(itinerary)

            except Exception as e:
                st.error(f"An error occurred: {e}")
        else:
            st.warning("Please fill in both fields to generate an itinerary.")