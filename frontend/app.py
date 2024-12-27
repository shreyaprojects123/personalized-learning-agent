import streamlit as st
import requests
from typing import List
import json

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

def display_module_content(module):
    """Display a single module's content in textbook style"""
    if 'content' in module:
        # Introduction
        if 'introduction' in module['content']:
            st.markdown("### Introduction")
            st.write(module['content']['introduction'])
            st.markdown("---")
        
        # Sections
        if 'sections' in module['content']:
            for section in module['content']['sections']:
                st.markdown(f"### {section['title']}")
                st.write(section['content'])
                
                # Examples for each section
                if 'examples' in section:
                    st.markdown("**📌 Examples:**")
                    for example in section['examples']:
                        st.markdown(f"**{example['scenario']}**")
                        st.markdown(f"_{example['explanation']}_")
                        st.markdown("---")
        
        # Summary
        if 'summary' in module['content']:
            st.markdown("### 📝 Summary")
            st.write(module['content']['summary'])
            st.markdown("---")
    
    # Quiz
    if 'quiz' in module:
        st.markdown("### 📋 Practice Quiz")
        for i, question in enumerate(module['quiz'], 1):
            st.markdown(f"**Question {i}:** {question['question']}")
            
            # Display options
            selected = st.radio(
                "Select your answer:",
                question['options'],
                key=f"quiz_{module['title']}_{i}"
            )
            
            # Check Answer button
            if st.button(f"Check Answer", key=f"check_{module['title']}_{i}"):
                if selected == question['options'][ord(question['correct_answer']) - ord('A')]:
                    st.success("✅ Correct!")
                else:
                    st.error("❌ Incorrect")
                    correct_option = question['options'][ord(question['correct_answer']) - ord('A')]
                    st.write(f"The correct answer is: {correct_option}")
                st.info(f"**Explanation:** {question['explanation']}")
            st.markdown("---")

def display_learning_path(learning_path):
    st.header("Your Personalized Learning Path")
    
    # Overview
    if "overview" in learning_path:
        st.subheader("Course Overview")
        st.write(learning_path["overview"])
        st.markdown("---")
    
    # Modules
    st.subheader("Learning Modules")
    for i, module in enumerate(learning_path.get("modules", []), 1):
        with st.expander(f"📚 Module {i}: {module['title']}"):
            display_module_content(module)
    
    # Milestones
    if "milestones" in learning_path:
        st.subheader("🎯 Progress Milestones")
        for milestone in learning_path["milestones"]:
            st.markdown(f"• {milestone}")

def main():
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
                display_learning_path(learning_path)
    elif submitted:
        st.error("Please enter at least one topic to learn!")

if __name__ == "__main__":
    main()