"""
Guess 60 % - a modification of Guess 2/3
"""

from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c,
)


author = 'oTree/bobrae'

doc = """
Documentation of 'guess_two_thirds':
Players all guess a number; whoever guesses closest to
0.6 of the average wins.

See https://en.wikipedia.org/wiki/Guess_2/3_of_the_average
"""


class Constants(BaseConstants):
    players_per_group = 2
    num_rounds = 3
    name_in_url = 'guess_60'

    jackpot = c(100)
    guess_max = 100

    instructions_template = 'guess_60/Instructions.html'

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    sixty_percent_avg = models.FloatField()
    best_guess = models.PositiveIntegerField()
    num_winners = models.PositiveIntegerField()

    def set_payoffs(self):
        players = self.get_players()
        guesses = [p.guess for p in players]
        sixty_percent_avg = 0.6 * sum(guesses) / len(players)
        self.sixty_percent_avg = round(sixty_percent_avg, 2)
        self.best_guess = min(guesses, key=lambda guess: abs(guess - self.sixty_percent_avg)) 
        winners = [p for p in players if p.guess == self.best_guess]
        self.num_winners = len(winners)
        for p in winners: 
            p.is_winner = True
            p.payoff = Constants.jackpot / self.num_winners


    def sixty_percentage_avg_history(self):
        return [g.sixty_percent_avg for g in self.in_previous_rounds()]


class Player(BasePlayer):
    guess = models.PositiveIntegerField(max=Constants.guess_max,)
    is_winner = models.BooleanField(initial=False)
