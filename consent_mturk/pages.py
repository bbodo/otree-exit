from otree.api import Currency as c, currency_range
from otree_mturk_utils import views
from ._builtin import Page, WaitPage
from .models import Constants



class ConsentPage(Page):
    form_model = 'player'
    form_fields = ['consent']
    def is_displayed(self):
        return self.round_number == 1
    def before_next_page(self):
        if not self.player.consent:
            self.participant.vars['consent_dropout'] = True
        if self.timeout_happened:
            self.player.consent = False
            self.player.is_dropout = True
            self.player.participant.vars['dropout'] = True
            self.player.participant.vars['consent_dropout'] = True


class BlockDropouts(Page):
    def is_displayed(self):
        return self.round_number == 1 and self.player.participant.vars.get('consent_dropout', False)
        


page_sequence = [
    ConsentPage,
    BlockDropouts,
]
