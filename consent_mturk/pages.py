from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class GroupingWaitPage(WaitPage):
    group_by_arrival_time = True

    def get_players_for_group(self, waiting_players):
        print('in get_players_for_group')
        # a_players = [p for p in waiting_players if p.participant.vars['type'] == 'A']
        # b_players = [p for p in waiting_players if p.participant.vars['type'] == 'B']

        # if len(a_players) >= 2 and len(b_players) >= 2:
        if len(waiting_players >= 2):
            print('about to create a group')
            # return [a_players[0], a_players[1], b_players[0], b_players[1]]
            return waiting_players[0:self.session.config['players_per_group']-1]
        print('not enough players to create a group')

    def is_displayed(self):
        return self.round_number == 1


class MyPage(Page):
    pass


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        pass


class Results(Page):
    pass


page_sequence = [
    MyPage,
    ResultsWaitPage,
    Results
]
