ROLES = {
    "DATA_ENGINEER": {
        "priority": 1,
        "match_type": "phrase",
        "phrases": ["data engineer", "analytics engineer"],
        "forbid": ["scientist"],
    },
    "DATA_ANALYST": {
        "priority": 2,
        "match_type": "phrase",
        "phrases": ["data analyst", "business analyst"],
        "forbid": ["data engineer", "scientist"],
    },
    "DATA_SCIENTIST": {
        "priority": 3,
        "match_type": "phrase",
        "phrases": ["data scientist", "applied scientist"],
    },
    "ML_ENGINEER": {
        "priority": 4,
        "match_type": "phrase",
        "phrases": ["machine learning engineer", "ml engineer"],
    },
    "AI_ENGINEER": {
        "priority": 5,
        "match_type": "phrase",
        "phrases": ["artificial intelligence engineer", "ai engineer"],
    },
    "PYTHON_SOFTWARE_ENGINEER": {
        "priority": 6,
        "match_type": "keywords",
        "required_keywords": ["python"],
        "optional_keywords": ["developer", "engineer", "backend"],
        "min_matches": 2,
        "forbid": ["data", "scientist", "ml", "ai"],
    },
}


def normalize_role(title: str) -> str | None:
    """
    Normalize a raw job title into a single canonical role.
    Returns None if the title does not match any known role.
    """

    if not title:
        return None

    normalized_title = title.lower().strip()

    roles_by_priority = sorted(
        ROLES.items(), key=lambda item: item[1]["priority"]
    )

    for role, config in roles_by_priority:

        if any(word in normalized_title for word in config.get("forbid", [])):
            continue

        if config["match_type"] == "phrase":
            if any(phrase in normalized_title for phrase in config.get("phrases", [])):
                return role

        elif config["match_type"] == "keywords":
            keywords = (
                config.get("required_keywords", [])
                + config.get("optional_keywords", [])
            )

            hits = sum(1 for kw in keywords if kw in normalized_title)

            if hits >= config.get("min_matches", 0):
                return role

    return None