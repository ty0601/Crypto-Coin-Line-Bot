import os
import message_json
from linebot import LineBotApi
from linebot.models import TextSendMessage, FlexSendMessage
from transitions.extensions import GraphMachine
from utils import send_text_message, send_image_url
from api import get_coin_price, get_coin_metadata


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_menu(self, event):
        text = event.message.text
        return text.lower() == "menu"

    def is_going_to_coins(self, event):
        text = event.message.text
        return text.lower() == "coins"

    def is_going_to_price(self, event):
        text = event.message.text
        coin = get_coin_price(text)
        return coin != []

    def is_going_to_metadata(self, event):
        text = event.message.text
        coin = get_coin_metadata(text)
        return coin != []

    def is_going_to_fsm_graph(self, event):
        text = event.message.text
        return text.lower() == "show fsm graph"

    def is_going_to_introduction(self, event):
        text = event.message.text
        return text.lower() == "show introduction"

    def is_going_to_cancel(self, event):
        text = event.message.text
        return text.lower() == "cancel"

    def on_enter_menu(self, event):
        reply_token = event.reply_token
        reply_message = FlexSendMessage("open menu", message_json.main_menu)
        line_bot_api = LineBotApi(os.getenv('LINE_CHANNEL_ACCESS_TOKEN'))
        line_bot_api.reply_message(reply_token, reply_message)

    def on_enter_coins(self, event):
        reply_token = event.reply_token
        reply_message = FlexSendMessage("open menu", message_json.coin_menu)
        line_bot_api = LineBotApi(os.getenv('LINE_CHANNEL_ACCESS_TOKEN'))
        line_bot_api.reply_message(reply_token, reply_message)

    def on_enter_price(self, event):
        reply_token = event.reply_token
        send_text_message(reply_token, "on_enter_price")

    def on_enter_metadata(self, event):
        reply_token = event.reply_token
        send_text_message(reply_token, "on_enter_metadata")

    def on_enter_fsm_graph(self, event):
        reply_token = event.reply_token
        send_image_url(reply_token,
                       'https://raw.githubusercontent.com/ty0601/LINE-BOT/master/img/show-fsm.png?token=ARDPLX3VSVVJ7FTCNPRBXFDB2CW54')
        self.go_back()

    def on_enter_introduction(self, event):
        reply_token = event.reply_token
        reply_message = FlexSendMessage("open menu", message_json.introduction)
        line_bot_api = LineBotApi(os.getenv('LINE_CHANNEL_ACCESS_TOKEN'))
        line_bot_api.reply_message(reply_token, reply_message)

    def on_enter_cancel(self, event):
        reply_token = event.reply_token
        send_text_message(reply_token, "on_enter_cancel")
        self.go_back()
