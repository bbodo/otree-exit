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
	name_in_url = 'mturkultm'
	players_per_group = 2
	num_rounds = 5

	instructions_template = 'mturk_ultimatum/Instructions.html'

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
				# g.use_strategy_method = random.choice([True, False])
				g.use_strategy_method = False
		if(self.round_number > 1):
			for p in self.get_players():
				p.dropout_caused = p.in_round(self.round_number-1).dropout_caused
				p.dropout_suffered=p.in_round(self.round_number-1).dropout_suffered



def make_field(amount):
	return models.BooleanField(
		widget=widgets.RadioSelectHorizontal,
		label='Would you accept an offer of {}?'.format(c(amount)))


class Group(BaseGroup):
	# global_timeout_happened = models.BooleanField(
	# 	doc="""Whether this group had a NoShow/DropOut"""
	# )

	use_strategy_method = models.BooleanField(
		doc="""Whether this group uses strategy method""",
		default=False
	)

	amount_offered = models.CurrencyField(choices=Constants.offer_choices)

	offer_accepted = models.BooleanField(
		doc="if offered amount is accepted (direct response method)"
	)

	# for strategy method, see the make_field function above
	# response_0  = make_field(0)
	# response_10 = make_field(10)
	# response_20 = make_field(20)
	# response_30 = make_field(30)
	# response_40 = make_field(40)
	# response_50 = make_field(50)
	# response_60 = make_field(60)
	# response_70 = make_field(70)
	# response_80 = make_field(80)
	# response_90 = make_field(90)
	# response_100 = make_field(100)


	def set_payoffs(self):
		p1, p2 = self.get_players()

		if self.use_strategy_method:
			self.offer_accepted = getattr(self, 'response_{}'.format(
				int(self.amount_offered)))
		if self.offer_accepted is None:
			self.offer_accepted = False
		if self.amount_offered is None:
			self.amount_offered = 0
		if self.offer_accepted:
			p1.payoff = Constants.endowment - self.amount_offered
			p2.payoff = self.amount_offered
		else:
			p1.payoff = Constants.payoff_if_rejected
			p2.payoff = Constants.payoff_if_rejected


class Player(BasePlayer):
	def chat_nickname(self):
		# return 'Player {}'.format(self.id_in_group)
		return self.participant.code
	def chat_configs(self):
		configs = []
		for other in self.get_others_in_group():
			if other.id_in_group < self.id_in_group:
				lower_id, higher_id = other.id_in_group, self.id_in_group
			else:
				lower_id, higher_id = self.id_in_group, other.id_in_group
			configs.append({
					# make a name for the channel that is the same for all
					# channel members. That's why we order it (lower, higher)
					'channel': '{}-{}-{}'.format(self.group.id, lower_id, higher_id),
					'label': 'Chat with Player {} ({}) in your group'.format(other.id_in_group, other.chat_nickname())
			})
		print(self.participant.code, configs)
		return configs
	
	dropout_caused = models.BooleanField(
		doc="Dropped out of this and following rounds.",
		initial = False
	)
	dropout_suffered = models.BooleanField(
		doc="This player's partner dropped out of this and following rounds.",
		initial = False
	)

