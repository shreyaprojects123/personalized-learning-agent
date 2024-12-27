from crewai import Task
from textwrap import dedent

class LearningPathTasks:
    @staticmethod
    def calculate_days(time_frame: str) -> int:
        """Convert time frame to number of days"""
        time_mapping = {
            "1 week": 7,
            "2 weeks": 14,
            "1 month": 30,
            "3 months": 90,
            "6 months": 180,
            "1 year": 365
        }
        return time_mapping.get(time_frame, 7)  # Default to 7 days if time frame not found

    @staticmethod
    def create_tasks(agents, topics, skill_level, time_frame):
        # Calculate number of days/modules
        num_days = LearningPathTasks.calculate_days(time_frame)
        
        design_curriculum = Task(
            description=dedent(f"""
                Create a {num_days}-day learning path for: {', '.join(topics)}
                Student level: {skill_level}
                
                IMPORTANT: Create EXACTLY {num_days} modules, one for each day.
                Each day's module should be completable within 1-2 hours of focused learning.
                
                Format your response EXACTLY as this JSON structure:
                {{
                    "overview": "A detailed overview of the complete {num_days}-day learning path",
                    "modules": [
                        {{
                            "title": "Day X: Clear module title",
                            "content": {{
                                "introduction": "Today's learning objectives and overview",
                                "sections": [
                                    {{
                                        "title": "Section Title",
                                        "content": "Detailed textbook-style explanation",
                                        "examples": [
                                            {{
                                                "scenario": "Example description",
                                                "explanation": "Example explanation"
                                            }}
                                        ]
                                    }}
                                ],
                                "summary": "Today's key takeaways"
                            }},
                            "quiz": [
                                {{
                                    "question": "Practice question",
                                    "options": ["A", "B", "C", "D"],
                                    "correct_answer": "A",
                                    "explanation": "Why this is correct"
                                }}
                            ]
                        }}
                    ],
                    "milestones": [
                        "Day 1: First milestone",
                        "Day 2: Second milestone",
                        ...and so on for {num_days} days
                    ]
                }}
                
                Make sure to:
                1. Create exactly {num_days} modules
                2. Title each module as 'Day X: [Topic]'
                3. Make each day's content manageable within 1-2 hours
                4. Progress logically from basic to advanced concepts
                5. Include daily milestones
                
                REMEMBER: Return ONLY the JSON structure, no other text."""),
            agent=agents['curriculum_designer'],
            expected_output=f"A valid JSON string containing a {num_days}-day learning path"
        )

        return [design_curriculum]