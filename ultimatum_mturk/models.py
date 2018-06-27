from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random

doc = """
Ultimatum game with two treatments: direct response and strategy method.
In the former, one player makes an offer and the other either accepts or rejects.
It comes in two flavors, with and without hypothetical questions about the second player's response to offers other than the one that is made.
In the latter treatment, the second player is given a list of all possible offers, and is asked which ones to accept or reject.
"""


class Constants(BaseConstants):
    name_in_url = 'ultmturk'
    players_per_group = 2
    num_rounds = 5

    instructions_template = 'ultimatum_mturk/Instructions.html'

    endowment = c(100)
    payoff_if_rejected = c(0)
    payoff_showup = c(1000)
    offer_increment = c(10)

    offer_choices = currency_range(0, endowment, offer_increment)
    offer_choices_count = len(offer_choices)

    keep_give_amounts = []
    for offer in offer_choices:
        keep_give_amounts.append((offer, endowment - offer))


class Subsession(BaseSubsession):
    def creating_session(self):
        # randomize to treatments
        for g in self.get_groups():
            if 'use_strategy_method' in self.session.config:
                g.use_strategy_method = self.session.config['use_strategy_method']
            else:
                g.use_strategy_method = random.choice([True, False])
        for p in self.get_players():
            p.participant.vars['global_timeout'] = False



def make_field(amount):
    return models.BooleanField(
        widget=widgets.RadioSelectHorizontal,
        label='Would you accept an offer of {}?'.format(c(amount)))


class Group(BaseGroup):
    global_timeout_happened = models.BooleanField(
        doc="""Whether this group had a NoShow/DropOut"""
    )

    use_strategy_method = models.BooleanField(
        doc="""Whether this group uses strategy method""",
        default=False
    )

    amount_offered = models.CurrencyField(choices=Constants.offer_choices)

    offer_accepted = models.BooleanField(
        doc="if offered amount is accepted (direct response method)"
    )

    # for strategy method, see the make_field function above
    response_0  = make_field(0)
    response_10 = make_field(10)
    response_20 = make_field(20)
    response_30 = make_field(30)
    response_40 = make_field(40)
    response_50 = make_field(50)
    response_60 = make_field(60)
    response_70 = make_field(70)
    response_80 = make_field(80)
    response_90 = make_field(90)
    response_100 = make_field(100)


    def set_payoffs(self):
        p1, p2 = self.get_players()

        if self.global_timeout_happened:
            # p1.payoff = Constants.payoff_showup
            # p2.payoff = Constants.payoff_showup
            if p1.participant.vars['global_timeout']:
                p2.payoff = Constants.payoff_if_rejected
            else:
                p1.payoff = Constants.payoff_if_rejected
            return

        if self.use_strategy_method:
            self.offer_accepted = getattr(self, 'response_{}'.format(
                int(self.amount_offered)))

        if self.offer_accepted:
            p1.payoff = Constants.endowment - self.amount_offered
            p2.payoff = self.amount_offered
        else:
            p1.payoff = Constants.payoff_if_rejected
            p2.payoff = Constants.payoff_if_rejected


class Player(BasePlayer):
    pass