"""
Configuration file for the Hotel Information Agent project.
This file documents the main setup and capabilities of the agent.
"""

PROJECT_NAME = "Hotel Information Agent"

MODEL_NAME = "gpt-5-mini"

PLATFORM = "Azure AI Foundry"

DESCRIPTION = (
    "AI-powered hotel information assistant designed to provide "
    "grounded and professional responses to hotel guest inquiries."
)

CORE_FEATURES = [
    "Grounded hotel information responses",
    "Prompt-engineered system instructions",
    "Knowledge-based response generation",
    "Hallucination prevention",
    "Hospitality-focused conversational support",
    "Guest assistance workflows",
]

SUPPORTED_TOPICS = [
    "Hotel amenities",
    "Check-in and check-out",
    "Parking",
    "Dining",
    "Wi-Fi",
    "Accessibility",
    "Transportation",
    "Pet policies",
    "Reservation policies",
    "Guest support",
]

STARTER_PROMPTS = [
    "What amenities does the hotel offer?",
    "What time is check-in and check-out?",
    "Does the hotel provide airport transportation or parking?",
]

KNOWLEDGE_SOURCE = "General Hotel Information Knowledge Base"
