from pydantic import BaseModel, Field, ConfigDict
from typing import List, Optional

class File(BaseModel):
    path: str = Field(description="The path to the file to be created or modified")
    purpose: str = Field(description="The purpose of the file, e.g. 'main application logic', 'data processing module', etc.")

class Plan(BaseModel):
    name: str = Field(description="The name of app to be built")
    description: str = Field(description="A oneline description of the app to be built, e.g. 'A web application for managing personal finances'")
    techstack: str = Field(description="The tech stack to be used for the app, e.g. 'python', 'javascript', 'react', 'flask', etc.")
    features: List[str] = Field(description="A list of features that the app should have, e.g. 'user authentication', 'data visualization', etc.")
    files: List[File] = Field(description="A list of files to be created, each with a 'path' and 'purpose'")
    
class ImplementationTask(BaseModel):
    filepath: str = Field(description="The path to the file to be modified")
    description: str = Field(description="A detailed description of the task to be performed on the file, e.g. 'add user authentication', 'implement data processing logic', etc.")
    
class ImplementationPlan(BaseModel):
    implementation_steps: List[ImplementationTask] = Field(description="A list of steps to be taken to implement the task")
    model_config = ConfigDict(extra="allow")
    
    
class Implementation(BaseModel):
    filepath: str = Field(description="The path to the file that is currently being created or modified")
    content: str = Field(description='content of the file.')
    
class CoderState(BaseModel):
    task_plan: ImplementationPlan = Field(description="The current state of the implementation plan, including which tasks have been completed and which are still pending.")
    current_step_index: int = Field(0, description="The index of the current implementation step being worked on.")
    content: Optional[str] = Field(None, description="The content of the file currently being edited or created")