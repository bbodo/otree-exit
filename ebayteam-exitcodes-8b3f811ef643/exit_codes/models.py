from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
from .exit_codes import encrypt_and_save_csv, encrypt_and_save_json

author = 'Your name here'

doc = """
An example app for Amazon MTurk exit codes.
After the creating a session in the app using either the sessions tab or the demo tab
a new file named as 'YEAR-MONTH-DAY_Hour_Minute_Second_SessionCode.csv' will appear
in the project directory
"""


class Constants(BaseConstants):
    name_in_url = 'exit_codes'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    def before_session_starts(self):
        # Only Change the url to what you want before creating the session in otree
        encrypt_and_save_csv(self.session.participant_set.all(), self.session.code, "http://127.0.0.1:8000/InitializeParticipant/")
        encrypt_and_save_json(self.session.participant_set.all(), self.session.code, "http://127.0.0.1:8000/InitializeParticipant/")
   

class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass
