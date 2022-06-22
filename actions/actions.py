
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

from services.normalization import text_to_date, text_to_coordinate
from services.weather import get_text_weather_date


class ActionWeatherFormSubmit(Action):
    def name(self) -> Text:
        return "action_weather_form_submit"

    def run(
        self,
        dispatcher: "CollectingDispatcher",
        tracker: Tracker,
        domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:

        city = tracker.get_slot("address")
        date_text = tracker.get_slot("date-time")
        date_object = text_to_date(date_text)

        if not date_object:
            msg = f"Not support for weather query for {city}, {date_text}"
            dispatcher.utter_message(msg)
        else:
            dispatcher.utter_message(template="utter_working_on_it")

            try:
                lat, lon = text_to_coordinate(city)
                weather_data = get_text_weather_date(lat, lon, date_object, date_text, city)

            except Exception as e:
                exec_msg = str(e)
                dispatcher.utter_message(exec_msg)

            else:
                dispatcher.utter_message(weather_data)

        return []
