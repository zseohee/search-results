PREDEFINED_KEYWORDS = [
    "blind",
    "deaf",
    "physical disability",
    "intellectual disability",
    "autism spectrum disorder",
    "welfare",
    "financial aid",
    "disability",
    "benefits",
    "SSI",
    "grants",
    "accessibility",
    "universal design",
    "assistive technology",
    "accessible design",
    "screen reader",
    "audiodescription",
    "braille",
    "ASL",
    "sign language",
    "hearing aids",
    "prosthesis",
    "mental health awareness",
    "inclusion",
    "disability rights",
    "emotional intelligence",
    "community support",
    "smart devices",
    "Alexa",
    "Google Assistant",
    "Siri",
    "voice control",
    "captioning",
    "deaf culture",
]

def extract_tags(text: str) -> list:
    text = text.lower()
    return [keyword for keyword in PREDEFINED_KEYWORDS if keyword.lower() in text]

def classify_category(text: str) -> str:
    text = text.lower()

    if any(keyword in text for keyword in ["job", "hiring", "employment", "apply", "position", "opportunity"]):
        return "job"
    if any(keyword in text for keyword in ["event", "conference", "workshop", "webinar", "campaign", "forum"]):
        return "event"
    if any(
        keyword in text
        for keyword in [
            "benefit",
            "welfare",
            "empower",
            "financial aid",
            "grant",
            "ssi",
            "policy",
            "registration",
            "support",
        ]
    ):
        return "welfare"
    return "other"
