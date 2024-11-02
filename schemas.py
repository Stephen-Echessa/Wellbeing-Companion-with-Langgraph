from pydantic import BaseModel, Field
from typing import List, TypedDict
from langgraph.graph import MessagesState


# This agent captures key details about the client’s emotional state and issues, providing feedback to guide 
class ActiveListener(BaseModel):
    key_issues: List[str] = Field(
        description='List of key concerns expressed by the client during the session.'
    )
    root_cause: str = Field(
        description='Identified root cause of the client issue, or "None" if the root cause is still unclear.'
    )
    check_online_medical_citations: bool = Field(
        description="Boolean flag indicating if an external search is necessary for complex or health-related issues that require expert-backed information."
    )


# This agent offers expert recommendations based on the session's analysis, especially for health-related cases.
class HealthAdvisor(BaseModel):
    condition: str = Field(
        description="Client's primary health related-concern"
    )
    solutions: List[str] = Field(
        description="A list of recommended solutions or strategies tailored to assist the client with health-related concerns. Each solution is crafted based on a thorough analysis of the session's content."
    )


class AssistantState(MessagesState):
    listener_notes: dict
    expert_solutions: dict
    summary: str
