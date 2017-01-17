from . import models
from ._builtin import Page, WaitPage
from otree.api import Currency as c, currency_range
from .models import Constants


class Gamble_1(Page):
    form_model = models.Player
    form_fields = ['choice_1',]


class Gamble_2(Page):
    form_model = models.Player
    form_fields = ['choice_2',]

    def before_next_page(self):
        self.player.set_payoff()


page_sequence = [
    Gamble_1,
    Gamble_2
]
