import os
from linebot import LineBotApi
from linebot.models import TextSendMessage

from transitions.extensions import GraphMachine

from utils import send_text_message
from api import get_metadata, get_coin_price


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_menu(self, event):
        text = event.message.text
        return text.lower() == "MENU"

    def is_going_to_coins(self, event):
        text = event.message.text
        return text.lower() == "Coins"

    def is_going_to_price(self, event):
        text = event.message.text
        return text.lower() == "Show Price"

    def is_going_to_metadata(self, event):
        text = event.message.text
        return text.lower() == "Show Metadata"

    def is_going_to_fsm_graph(self, event):
        text = event.message.text
        return text.lower() == "Show FSM Graph"

    def is_going_to_introduction(self, event):
        text = event.message.text
        return text.lower() == "Bot Introduction"

    def is_going_to_cancel(self, event):
        text = event.message.text
        return text.lower() == "Cancel"

    def on_enter_menu(self, event):
        reply_token = event.reply_token
        line_bot_api = LineBotApi(os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None))
        line_bot_api.reply_message(reply_token, TextSendMessage(text="Menu"))
        send_text_message(reply_token, "on_enter_menu")

    def on_enter_coins(self, event):
        reply_token = event.reply_token
        send_text_message(reply_token, "on_enter_coins")

    def on_enter_price(self, event):
        reply_token = event.reply_token
        send_text_message(reply_token, "on_enter_price")

    def on_enter_metadata(self, event):
        reply_token = event.reply_token
        send_text_message(reply_token, "on_enter_metadata")

    def on_enter_fsm_graph(self, event):
        reply_token = event.reply_token
        send_text_message(reply_token, "on_enter_fsm_graph")
        self.go_back()

    def on_enter_introduction(self, event):
        reply_token = event.reply_token
        send_text_message(reply_token, "on_enter_metadata")
        self.go_back()

    def on_enter_cancel(self, event):
        reply_token = event.reply_token
        send_text_message(reply_token, "on_enter_cancel")
        self.go_back()
