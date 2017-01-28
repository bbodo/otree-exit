from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants

# Import this function to get the exit code for a single player
from .exit_codes import aes_encrypt, sha_hash

class ExitCodeWaitPage(WaitPage):

    def after_all_players_arrive(self):
        pass

"""
    Cleaned up the pages for less confusion when testing.
"""


# CHANGE sha_hash TO aes_encrypt FOR MORE COMPLEX CODES.

class Checkout(Page):
    def vars_for_template(self):
        return {'exit_code' : sha_hash(self.participant.code)[0:8]}


page_sequence = [
    # ExitCodeWaitPage,
    Checkout,
]
