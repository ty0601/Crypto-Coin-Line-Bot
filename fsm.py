import os
import message_json
from linebot import LineBotApi
from linebot.models import TextSendMessage, FlexSendMessage
from transitions.extensions import GraphMachine
from utils import send_text_message, send_image_url
from api import get_coin_price


class TocMachine(GraphMachine):
    curr_coin = ''

    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_menu(self, event):
        text = event.message.text
        return text.lower() == "menu"

    def is_going_to_coin_menu(self, event):
        global  curr_coin
        curr_coin = event.message.text
        return True

    def is_going_to_coins(self, event):
        text = event.message.text
        return 'coins' in text

    def is_going_to_price(self, event):
        text = event.message.text
        return text.lower() == "price"

    def is_going_to_metadata(self, event):
        text = event.message.text
        return text.lower() == "metadata"

    def is_going_to_fsm_graph(self, event):
        text = event.message.text
        return text.lower() == "show fsm graph"

    def is_going_to_introduction(self, event):
        text = event.message.text
        return text.lower() == "show introduction"

    def is_going_to_cancel(self, event):
        text = event.message.text
        return text.lower() == "end operation"

    def on_enter_menu(self, event):
        reply_token = event.reply_token
        reply_message = FlexSendMessage("open menu", message_json.main_menu)
        line_bot_api = LineBotApi(os.getenv('LINE_CHANNEL_ACCESS_TOKEN'))
        line_bot_api.reply_message(reply_token, reply_message)

    def on_enter_coins(self, event):
        curr_coin = ''
        reply_token = event.reply_token
        reply_message = FlexSendMessage("choose coin", message_json.choose_coin)
        line_bot_api = LineBotApi(os.getenv('LINE_CHANNEL_ACCESS_TOKEN'))
        line_bot_api.reply_message(reply_token, reply_message)

    def on_enter_coin_menu(self, event):
        global curr_coin
        reply_token = event.reply_token
        reply_message = FlexSendMessage("coin menu", message_json.coin_menu)
        line_bot_api = LineBotApi(os.getenv('LINE_CHANNEL_ACCESS_TOKEN'))
        send_text_message(reply_token,curr_coin)
        line_bot_api.reply_message(reply_token, reply_message)

    def on_enter_price(self, event):
        global curr_coin
        reply_token = event.reply_token
        reply_message = FlexSendMessage("coin price", message_json.price_info)
        send_text_message(reply_token, curr_coin)
        coin_price = get_coin_price(curr_coin)
        # if not coin_price:
        #     send_text_message(reply_token, "Sorry, I can't find the coin")
        # else:
            # reply_message['body']['contents'][0]['contents'][0]['text'] = coin_price[0] + ' - (' + coin_price[1] + ')'
            # reply_message['body']['contents'][1]['contents'][1]['contents'][0]['text'] = '$ ' + coin_price[2]
            # reply_message['body']['contents'][2]['contents'][1]['contents'][0]['text'] = '$ ' + coin_price[3]
            # reply_message['body']['contents'][3]['contents'][1]['contents'][0]['text'] = '$ ' + coin_price[4]
            # reply_message['body']['contents'][4]['contents'][1]['contents'][0]['text'] = coin_price[4] + '%'
            # reply_message['body']['contents'][5]['contents'][1]['contents'][0]['text'] = coin_price[5] + '%'
            # reply_message['body']['contents'][6]['contents'][1]['contents'][0]['text'] = coin_price[6] + '%'
            # reply_message['body']['contents'][7]['contents'][1]['contents'][0]['text'] = coin_price[7] + '%'
        line_bot_api = LineBotApi(os.getenv('LINE_CHANNEL_ACCESS_TOKEN'))
        line_bot_api.reply_message(reply_token, reply_message)

    def on_enter_metadata(self, event):
        reply_token = event.reply_token
        send_text_message(reply_token, "on_enter_metadata")

    def on_enter_fsm_graph(self, event):
        reply_token = event.reply_token
        send_image_url(reply_token,
                       'https://github.com/ty0601/LINE-BOT/blob/master/img/show-fsm.png?raw=true')
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
