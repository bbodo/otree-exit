# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import otree_save_the_change.mixins
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('otree', '0016_auto_20161120_1843'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('id_in_subsession', otree.db.models.PositiveIntegerField(null=True, db_index=True)),
                ('round_number', otree.db.models.PositiveIntegerField(null=True, db_index=True)),
                ('sixty_percent_avg', otree.db.models.FloatField(null=True)),
                ('best_guess', otree.db.models.PositiveIntegerField(null=True)),
                ('num_winners', otree.db.models.PositiveIntegerField(null=True)),
                ('session', models.ForeignKey(related_name='guess_60_group', to='otree.Session')),
            ],
            options={
                'db_table': 'guess_60_group',
            },
            bases=(otree_save_the_change.mixins.SaveTheChange, models.Model),
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('id_in_group', otree.db.models.PositiveIntegerField(null=True, db_index=True)),
                ('payoff', otree.db.models.CurrencyField(null=True, default=0, max_digits=12)),
                ('round_number', otree.db.models.PositiveIntegerField(null=True, db_index=True)),
                ('_group_by_arrival_time_arrived', otree.db.models.BooleanField(default=False, choices=[(True, 'Yes'), (False, 'No')])),
                ('_group_by_arrival_time_grouped', otree.db.models.BooleanField(default=False, choices=[(True, 'Yes'), (False, 'No')])),
                ('guess', otree.db.models.PositiveIntegerField(null=True)),
                ('is_winner', otree.db.models.BooleanField(default=False, choices=[(True, 'Yes'), (False, 'No')])),
                ('group', models.ForeignKey(null=True, to='guess_60.Group')),
                ('participant', models.ForeignKey(related_name='guess_60_player', to='otree.Participant')),
                ('session', models.ForeignKey(related_name='guess_60_player', to='otree.Session')),
            ],
            options={
                'db_table': 'guess_60_player',
            },
            bases=(otree_save_the_change.mixins.SaveTheChange, models.Model),
        ),
        migrations.CreateModel(
            name='Subsession',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('round_number', otree.db.models.PositiveIntegerField(null=True, db_index=True)),
                ('session', models.ForeignKey(null=True, related_name='guess_60_subsession', to='otree.Session')),
            ],
            options={
                'db_table': 'guess_60_subsession',
            },
            bases=(otree_save_the_change.mixins.SaveTheChange, models.Model),
        ),
        migrations.AddField(
            model_name='player',
            name='subsession',
            field=models.ForeignKey(to='guess_60.Subsession'),
        ),
        migrations.AddField(
            model_name='group',
            name='subsession',
            field=models.ForeignKey(to='guess_60.Subsession'),
        ),
    ]
