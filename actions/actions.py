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
            #Câu hỏi về giá khi cung cấp thông tin tên của sản phẩm 
class action_aws_price(Action):
    def name(self) -> Text:
        return "action_aws_price"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        product_name = tracker.get_slot("product")

        # Logic để truy vấn và lấy giá sản phẩm từ file JSON
        with open('D:/abc/products.json', encoding="utf-8") as f:
            products = json.load(f)['products']

            n = len(products)
            check = False
            for i in range(n):
                if product_name in products[i]['product_name']:
                    check = True
                    break
                else: 
                    check = False
                
            if check == True:
                price = products[i]['price']
                dispatcher.utter_message(f"Giá của sản phẩm {product_name} là {price}")
            else:
                dispatcher.utter_message(f"Không tìm thấy thông tin về sản phẩm {product_name}")

            return[]

#Câu hỏi trả về chất liệu của sản phẩm
class action_aws_material(Action):
    def name(self) -> Text:
        return "action_aws_material"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        product_name = tracker.get_slot("product")

        # Logic để truy vấn và lấy chất liệu sản phẩm từ file JSON
        with open('D:/abc/products.json', encoding="utf-8") as f:
            products = json.load(f)['products']

            n = len(products)
            check = False
            for i in range(n):
                if product_name in products[i]['product_name']:
                    check = True
                    break
                else: 
                    check = False
                
            if check == True:
                material = products[i]['material']
                dispatcher.utter_message(f"Dạ thưa quý khách,{product_name} được làm bằng chất liệu {material}")
            else:
                dispatcher.utter_message(f"Xin lỗi quý khách, chúng tôi không tìm thấy thông tin về sản phẩm {product_name}")

            return[]

#Câu hỏi trả về list các màu của sản phẩm

class action_aws_color_list(Action):
    def name(self) -> Text:
        return "action_aws_color_list"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        product_name = tracker.get_slot("product")

        # Logic để truy vấn và lấy chất liệu sản phẩm từ file JSON
        with open('D:/abc/products.json', encoding="utf-8") as f:
            products = json.load(f)['products']

            n = len(products)
            check = False
            for i in range(n):
                if product_name in products[i]['product_name']:
                    check = True
                    break
                else: 
                    check = False
                
            if check == True:
                color = products[i]['color']
                dispatcher.utter_message(f"Đối với {product_name} thì Nana shop hiện tại có các màu: {color} . Quý khách có thể thoải mái lựa chọn theo sở thích của mình ")
            else:
                dispatcher.utter_message(f"Xin lỗi quý khách, chúng tôi không tìm thấy thông tin về sản phẩm {product_name}")

            return[]


#Câu hỏi yeess-no về color
class action_aws_color_yn(Action):
    def name(self) -> Text:
        return "action_aws_color_yn"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        product_name = tracker.get_slot("product")
        color = tracker.get_slot("colors")

        # Logic để truy vấn và lấy chất liệu sản phẩm từ file JSON
        with open('D:/abc/products.json', encoding="utf-8") as f:
            products = json.load(f)['products']

            n = len(products)
            check = 0
            for i in range(n):
                if product_name in products[i]['product_name']:
                    if color in products[i]['color'][i]:
                        check = 1
                        break
                    else:  
                        check = 2
                else: 
                    check = 0
                
            if check == 1:
                dispatcher.utter_message(f"Đối với {product_name} thì Nana shop hiện tại có màu {color} ạ")
            elif check == 2:
                dispatcher.utter_message(f"Đối với {product_name} thì Nana shop hiện tại không có màu {color} ạ. Quý khách có thể tham khảo những màu khác ạ")
            else:
                dispatcher.utter_message(f"Xin lỗi quý khách, chúng tôi không tìm thấy thông tin về sản phẩm {product_name}")

            return[]


