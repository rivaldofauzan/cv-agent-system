from typing import TypedDict, List, Dict, Optional
from pydantic import BaseModel, Field

# Pydantic models for structured data extraction from the CV
# These models ensure that the data passed between agents is well-defined and validated.

class Experience(BaseModel):
    role: str = Field(..., description="The job title or role.")
    company: str = Field(..., description="The name of the company.")
    duration: str = Field(..., description="The duration of the employment (e.g., '2021 - Present').")
    description: List[str] = Field(..., description="A list of responsibilities and achievements.")

class Education(BaseModel):
    degree: str = Field(..., description="The degree obtained.")
    institution: str = Field(..., description="The name of the institution.")
    duration: str = Field(..., description="The duration of study.")

class StructuredCV(BaseModel):
    """The structured, machine-readable format of the CV."""
    name: str = Field(..., description="Candidate's full name.")
    contact_info: Dict[str, str] = Field(..., description="Contact information like email and phone.")
    summary: str = Field(..., description="The professional summary or objective.")
    experience: List[Experience] = Field(..., description="A list of professional experiences.")
    education: List[Education] = Field(..., description="A list of educational qualifications.")
    skills: Dict[str, List[str]] = Field(..., description="A dictionary of categorized skills (e.g., 'Programming Languages').")

# This TypedDict defines the state of our LangGraph.
# It's the central object that is passed around and modified by the agents.

class AgentState(TypedDict):
    """
    Represents the state of our multi-agent workflow.
    """
    cv_text: str
    target_role: str
    structured_cv: Optional[StructuredCV]
    skill_analysis: Optional[Dict[str, List[str]]]
    market_demands: Optional[str]
    final_report: Optional[str]

