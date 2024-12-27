from crewai import Agent
from textwrap import dedent

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
            verbose=True
        )

        return {
            'curriculum_designer': curriculum_designer
        }