def remove_constants(documents: list[str]) -> list[str]:
    """
    Removes useless constants from all documents.
    
    Examples: "experience", "skills", "education", etc. 
    """

    constants: list[str] = ["experience", "skill", "hobby", "education", "certification", "project", "contact", "summary", "objective", "achievement", "reference", "work experience", "internship", "volunteer", "award", "portfolio", "extracurricular activity", "language", "social media", "linkedin", "github", "email", "address", "phone number", "website", "career summary", "contact detail", "professional summary", "key skill", "professional experience", "educational background", "academic qualification", "training", "certification & training", "qualification", "higher education", "university degree", "college degree", "technical skill", "soft skill", "programming language", "project undertaken", "research", "conference attended", "lecture", "publication", "seminar", "online course", "course", "coursework", "academic project", "public speaking", "workshop", "leadership role", "volunteer work", "community involvement", "volunteer experience", "interest", "affiliation", "professional organization", "membership", "technical workshop", "online training", "internship", "student organization", "honor", "scholarship", "leadership experience", "teamwork", "professional network", "military service", "government service", "job responsibility", "career objective", "desired position", "current position", "previous role", "employer history", "employment history", "salary expectation", "relocation preference", "start date", "language known", "native language", "fluency", "spoken language", "communication skill", "collaborative skill", "analytical skill", "time management", "organizational skill", "attention to detail", "problem-solving skill", "leadership skill", "project management skill", "research skill", "presentation skill", "creative skill", "critical thinking skill", "adaptability", "work style", "work ethic", "personality trait", "characteristic", "marital status", "age", "date of birth", "nationality", "citizenship", "passport number", "visa status", "permanent address", "current address"]

    for constant in constants:
        for i, document in enumerate(documents):
            documents[i] = document.replace(constant, "").strip()
        
    return documents
