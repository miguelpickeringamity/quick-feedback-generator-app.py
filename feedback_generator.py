# Feedback generator for observation notes
# This script processes free-form observation notes and generates structured feedback for teachers.

import re
from typing import Dict, List, Tuple

def get_categories() -> Dict[str, Dict[str, List[str]]]:
    """Return the categories and their associated keywords and reflection prompts."""
    return {
        "Clear Learning Objectives": {
            "keywords": ["objective", "goal", "learning target", "purpose", "expectation"],
            "reflection": "How often do you revisit and clarify the lesson objectives during the class?"
        },
        "Engagement": {
            "keywords": ["engage", "participation", "active", "hands-on", "collaborative", "group", "attention"],
            "reflection": "Which strategies help maintain high student engagement in your lessons?"
        },
        "Pacing": {
            "keywords": ["pace", "timing", "flow", "transition", "move on", "slow", "fast", "transition"],
            "reflection": "How do you decide when to adjust the pace of your teaching?"
        },
        "Differentiation": {
            "keywords": ["differentiate", "scaffold", "support", "challenge", "accommodate", "modify", "advanced"],
            "reflection": "What techniques do you use to meet diverse learning needs in your classroom?"
        },
        "Student Participation": {
            "keywords": ["student participation", "discussion", "questions", "answers", "voice", "input", "feedback"],
            "reflection": "How do you ensure all students have opportunities to contribute?"
        },
        "Teacher-Student Interaction": {
            "keywords": ["interaction", "question", "feedback", "monitor", "check-in", "rapport"],
            "reflection": "In what ways do you provide timely and constructive feedback during lessons?"
        },
        "Classroom Environment": {
            "keywords": ["environment", "classroom", "management", "tone", "organization", "seating", "positive", "supportive"],
            "reflection": "What adjustments could enhance the learning environment further?"
        },
        "Instructional Materials and Resources": {
            "keywords": ["materials", "resources", "technology", "tools", "handout", "digital", "textbook"],
            "reflection": "How effectively are instructional materials supporting your learning goals?"
        },
        "Assessment for Learning": {
            "keywords": ["assessment", "formative", "check for understanding", "feedback", "exit ticket", "monitor", "evaluate"],
            "reflection": "How do you use formative assessments to inform real-time instruction?"
        },
        "Student Understanding and Misunderstandings": {
            "keywords": ["understand", "misconception", "confusion", "clarify", "question", "explain"],
            "reflection": "How do you identify and address student misunderstandings during lessons?"
        }
    }


def categorize_sentences(text: str, categories: Dict[str, Dict[str, List[str]]]) -> Dict[str, List[str]]:
    """Categorize sentences based on keyword presence for each category."""
    # Normalize text
    sentences = [s.strip() for s in re.split(r'[.!?]\s*', text) if s.strip()]
    categorized: Dict[str, List[str]] = {cat: [] for cat in categories}
    # Lowercase sentences for matching
    for sentence in sentences:
        lower_sentence = sentence.lower()
        for category, info in categories.items():
            if any(keyword in lower_sentence for keyword in info["keywords"]):
                categorized[category].append(sentence)
    return categorized


def generate_feedback(notes: str) -> Tuple[Dict[str, Dict[str, List[str]]], Dict[str, Dict[str, str]]]:
    """Generate structured feedback from observation notes.

    Returns a tuple of (highlights, recommendations) dictionaries.
    Each dictionary maps category to a summary and reflection question.
    """
    categories = get_categories()
    categorized_sentences = categorize_sentences(notes, categories)
    highlights = {}
    recommendations = {}

    for category, sentences in categorized_sentences.items():
        if sentences:
            # Highlights: join sentences with context
            highlights[category] = {
                "summary": " ".join(sentences),
                "reflection": categories[category]["reflection"]
            }
            # Recommendations: provide general suggestion for improvement based on category
            # We could tailor this further with more logic; for now, generic coaching tips.
            if category == "Clear Learning Objectives":
                recommendation = "Explicitly state and reference learning objectives throughout the lesson so students know what they are working toward."
            elif category == "Engagement":
                recommendation = "Incorporate varied activities and interactive tasks to keep students actively involved in the learning process."
            elif category == "Pacing":
                recommendation = "Balance teacher instruction with student activity and monitor transitions for smoother flow."
            elif category == "Differentiation":
                recommendation = "Provide multiple pathways or scaffolds to support diverse learners and challenge advanced students."
            elif category == "Student Participation":
                recommendation = "Encourage participation through structured discussions and ensure all voices are heard."
            elif category == "Teacher-Student Interaction":
                recommendation = "Use questioning and feedback strategies that engage all students and guide learning."
            elif category == "Classroom Environment":
                recommendation = "Maintain an organized, positive, and supportive classroom setup conducive to learning."
            elif category == "Instructional Materials and Resources":
                recommendation = "Integrate materials and technologies that align with lesson goals and enhance learning."
            elif category == "Assessment for Learning":
                recommendation = "Use formative assessment techniques to check understanding and adjust instruction in real time."
            elif category == "Student Understanding and Misunderstandings":
                recommendation = "Promptly address misconceptions by clarifying and re-teaching concepts as needed."
            else:
                recommendation = "Consider targeted strategies to enhance this instructional area."
            recommendations[category] = {
                "suggestion": recommendation,
                "reflection": categories[category]["reflection"]
            }
    return highlights, recommendations

# Example usage (if run directly)
if __name__ == "__main__":
    example_notes = """
    The teacher began the lesson by stating the learning objective clearly on the board and explaining that students would identify key themes. Students appeared engaged during the discussion and participated actively in group work. However, transitions between activities were slightly rushed, and some advanced students seemed ready to move on sooner. The teacher provided immediate feedback when students were confused and used various instructional materials, including a short video and handouts. Formative assessment was evident through questioning and exit tickets.
    """
    highlights, recommendations = generate_feedback(example_notes)
    for cat in highlights:
        print(f"Category: {cat}")
        print(f"Highlights: {highlights[cat]['summary']}")
        print(f"Recommendation: {recommendations[cat]['suggestion']}")
        print(f"Reflection Prompt: {highlights[cat]['reflection']}")
        print("---")

