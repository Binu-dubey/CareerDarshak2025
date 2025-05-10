def get_personality_insights(personality_type):
    profiles = {
        "The Innovator": {
            "description": "Creative problem-solver who thinks outside the box",
            "key_strengths": [
                "Strong self-learning capabilities",
                "Excellent problem-solving skills",
                "Ability to work independently",
                "Methodical approach to tasks"
            ],
            "growth_areas": [
                "Team collaboration skills",
                "Communication in group settings",
                "Time management under pressure"
            ]
        },
        "The Collaborator": {
            "description": "Team-oriented individual who thrives in cooperative environments",
            "key_strengths": [
                "Excellent team player",
                "Empathetic and considerate",
                "Strong interpersonal skills",
                "Supportive and reliable"
            ],
            "growth_areas": [
                "Taking initiative independently",
                "Decision-making without consensus",
                "Technical upskilling"
            ]
        },
        "The Analyst": {
            "description": "Data-driven thinker who excels at analytical tasks and logical reasoning",
            "key_strengths": [
                "Strong logical and critical thinking",
                "Detail-oriented and thorough",
                "Excellent with numbers and data",
                "Efficient problem-solver"
            ],
            "growth_areas": [
                "Communication of complex ideas",
                "Flexibility in dynamic settings",
                "Collaborating with creative teams"
            ]
        },
        "The Communicator": {
            "description": "Expressive and articulate individual who enjoys engaging with others",
            "key_strengths": [
                "Excellent verbal and written communication",
                "Persuasive and confident",
                "Charismatic team presence",
                "Active listener"
            ],
            "growth_areas": [
                "Deep focus on technical tasks",
                "Time management",
                "Balancing talk with action"
            ]
        },
        "The Adaptable Achiever": {
            "description": "Flexible and driven person who excels under changing conditions",
            "key_strengths": [
                "Highly adaptable to new environments",
                "Quick learner",
                "Resilient and determined",
                "Thrives in fast-paced settings"
            ],
            "growth_areas": [
                "Consistency in structured environments",
                "Long-term planning",
                "Attention to detail"
            ]
        }
    }

    return profiles.get(personality_type, {
        "description": "Personality profile not available.",
        "key_strengths": [],
        "growth_areas": []
    })
