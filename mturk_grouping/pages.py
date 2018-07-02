from otree.api import Currency as c, currency_range
from otree_mturk_utils import views
from ._builtin import Page, WaitPage
from .models import Constants
from otree_mturk_utils.views import CustomMturkPage, CustomMturkWaitPage

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

class GroupingWP(CustomMturkWaitPage):
    template_name = "mturk_grouping/Grouping.html"
    skip_until_the_end_of = 'experiment'
    # startwp_timer = session.vars['wait_time']
    use_task = False
    startwp_timer = Constants.timer_seconds
    def set_timer(self):
        if self.session.vars.get('wait_time'):
            return self.session.vars['wait_time']
        else:
            return self.startwp_timer
    def is_displayed(self):
        self.startwp_timer = self.set_timer()
        startwp_timer = self.set_timer()
        return True



page_sequence = [
    GroupingWP
]
# for page in page_sequence:
#     page.startwp_timer = page.set_timer(page)
