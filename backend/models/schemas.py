from pydantic import BaseModel
from typing import List, Optional

class LearningPathRequest(BaseModel):
    topics: List[str]
    skill_level: str
    time_frame: str
    simplification_level: int  # 1-5, where 5 is most simplified/dumbed down

class Resource(BaseModel):
    type: str
    title: str
    url: Optional[str]
    description: str
    difficulty: str
    time_to_complete: str

class Module(BaseModel):
    title: str
    description: str
    learning_objectives: List[str]
    resources: List[Resource]
    exercises: List[str]
    estimated_time: str

class LearningPath(BaseModel):
    topics: List[str]
    skill_level: str
    time_frame: str
    overview: str
    prerequisites: List[str]
    modules: List[Module]
    milestones: List[str]