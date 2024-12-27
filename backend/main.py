from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from crewai import Crew
from .models.schemas import LearningPathRequest, LearningPath
from .crew.agents import LearningPathAgents
from .crew.tasks import LearningPathTasks
import json
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Verify API key is set
if not os.getenv("OPENAI_API_KEY"):
    raise ValueError("OPENAI_API_KEY not found in environment variables")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def clean_and_parse_json(result):
    """Clean and parse the crew result into valid JSON"""
    try:
        # If result is CrewAI output, get raw_output
        if hasattr(result, 'raw_output'):
            result = result.raw_output
        
        # Convert to string if needed
        if not isinstance(result, str):
            result = str(result)
        
        # Clean the string
        result = result.strip()
        
        # If the response is wrapped in ```json ```, extract just the JSON
        if "```json" in result:
            result = result.split("```json")[1].split("```")[0]
        elif "```" in result:
            result = result.split("```")[1]
        
        # Parse JSON
        data = json.loads(result)
        return data
        
    except json.JSONDecodeError as e:
        print(f"JSON Parse Error: {e}")
        print(f"Raw Result: {result}")
        return create_default_response("Error parsing content")
    except Exception as e:
        print(f"General Error: {e}")
        print(f"Raw Result: {result}")
        return create_default_response(str(e))

def create_default_response(error_msg):
    """Create a default response structure"""
    return {
        "overview": "This is a basic introduction to your chosen topic.",
        "modules": [
            {
                "title": "Getting Started",
                "content": {
                    "introduction": "Let's begin learning about this topic.",
                    "sections": [
                        {
                            "title": "Basic Concepts",
                            "content": "Understanding the fundamentals...",
                            "examples": [
                                {
                                    "scenario": "Real-world example",
                                    "explanation": "How this applies..."
                                }
                            ]
                        }
                    ],
                    "summary": "Key points covered..."
                },
                "quiz": [
                    {
                        "question": "Test your understanding",
                        "options": ["A", "B", "C", "D"],
                        "correct_answer": "A",
                        "explanation": "This is why..."
                    }
                ]
            }
        ],
        "milestones": ["Complete basic concepts"]
    }

@app.post("/learning-path/")
async def create_learning_path(request: LearningPathRequest):
    try:
        # Initialize agents
        agents_manager = LearningPathAgents(request.simplification_level)
        agents = agents_manager.create_agents()
        
        # Create tasks
        tasks = LearningPathTasks.create_tasks(
            agents,
            request.topics,
            request.skill_level,
            request.time_frame
        )
        
        # Create and run the crew
        crew = Crew(
            agents=list(agents.values()),
            tasks=tasks,
            verbose=True
        )

        # Execute the crew's tasks
        result = crew.kickoff()
        
        # Process the result
        processed_result = clean_and_parse_json(result)
        
        return processed_result
        
    except Exception as e:
        print(f"Error in create_learning_path: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health_check():
    return {"status": "healthy"}