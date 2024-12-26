import streamlit as st
import requests
from typing import List

def create_learning_path(topics: List[str], skill_level: str, time_frame: str, simplification_level: int):
    url = "http://localhost:8000/learning-path/"
    data = {
        "topics": topics,
        "skill_level": skill_level,
        "time_frame": time_frame,
        "simplification_level": simplification_level
    }
    try:
        response = requests.post(url, json=data)
        if response.status_code != 200:
            st.error(f"Backend error: {response.status_code}")
            st.error(f"Error details: {response.text}")
            return None
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Connection error: {str(e)}")
        return None

st.title("AI Learning Path Creator")
st.write("Get personalized learning paths for any topics you want to master!")

with st.form("learning_path_form"):
    topics_input = st.text_area("Enter the topics you want to learn (one per line):")
    topics = [topic.strip() for topic in topics_input.split("\n") if topic.strip()]
    
    skill_level = st.select_slider(
        "Select your current skill level:",
        options=["Complete Beginner", "Beginner", "Intermediate", "Advanced", "Expert"]
    )
    
    time_frame = st.select_slider(
        "How much time can you dedicate?",
        options=["1 week", "2 weeks", "1 month", "3 months", "6 months", "1 year"]
    )
    
    simplification_level = st.slider(
        "How simplified would you like the content? (1: Technical, 5: Very Simple)",
        min_value=1,
        max_value=5,
        value=3
    )
    
    submitted = st.form_submit_button("Create Learning Path")

if submitted and topics:
    with st.spinner("Creating your personalized learning path..."):
        learning_path = create_learning_path(topics, skill_level, time_frame, simplification_level)
        
        if learning_path:
            st.header("Your Personalized Learning Path")
            
            if "overview" in learning_path:
                st.subheader("Overview")
                st.write(learning_path["overview"])
            
            if "prerequisites" in learning_path:
                st.subheader("Prerequisites")
                for prereq in learning_path["prerequisites"]:
                    st.write(f"- {prereq}")
            
            if "modules" in learning_path:
                st.subheader("Learning Modules")
                for i, module in enumerate(learning_path["modules"], 1):
                    with st.expander(f"Module {i}: {module['title']}"):
                        st.write(f"**Description:** {module['description']}")
                        st.write("\n**Learning Objectives:**")
                        for obj in module["learning_objectives"]:
                            st.write(f"- {obj}")
                            
                        st.write("\n**Resources:**")
                        for resource in module["resources"]:
                            st.write(f"- [{resource['title']}]({resource.get('url', '#')})")
                            st.write(f"  - Type: {resource['type']}")
                            st.write(f"  - Difficulty: {resource['difficulty']}")
                            st.write(f"  - Time: {resource['time_to_complete']}")
                        
                        st.write("\n**Exercises:**")
                        for exercise in module["exercises"]:
                            st.write(f"- {exercise}")
            
            if "milestones" in learning_path:
                st.subheader("Progress Milestones")
                for milestone in learning_path["milestones"]:
                    st.write(f"- {milestone}")
elif submitted:
    st.error("Please enter at least one topic to learn!")