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
        choices=['Gamble A', 'Gamble B'],
        verbose_name='''
        A: 66% chance for a payoff of 2400, 33% chance for a payoff of 2500,
        1% chance for a payoff of 0, e.g. no payoff at all.
        B: 100% chance for a payoff of 2400.
        ''',
        widget=widgets.RadioSelect())

    gamble_2 = models.CharField(
        initial=None,
        choices=['Gamble A', 'Gamble B'],
        verbose_name='''
        A: 67% chance for a payoff of 0, e.g. no payoff at all.
        33% chance for a payoff of 2500. 
        B: 66% chance for a payoff of 0, e.g. no payoff at all.
        34% chance of a payoff of 2400.
        ''',
        widget=widgets.RadioSelect())