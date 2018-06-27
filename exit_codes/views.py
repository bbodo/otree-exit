from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants
from django.http import JsonResponse
# Import this function to get the exit code for a single player
from .exit_codes import aes_encrypt, sha_hash
#from .models import json_file

"""
    Cleaned up the pages for less confusion when testing.
"""

# CHANGE sha_hash TO aes_encrypt FOR MORE COMPLEX CODES.

class Checkout(Page):
    def vars_for_template(self):
        return {'exit_code' : sha_hash(self.participant.code)[0:8]}
    def is_displayed(self):
        print('This participant had a dropout tag', self.participant.vars.get('dropout'))
        if 'dropout' not in self.participant.vars:
            self.participant.vars['dropout'] = False
        return not self.participant.vars['dropout']

# class AccessExit():
#     test = JsonResponse({'AccessExit': json_file}, safe=False)

class DeadEnd(Page):
    def is_displayed(self):
        if 'dropout' not in self.participant.vars:
            self.participant.vars['dropout'] = False
        return self.participant.vars['dropout']


page_sequence = [
    Checkout,
    #AccessExit,
    DeadEnd,
]
