from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class BasePage(Page):
    def get_timeout_seconds(self):
        return self.session.config.get('timeout_seconds', 30)

class Introduction(BasePage):
    pass


class Offer(BasePage):
    form_model = 'group'
    form_fields = ['amount_offered']

    def is_displayed(self):
        return self.player.id_in_group == 1


class WaitForProposer(WaitPage):
    pass


class Accept(BasePage):
    form_model = 'group'
    form_fields = ['offer_accepted']

    def is_displayed(self):
        return self.player.id_in_group == 2 and not self.group.use_strategy_method


class AcceptStrategy(BasePage):
    form_model = 'group'
    form_fields = ['response_{}'.format(int(i)) for i in
                   Constants.offer_choices]

    def is_displayed(self):
        return self.player.id_in_group == 2 and self.group.use_strategy_method


class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_payoffs()


class Results(BasePage):
    pass


page_sequence = [Introduction,
                 Offer,
                 WaitForProposer,
                 Accept,
                 AcceptStrategy,
                 ResultsWaitPage,
                 Results]
