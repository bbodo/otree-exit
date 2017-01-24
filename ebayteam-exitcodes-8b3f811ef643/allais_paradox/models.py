from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random


class Constants(BaseConstants):
    name_in_url = 'allais_paradox'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    def set_payoff(self):
        """Calculate payoff, which is zero for the survey"""
        self.payoff = 0

    gamble_1 = models.CharField(
        initial=None,
        choices=['Option A', 'Gamble B'],
        verbose_name='''Please choose your desired option''',
        widget=widgets.RadioSelect())

    gamble_2 = models.CharField(
        initial=None,
        choices=['Gamble A', 'Gamble B'],
        verbose_name='''Please choose your desired option''',
        widget=widgets.RadioSelect())