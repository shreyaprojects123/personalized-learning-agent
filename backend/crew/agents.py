from crewai import Agent
from langchain.tools import DuckDuckGoSearchRun
from textwrap import dedent

search_tool = DuckDuckGoSearchRun()

class LearningPathAgents:
    def __init__(self, simplification_level: int):
        self.simplification_level = simplification_level
        
    def create_agents(self):
        curriculum_designer = Agent(
            role='Curriculum Designer',
            goal=dedent(f"""Design learning paths that are well-structured and 
            simplified to level {self.simplification_level} out of 5. Focus on making 
            concepts as accessible as possible while maintaining accuracy."""),
            backstory=dedent("""You are an expert in breaking down complex topics 
            into simple, digestible pieces. You excel at creating curricula for 
            learners of all levels."""),
            tools=[search_tool],
            verbose=True
        )

        resource_curator = Agent(
            role='Resource Curator',
            goal=dedent(f"""Find learning resources that match simplification 
            level {self.simplification_level}. Focus on beginner-friendly content 
            and practical examples."""),
            backstory=dedent("""You are a skilled curator who excels at finding 
            resources that make complex topics easy to understand."""),
            tools=[search_tool],
            verbose=True
        )

        exercise_creator = Agent(
            role='Exercise Creator',
            goal=dedent(f"""Create exercises that reinforce learning at 
            simplification level {self.simplification_level}. Focus on hands-on 
            practice with clear instructions."""),
            backstory=dedent("""You specialize in creating exercises that help 
            beginners gain confidence through practical application."""),
            tools=[search_tool],
            verbose=True
        )

        progress_tracker = Agent(
            role='Progress Tracker',
            goal=dedent("""Design clear milestones and simple progress tracking 
            methods that encourage learners."""),
            backstory=dedent("""You are an expert in creating encouraging and 
            clear progress tracking systems that keep learners motivated."""),
            tools=[search_tool],
            verbose=True
        )

        return {
            'curriculum_designer': curriculum_designer,
            'resource_curator': resource_curator,
            'exercise_creator': exercise_creator,
            'progress_tracker': progress_tracker
        }