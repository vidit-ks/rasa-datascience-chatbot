from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
import re


class ActionListUpcomingBatches(Action):
    def name(self) -> Text:
        return "action_list_upcoming_batches"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        batches = ["📅 July 15, 2025", "📅 September 1, 2025", "📅 November 10, 2025"]
        batch_list = "\n".join(f"- {date}" for date in batches)
        dispatcher.utter_message(
            text=f"Here are our upcoming batch start dates:\n{batch_list}")
        return []


class ActionProvideCourseFee(Action):
    def name(self) -> Text:
        return "action_provide_course_fee"

    def run(self, dispatcher, tracker, domain):
        level = tracker.get_slot("course_level")

        if not level:
            dispatcher.utter_message(text="Please specify whether you're interested in beginner, intermediate, or advanced level.")
            return []

        fee_lookup = {
            "beginner": "₹30,000",
            "intermediate": "₹40,000",
            "advanced": "₹50,000"
        }

        fee = fee_lookup.get(level.lower(), "₹50,000")
        dispatcher.utter_message(text=f"The fee for our {level.title()} level course is {fee}. Scholarships and EMI options are also available.")
        return []


class ActionShowCourseTopics(Action):
    def name(self) -> Text:
        return "action_show_course_topics"

    def run(self, dispatcher, tracker, domain):
        topics = [
            "📌 Python Programming",
            "📊 Statistics & Data Analysis",
            "🤖 Machine Learning Algorithms",
            "🧠 Deep Learning (CNNs, RNNs)",
            "🗣️ Natural Language Processing",
            "📂 Real-World Capstone Projects"
        ]
        dispatcher.utter_message(
            text="📚 Our curriculum includes:\n" + "\n".join(topics))
        return []


class ActionScholarshipInfo(Action):
    def name(self) -> Text:
        return "action_scholarship_info"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(text=(
            "🎓 **Scholarships & Offers**\n"
            "- Early Bird: 10% off\n"
            "- Merit Scholarship: Up to 25% for top candidates\n"
            "- Group Discount: For 3+ enrollments\n"
            "- EMI Plans also available for flexible payments."
        ))
        return []


class ActionCourseMode(Action):
    def name(self) -> Text:
        return "action_course_mode"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        mode = tracker.get_slot("mode")

        if mode:
            dispatcher.utter_message(text=f"✅ Yes, we offer **{mode.title()}** classes with flexible and comfortable timings!")
        else:
            dispatcher.utter_message(text=(
                "🖥️ Course Delivery Modes:\n"
                "- Online (Live & Recorded)\n"
                "- Offline (Delhi & Mumbai campuses)\n"
                "- Hybrid (Mix of both)"
            ))

        return []


class ActionCoursePractice(Action):
    def name(self) -> Text:
        return "action_course_practice"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(text=(
            "🧪 Our program emphasizes hands-on experience:\n"
            "- 10+ coding assignments\n"
            "- 3 major capstone projects\n"
            "- Case studies and code reviews"
        ))
        return []


class ActionCourseRecommendationByBudget(Action):
    def name(self) -> Text:
        return "action_course_recommendation_by_budget"

    def run(self, dispatcher, tracker, domain):
        budget = tracker.get_slot("budget")
        if budget:
            match = re.search(r"(\d{2,6})", budget.replace(",", ""))
            if match:
                budget_value = int(match.group(1))
                if budget_value <= 30000:
                    recommendation = "🎯 Certificate Program (3 months) – practical + affordable!"
                elif budget_value <= 50000:
                    recommendation = "🎯 Intermediate Track (4 months) – great value and content-rich."
                else:
                    recommendation = "🌟 Advanced Program (6 months) – includes job prep & career support."

                dispatcher.utter_message(text=f"Based on your budget, we recommend:\n{recommendation}")
            else:
                dispatcher.utter_message(text="⚠️ I couldn’t read the amount properly. Please enter like ₹30000.")
        else:
            dispatcher.utter_message(text="Could you please tell me your budget so I can recommend the best fit?")
        return []


class ActionProvideAdmissionLink(Action):
    def name(self) -> Text:
        return "action_provide_admission_link"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(text="📝 Ready to enroll? Fill out the form here 👉 [Apply Now](https://example.com/apply)")
        return []


class ActionCourseDuration(Action):
    def name(self) -> Text:
        return "action_course_duration"

    def run(self, dispatcher, tracker, domain):
        course = tracker.get_slot("course") or "Data Science"

        durations = {
            "data science": "12 weeks",
            "ds": "12 weeks",
            "ai": "14 weeks",
            "ml": "10 weeks"
        }

        duration = durations.get(course.lower(), "12 weeks")
        dispatcher.utter_message(
            text=f"🕒 The *{course.title()}* course runs for **{duration}**.")
        return [SlotSet("course", course), SlotSet("duration", duration)]
