from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Bodo Braegger'

doc = """
A simple information and consent page where subjects can only continue if they consent.
"""


class Constants(BaseConstants):
    name_in_url = 'mturk_consent'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    consent = models.BooleanField(widget=widgets.RadioSelect,
                                  initial=False
    )

    is_dropout = models.BooleanField(default=False)