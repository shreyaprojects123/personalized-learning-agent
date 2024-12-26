from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from crewai import Crew, Process
from .models.schemas import LearningPathRequest, LearningPath
from .crew.agents import LearningPathAgents
from .crew.tasks import LearningPathTasks

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/learning-path/")
async def create_learning_path(request: LearningPathRequest):
    try:
        # Create a default response structure
        response = {
            "topics": request.topics,
            "skill_level": request.skill_level,
            "time_frame": request.time_frame,
            "overview": "Learning path overview will be generated here.",
            "prerequisites": ["Basic computer skills", "Internet connection"],
            "modules": [
                {
                    "title": "Getting Started",
                    "description": "Introduction to the topics",
                    "learning_objectives": ["Understand basic concepts"],
                    "resources": [
                        {
                            "type": "Article",
                            "title": "Introduction",
                            "description": "Getting started guide",
                            "difficulty": "Beginner",
                            "time_to_complete": "30 minutes"
                        }
                    ],
                    "exercises": ["Practice exercise 1"]
                }
            ],
            "milestones": ["Complete introduction module"]
        }
        
        return response
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Add a test endpoint
@app.get("/health")
async def health_check():
    return {"status": "healthy"}