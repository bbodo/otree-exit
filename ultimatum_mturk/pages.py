from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
# from otree_mturk_utils.views import CustomMturkPage, CustomMturkWaitPage


timeout_general = 100

class Introduction(Page):
    timeout_seconds = timeout_general
    def is_displayed(self):
        return self.round_number == 1

# class Grouping(CustomMturkWaitPage):
class Grouping(Page):
    skip_until_the_end_of = 'app'
    startwp_timer = 1
    use_task = False

class Offer(Page):
    form_model = 'group'
    form_fields = ['amount_offered']

    def is_displayed(self):
        return self.player.id_in_group == 1 and not self.player.participant.vars['global_timeout']

    timeout_seconds = timeout_general


# class WaitForProposer(CustomMturkPage):
class WaitForProposer(Page):
    template_name = "ultimatum_mturk/WaitForProposer.html"
    timeout_seconds = timeout_general
    timer_text = "Maximum wait time left: "

    # def vars_for_template(self):
    #     return {
    #         "title_text": "Please wait",
    #         "body_text": "Waiting for other participants"
    #     }

    # def is_displayed(self):
    #     if self.player.get

    def before_next_page(self):
        if self.timeout_happened:
            self.player.participant.vars['global_timeout'] = True
            self.player.get_others_in_group()[0].participant.vars['global_timeout'] = True
    
    def is_displayed(self):
        return not self.player.participant.vars['global_timeout']


class Accept(Page):
    form_model = 'group'
    form_fields = ['offer_accepted']

    def is_displayed(self):
        return self.player.id_in_group == 2 and not self.group.use_strategy_method and not self.player.participant.vars['global_timeout']

    timeout_seconds = timeout_general


class AcceptStrategy(Page):
    form_model = 'group'
    form_fields = ['response_{}'.format(int(i)) for i in
                   Constants.offer_choices]

    def is_displayed(self):
        return self.player.id_in_group == 2 and self.group.use_strategy_method and not self.player.participant.vars['global_timeout']

class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_payoffs()
    def is_displayed(self):
        return not self.player.participant.vars['global_timeout']


class Results(Page):
    def is_displayed(self):
        return not self.player.participant.vars['global_timeout']


page_sequence = [
                #  Grouping,
                 Introduction,
                 Offer,
                 WaitForProposer,
                 Accept,
                 AcceptStrategy,
                 ResultsWaitPage,
                 Results]
