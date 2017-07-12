from otree.api import (
	models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
	Currency as c, currency_range, safe_json
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
		# You can change the URL or leave it blank for a simple AccessCode, ExitCode file.
		encrypt_and_save_csv(self.session.participant_set.all(), \
		self.session.code, "")
		global json_data
		json_data = encrypt_and_save_json(self.session.participant_set.all(), \
		self.session.code, "http://127.0.0.1:8000/InitializeParticipant/")
		global json_data



	def vars_for_admin_report(self):
		return {'AccessExit': safe_json(json_data)}


class Group(BaseGroup):
	pass


class Player(BasePlayer):
	pass
