# actions.py

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

# Example action: returning upcoming batch dates
class ActionListUpcomingBatches(Action):

    def name(self) -> Text:
        return "action_list_upcoming_batches"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        batches = ["July 15, 2025", "September 1, 2025", "November 10, 2025"]
        batch_list = ", ".join(batches)
        dispatcher.utter_message(text=f"The upcoming Data Science batches start on: {batch_list}.")
        return []

# Example action: returning fee structure based on course level
class ActionProvideCourseFee(Action):

    def name(self) -> Text:
        return "action_provide_course_fee"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        course_level = tracker.get_slot("course_level")
        if course_level:
            course_level = course_level.lower()
            fees = {
                "beginner": "₹30,000 for 3 months",
                "intermediate": "₹45,000 for 4 months",
                "advanced": "₹60,000 for 6 months"
            }
            fee_info = fees.get(course_level, "₹45,000 as standard fee")
            dispatcher.utter_message(text=f"The fee for {course_level} level is {fee_info}.")
        else:
            dispatcher.utter_message(text="Please specify whether you're interested in beginner, intermediate, or advanced level.")
        
        return []

# Example action: return course curriculum/topics
class ActionShowCourseTopics(Action):

    def name(self) -> Text:
        return "action_show_course_topics"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        topics = [
            "Python basics",
            "Statistics for Data Science",
            "Machine Learning algorithms",
            "Deep Learning (Neural Networks, CNNs)",
            "NLP (Natural Language Processing)",
            "Project Work with real datasets"
        ]
        topics_list = "\n- " + "\n- ".join(topics)
        dispatcher.utter_message(text=f"Our course covers the following topics:\n{topics_list}")
        return []

# Action: return scholarship info
class ActionScholarshipInfo(Action):

    def name(self) -> Text:
        return "action_scholarship_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Yes! We offer:\n- Early bird discounts (10%)\n- Merit-based scholarships (up to 25%)\n- Need-based support (on application)")
        return []

# Action: respond to mode query
class ActionCourseMode(Action):

    def name(self) -> Text:
        return "action_course_mode"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Our course is available in Online, Offline (Delhi & Mumbai), and Hybrid modes. Which one would you prefer?")
        return []

# Action: respond to practice/projects query
class ActionCoursePractice(Action):

    def name(self) -> Text:
        return "action_course_practice"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Yes! The course includes:\n- Weekly coding assignments\n- 3 real-world capstone projects\n- 5 mini-projects across modules")
        return []

# Action: budget-based recommendation
class ActionCourseRecommendationByBudget(Action):

    def name(self) -> Text:
        return "action_course_recommendation_by_budget"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        budget = tracker.get_slot("budget")
        if budget:
            try:
                budget_value = int(budget.replace("₹", "").replace(",", "").strip())
                if budget_value <= 30000:
                    dispatcher.utter_message(text="With that budget, we recommend our Certificate Program (3 months).")
                elif 30000 < budget_value <= 50000:
                    dispatcher.utter_message(text="You can go for our Intermediate Data Science Track (4 months).")
                else:
                    dispatcher.utter_message(text="Great! You qualify for our Advanced Program with job assistance (6 months).")
            except:
                dispatcher.utter_message(text="Couldn't process your budget. Please enter an amount in ₹.")
        else:
            dispatcher.utter_message(text="Can you share your budget so I can suggest the best course?")
        return []


class ActionProvideAdmissionLink(Action):
    def name(self) -> Text:
        return "action_provide_admission_link"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        dispatcher.utter_message(text="Here is the admission form link: https://example.com/apply")
        return []
