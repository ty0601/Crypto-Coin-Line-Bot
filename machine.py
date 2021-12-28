from fsm import TocMachine


def create_machine():
    machine = TocMachine(
        states=["user", "menu", "choose_coins", "coin_menu", "price", "metadata", "fsm_graph", "introduction",
                "cancel"],
        transitions=[
            {
                "trigger": "advance",
                "source": "user",
                "dest": "menu",
                "conditions": "is_going_to_menu",
            },
            {
                "trigger": "advance",
                "source": "menu",
                "dest": "menu",
                "conditions": "is_going_to_menu",
            },
            {
                "trigger": "advance",
                "source": "menu",
                "dest": "choose_coins",
                "conditions": "is_going_to_choose_coins",
            },
            {
                "trigger": "advance",
                "source": "choose_coins",
                "dest": "coin_menu",
                "conditions": "is_going_to_coin_menu",
            },
            {
                "trigger": "advance",
                "source": "coin_menu",
                "dest": "choose_coins",
                "conditions": "is_going_to_choose_coins",
            },
            {
                "trigger": "advance",
                "source": "coin_menu",
                "dest": "price",
                "conditions": "is_going_to_price",
            },
            {
                "trigger": "advance",
                "source": "coin_menu",
                "dest": "metadata",
                "conditions": "is_going_to_metadata",
            },
            {
                "trigger": "advance",
                "source": "menu",
                "dest": "introduction",
                "conditions": "is_going_to_introduction",
            },
            {
                "trigger": "advance",
                "source": "menu",
                "dest": "fsm_graph",
                "conditions": "is_going_to_fsm_graph",
            },
            {
                "trigger": "advance",
                "source": "price",
                "dest": "cancel",
                "conditions": "is_going_to_cancel",
            },
            {
                "trigger": "advance",
                "source": "price",
                "dest": "choose_coins",
                "conditions": "is_going_to_choose_coins",
            },
            {
                "trigger": "advance",
                "source": "price",
                "dest": "menu",
                "conditions": "is_going_to_menu",
            },
            {
                "trigger": "advance",
                "source": "metadata",
                "dest": "cancel",
                "conditions": "is_going_to_cancel",
            },
            {
                "trigger": "advance",
                "source": "metadata",
                "dest": "choose_coins",
                "conditions": "is_going_to_choose_coins",
            },
            {
                "trigger": "advance",
                "source": "metadata",
                "dest": "menu",
                "conditions": "is_going_to_menu",
            },

            {"trigger": "go_back", "source": ["introduction", "fsm_graph", "cancel"], "dest": "user"},
        ],
        initial="user",
        auto_transitions=False,
        show_conditions=True,
    )

    return machine