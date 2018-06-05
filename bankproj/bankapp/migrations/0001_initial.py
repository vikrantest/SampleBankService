# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-06-05 11:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BankCurrency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currency_name', models.CharField(max_length=25)),
                ('currency_symbol', models.CharField(max_length=5)),
            ],
            options={
                'db_table': 'bank_currencies',
            },
        ),
        migrations.CreateModel(
            name='BaseModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.IntegerField()),
                ('updated_at', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='AccountRules',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='bankapp.BaseModel')),
                ('min_balance', models.FloatField(default=0.0)),
                ('max_deposit_per_transaction', models.FloatField(default=0.0)),
                ('max_deposit_per_day_frequency', models.IntegerField(default=0)),
                ('max_deposit_per_day', models.FloatField(default=0.0)),
                ('min_withdrawl_per_transaction', models.FloatField(default=0.0)),
                ('min_withdrawl_per_day_frequency', models.IntegerField(default=0)),
                ('min_withdrawl_per_day', models.FloatField(default=0.0)),
            ],
            options={
                'db_table': 'account_rules',
            },
            bases=('bankapp.basemodel',),
        ),
        migrations.CreateModel(
            name='BankAccount',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='bankapp.BaseModel')),
                ('account_number', models.CharField(max_length=30)),
                ('account_balance', models.FloatField(default=0.0)),
                ('account_laser_balance', models.FloatField(default=0.0)),
                ('account_ifsc', models.CharField(max_length=20)),
                ('account_currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bank_accounts_currency', to='bankapp.BankCurrency')),
            ],
            options={
                'db_table': 'bank_accounts',
            },
            bases=('bankapp.basemodel',),
        ),
        migrations.CreateModel(
            name='BankAccountProfile',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='bankapp.BaseModel')),
                ('first_name', models.CharField(max_length=10)),
                ('last_name', models.CharField(max_length=10)),
                ('date_of_birth', models.IntegerField()),
                ('gender', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=200)),
                ('pincode', models.CharField(max_length=10)),
                ('verified', models.BooleanField(default=False)),
                ('account_id_num', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'account_profile',
            },
            bases=('bankapp.basemodel',),
        ),
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='bankapp.BaseModel')),
                ('transaction_id', models.CharField(max_length=10)),
                ('transaction_type', models.CharField(max_length=10)),
                ('transaction_source', models.CharField(max_length=10)),
                ('transaction_amount', models.FloatField(default=0.0)),
                ('transaction_status', models.CharField(max_length=10)),
                ('transaction_start_time', models.IntegerField()),
                ('transaction_end_time', models.IntegerField()),
                ('from_account', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='account_transactions_from_account', to='bankapp.BankAccount')),
                ('to_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='account_transactions_to_account', to='bankapp.BankAccount')),
            ],
            options={
                'db_table': 'account_transactions',
            },
            bases=('bankapp.basemodel',),
        ),
        migrations.AddField(
            model_name='bankaccount',
            name='account_profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bank_accounts_profile', to='bankapp.BankAccountProfile'),
        ),
        migrations.AddField(
            model_name='bankaccount',
            name='account_rules',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bank_accounts_rules', to='bankapp.AccountRules'),
        ),
    ]
