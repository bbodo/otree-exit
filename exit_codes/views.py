from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants
from django.http import JsonResponse
# Import this function to get the exit code for a single player
from .exit_codes import aes_encrypt, sha_hash
#from .models import json_file
from otree_mturk_utils.views import CustomMturkPage, CustomMturkWaitPage

"""
    Cleaned up the pages for less confusion when testing.
"""
class EndResults(CustomMturkPage):
    def is_displayed(self):
        app_name = self.subsession._meta.app_label
        round_number = self.subsession.round_number
        return self.participant.vars.get('go_to_the_end', True) and not self.participant.vars.get('dropout', False)

# CHANGE sha_hash TO aes_encrypt FOR MORE COMPLEX CODES.

class Checkout(Page):
    def vars_for_template(self):
        return {'exit_code' : sha_hash(self.participant.code)[0:8]}
    def is_displayed(self):
        print('Does this participant have a dropout tag:', self.participant.vars.get('dropout', 'Nope'))
        print('Does this participant have a go_to_the_end tag:', self.participant.vars.get('go_to_the_end', 'Nope'))
        return self.participant.vars.get('go_to_the_end', True) and not self.participant.vars.get('dropout', False)

# class AccessExit():
#     test = JsonResponse({'AccessExit': json_file}, safe=False)

class DeadEnd(Page):
    def is_displayed(self):
        return self.participant.vars.get('dropout', False)
        


page_sequence = [
    EndResults,
    Checkout,
    #AccessExit,
    DeadEnd,
]
