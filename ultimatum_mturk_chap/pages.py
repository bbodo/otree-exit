from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
from otree_mturk_utils.views import CustomMturkPage, CustomMturkWaitPage


timeout_general = 100

class Introduction(CustomMturkPage):
    timeout_seconds = timeout_general
    def is_displayed(self):
        # app_name = self.subsession._meta.app_label
        # round_number = self.subsession.round_number
        # if not self.participant.vars.get('dropout'):
        #     if self.participant.vars.get('go_to_the_end') or self.participant.vars.get('skip_the_end_of_app_{}'.format(app_name)) or self.participant.vars.get('skip_the_end_of_app_{}_round_{}'.format(app_name , round_number)):
        #         self.participant.vars['dropout'] = False
        #         print('player', self.player.id_in_group, 'has go to end shit now, DID NOT BEFORE')
        #         for p in self.player.get_others_in_group():
        #             print(p.participant.vars)
        #             if not p.vars.get('go_to_the_end') or p.vars.get('skip_the_end_of_app_{}'.format(app_name)) or p.vars.get('skip_the_end_of_app_{}_round_{}'.format(app_name , round_number)):
        #                 p.participant.vars['dropout'] = True
        #                 print(p.participant.vars)
        
        return self.round_number == 1 # and not self.participant.vars['dropout']

class Grouping(CustomMturkWaitPage):
    template_name = "ultimatum_mturk_chap/Grouping.html"
    skip_until_the_end_of = 'experiment'
    startwp_timer = timeout_general
    use_task = False
    def is_displayed(self):
        # prin(self.group.get)
        return self.round_number == 1 and not self.participant.vars.get('dropout')
class ReGrouping(Grouping):
    group_by_arrival_time = False
    def is_displayed(self):
        return self.round_number > 1

class Offer(CustomMturkPage):
    form_model = 'group'
    form_fields = ['amount_offered']

    def is_displayed(self):
        print("Right now:", self.group.id, [p.participant.code for p in self.group.get_players()])
        if (self.round_number > 1):
            print("In first round:", self.group.in_round(1).id, [p.participant.code for p in self.group.in_round(1).get_players()])
        return self.player.id_in_group == 1

    timeout_seconds = timeout_general


class WaitForProposer(WaitPage):
    # template_name = "ultimatum_mturk_chap/Grouping.html"
    startwp_timer = timeout_general
    timer_text = "Maximum wait time left: "
    
    def is_displayed(self):
        app_name = self.subsession._meta.app_label
        round_number = self.subsession.round_number
        return not (self.participant.vars.get('go_to_the_end') or self.participant.vars.get('skip_the_end_of_app_{}'.format(app_name)) or self.participant.vars.get('skip_the_end_of_app_{}_round_{}'.format(app_name , round_number)))



class Accept(CustomMturkPage):
    form_model = 'group'
    form_fields = ['offer_accepted']

    def is_displayed(self):
        return self.player.id_in_group == 2 and not self.group.use_strategy_method

    timeout_seconds = timeout_general


class AcceptStrategy(CustomMturkPage):
    form_model = 'group'
    form_fields = ['response_{}'.format(int(i)) for i in
                   Constants.offer_choices]

    def is_displayed(self):
        return self.player.id_in_group == 2 and self.group.use_strategy_method and not self.participant.vars['global_timeout']

# class ResultsWaitPage(CustomMturkWaitPage):
class ResultsWaitPage(WaitPage):
    # template_name = "ultimatum_mturk_chap/ResultsWaitPage.html"
    def after_all_players_arrive(self):
        self.group.set_payoffs()
    # def is_displayed(self):
    #     return not self.group.global_timeout_happened
    def is_displayed(self):
        app_name = self.subsession._meta.app_label
        round_number = self.subsession.round_number
        return not self.participant.vars.get('go_to_the_end') or self.participant.vars.get('skip_the_end_of_app_{}'.format(app_name)) or self.participant.vars.get('skip_the_end_of_app_{}_round_{}'.format(app_name , round_number))



class Results(CustomMturkPage):
    timeout_seconds = timeout_general

class EndResults(CustomMturkPage):
    def vars_for_template(self):
        return {'total_payoff': self.participant.payoff_plus_participation_fee().to_real_world_currency(self.session) }
    def is_displayed(self):
        app_name = self.subsession._meta.app_label
        round_number = self.subsession.round_number
        return self.subsession.round_number == Constants.num_rounds


page_sequence = [
                 Grouping,
                #  ReGrouping,
                 Introduction,
                 Offer,
                 WaitForProposer,
                 Accept,
                 AcceptStrategy,
                 ResultsWaitPage,
                 Results,
                 EndResults
                 ]
