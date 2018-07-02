from otree.api import Currency as c, currency_range
from otree_mturk_utils import views
from ._builtin import Page, WaitPage
from .models import Constants



class ConsentPage(Page):
    def is_displayed(self):
        return self.round_number == 1


page_sequence = [
    ConsentPage,
]
