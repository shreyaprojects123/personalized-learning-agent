from pydantic import BaseModel
from typing import List, Optional

class LearningPathRequest(BaseModel):
    topics: List[str]
    skill_level: str
    time_frame: str
    simplification_level: int

class Resource(BaseModel):
    type: str
    title: str
    description: str
    difficulty: str
    time_to_complete: str
    url: Optional[str] = None

class Module(BaseModel):
    title: str
    description: str
    learning_objectives: List[str]
    resources: List[Resource]
    exercises: List[str]

class LearningPath(BaseModel):
    overview: str
    prerequisites: List[str]
    modules: List[Module]
    milestones: List[str]