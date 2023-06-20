# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import json

class action_aws_price(Action):
    def name(self) -> Text:
        return "action_aws_price"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        product_name = tracker.get_slot("product")

        # Logic để truy vấn và lấy giá sản phẩm từ file JSON
        with open('products.json', 'r') as f:
            products = json.load(f)
            if product_name in products:
                price = products[product_name][price]
                dispatcher.utter_message(f"Giá trị của sản phẩm {product_name} là {price}")
            else:
                dispatcher.utter_message(f"Không tìm thấy thông tin về sản phẩm {product_name}")

            return []






