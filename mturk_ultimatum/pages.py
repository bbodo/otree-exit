from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
from otree_mturk_utils.views import CustomMturkPage, CustomMturkWaitPage
import types


timeout_general = 60

def before_next_page(self):
    if self.timeout_happened:
        self.participant.vars['dropout'] = True
        self.player.dropout_caused = True
        self.player.get_others_in_group()[0].dropout_suffered = True
        self.player.get_others_in_group()[0].participant.vars['go_to_the_end'] = True
        self.player.get_others_in_group()[0].participant.vars['dropout_suffered'] = True

def patch_in(target):
       target.before_next_page = types.MethodType(before_next_page, target)

class Introduction(CustomMturkPage):
    timeout_seconds = 3 * 60
    def vars_for_template(self):
        return {
            'participation_fee': self.session.config.get('participation_fee', 0),
            'points_conversion': self.session.config.get('real_world_currency_per_point', 0)*100,
            'total_payoff': self.participant.payoff_plus_participation_fee() 
            }
    def is_displayed(self):      
        return self.round_number == 1 # and not self.participant.vars['dropout']
    def before_next_page(self):
        before_next_page(self)



class Grouping(CustomMturkWaitPage):
    template_name = "ultimatum_mturk_chap/Grouping.html"
    skip_until_the_end_of = 'experiment'
    startwp_timer = 5 * 60
    use_task = False
    def is_displayed(self):
        # prin(self.group.get)
        return self.round_number == 1


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
    def before_next_page(self):
        before_next_page(self)



class WaitForProposer(WaitPage):
    # template_name = "ultimatum_mturk_chap/Grouping.html"
    startwp_timer = timeout_general
    timer_text = "Maximum wait time left: "
    
    def is_displayed(self):
        app_name = self.subsession._meta.app_label
        round_number = self.subsession.round_number
        return not self.participant.vars.get('dropout', False) and not (
                    self.participant.vars.get('go_to_the_end') or 
                    self.participant.vars.get('skip_the_end_of_app_{}'.format(app_name)) or 
                    self.participant.vars.get('skip_the_end_of_app_{}_round_{}'.format(app_name , round_number))
        )

class Accept(CustomMturkPage):
    form_model = 'group'
    form_fields = ['offer_accepted']

    def is_displayed(self):
        return self.player.id_in_group == 2 and not self.group.use_strategy_method

    timeout_seconds = timeout_general
    def before_next_page(self):
        before_next_page(self)



class AcceptStrategy(CustomMturkPage):
    form_model = 'group'
    form_fields = ['response_{}'.format(int(i)) for i in
                   Constants.offer_choices]

    def is_displayed(self):
        return self.player.id_in_group == 2 and self.group.use_strategy_method
    def before_next_page(self):
        before_next_page(self)


# class ResultsWaitPage(CustomMturkWaitPage):
class ResultsWaitPage(WaitPage):
    # template_name = "ultimatum_mturk_chap/ResultsWaitPage.html"
    def after_all_players_arrive(self):
        self.group.set_payoffs()
    def is_displayed(self):
        app_name = self.subsession._meta.app_label
        round_number = self.subsession.round_number
        return not self.participant.vars.get('dropout', False) and not (
                    self.participant.vars.get('go_to_the_end') or 
                    self.participant.vars.get('skip_the_end_of_app_{}'.format(app_name)) or 
                    self.participant.vars.get('skip_the_end_of_app_{}_round_{}'.format(app_name , round_number))
        )



class Results(CustomMturkPage):
    timeout_seconds = timeout_general
    def before_next_page(self):
        before_next_page(self)



pages = [
                #  Grouping,
                #  ReGrouping,
                 Introduction,
                 Offer,
                 WaitForProposer,
                 Accept,
                 AcceptStrategy,
                 ResultsWaitPage,
                 Results,
                #  EndResults
                # see exit_codes
                 ]

# for p in pages:
#     patch_in(p)
#     p.timeout_happened = False
#     p.before_next_page = types.MethodType(before_next_page, p)
#     print(p.before_next_page())
page_sequence = pages