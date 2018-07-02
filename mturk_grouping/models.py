from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Bodo Braegger'

# doc = """
#     Edit the 'group_size' parameter to match group size of the next app.
#     Edit the 'wait_time' parameter to determine how long a subject has to wait
#     before being able to skip a page (in seconds)
# """

doc = """
    Edit the players_per_group and timer_seconds in the Constants
"""


class Constants(BaseConstants):
    name_in_url = 'mturk_grouping'
    players_per_group = 2
    num_rounds = 1
    timer_seconds = 20


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass
