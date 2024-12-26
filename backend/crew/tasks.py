from crewai import Task
from textwrap import dedent

class LearningPathTasks:
    @staticmethod
    def create_tasks(agents, topics, skill_level, time_frame):
        design_curriculum = Task(
            description=dedent(f"""
                Create a curriculum for topics: {', '.join(topics)}
                Skill level: {skill_level}
                Time frame: {time_frame}
                
                Include:
                1. Clear learning objectives
                2. Module breakdown
                3. Time estimates
                4. Prerequisites
                5. Expected outcomes
                
                Focus on making the content accessible and engaging.
            """),
            agent=agents['curriculum_designer']
        )

        curate_resources = Task(
            description=dedent("""
                Find beginner-friendly resources for each module:
                1. Video tutorials
                2. Interactive exercises
                3. Reading materials
                4. Practice projects
                
                Ensure resources are:
                - Easy to understand
                - Well-explained
                - Practical and hands-on
            """),
            agent=agents['resource_curator'],
            dependencies=[design_curriculum]
        )

        create_exercises = Task(
            description=dedent("""
                Create practical exercises that:
                1. Start very simple
                2. Build confidence gradually
                3. Include detailed explanations
                4. Provide immediate feedback opportunities
                5. Connect to real-world applications
            """),
            agent=agents['exercise_creator'],
            dependencies=[design_curriculum]
        )

        design_tracking = Task(
            description=dedent("""
                Create a progress tracking system with:
                1. Clear milestones
                2. Simple self-assessment tools
                3. Progress indicators
                4. Achievement markers
                5. Confidence-building checkpoints
            """),
            agent=agents['progress_tracker'],
            dependencies=[design_curriculum, create_exercises]
        )

        return [design_curriculum, curate_resources, create_exercises, design_tracking]