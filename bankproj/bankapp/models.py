# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import sys
import time
from django.db import models
from bankapp.utils import get_time,get_local_day_start_end

class BaseModel(models.Model):
	created_at = models.IntegerField(blank=False)
	updated_at = models.IntegerField(blank=False)

	def save(self,*args,**kwargs):
		try:
			if not self.created_at:
				self.created_at = get_time()
			self.updated_at = get_time()
			super(BaseModel,self).save(*args,**kwargs)

		except ValueError:
			return False

class BankCurrency(models.Model):
	currency_name = models.CharField(max_length = 25)
	currency_symbol = models.CharField(max_length = 5)

	class Meta:
		db_table = 'bank_currencies'

class AccountRules(BaseModel):
	min_balance = models.FloatField(default=0.00)
	max_deposit_per_transaction = models.FloatField(default=0.00)
	max_deposit_per_day_frequency = models.IntegerField(default=0)
	max_deposit_per_day = models.FloatField(default=0.00)
	min_withdrawl_per_transaction = models.FloatField(default=0.00)
	min_withdrawl_per_day_frequency = models.IntegerField(default=0)
	min_withdrawl_per_day = models.FloatField(default=0.00)

	class Meta:
		db_table = 'account_rules'

class BankAccountProfile(BaseModel):
	first_name = models.CharField(max_length = 10)
	last_name = models.CharField(max_length = 10)
	date_of_birth = models.IntegerField(blank=False,null=False)
	gender = models.CharField(max_length = 10)
	address = models.CharField(max_length = 200)
	pincode = models.CharField(max_length = 10)
	verified = models.BooleanField(default=False)
	account_id_num = models.CharField(max_length = 50)

	class Meta:
		db_table = 'account_profile'

class BankAccount(BaseModel):
	account_profile = models.ForeignKey(BankAccountProfile,related_name = 'bank_accounts_profile')
	account_number = models.CharField(max_length = 30)
	account_rules = models.ForeignKey(AccountRules,related_name = 'bank_accounts_rules')
	account_balance = models.FloatField(default=0.00)
	account_laser_balance = models.FloatField(default=0.00)
	account_ifsc = models.CharField(max_length = 20)
	account_currency = models.ForeignKey(BankCurrency,related_name = 'bank_accounts_currency')

	class Meta:
		db_table = 'bank_accounts'

	def getAccountCurrency(self):
		return self.account_currency.currency_symbol

	def getCurrentDayTransaction(self,timestamp,transaction_type = 'credit'):
		start_time,end_time = get_local_day_start_end(timestamp)
		transactions = Transactions.objects.filter(to_account = self,transaction_start_time__gte=start_time,transaction_start_time__lte=end_time,transaction_type=transaction_type)
		transactions_count = transactions.count()
		transaction_amount_total = transactions.aggregate(total_amount = models.Sum('transaction_amount'))
		return [transactions_count,transaction_amount_total['total_amount'] or 0.00]

	def initiateTransaction(self,amount,transaction_time,transaction_type):
		Transactions.objects.create(to_account=self,transaction_type=transaction_type,transaction_start_time=transaction_time,transaction_end_time=get_time(),transaction_amount=amount)


class Transactions(BaseModel):#change to sender and reciever
	from_account = models.ForeignKey(BankAccount,blank=True,null=True,related_name = 'account_transactions_from_account')
	to_account = models.ForeignKey(BankAccount,related_name = 'account_transactions_to_account')
	transaction_id = models.CharField(max_length = 50)#change length in next migration
	transaction_type = models.CharField(max_length = 10)#,choices=[('credit','credit')('debit','debit')])
	transaction_source = models.CharField(max_length = 10)
	transaction_amount = models.FloatField(default=0.00)
	transaction_status = models.CharField(max_length = 10)
	transaction_start_time = models.IntegerField(blank=False,null=False)
	transaction_end_time = models.IntegerField(blank=False,null=False)

	class Meta:
		db_table = 'account_transactions'

	def save(self,*args,**kwargs):
		try:
			self.transaction_id = str(self.to_account.account_number[:5]),str(get_time()),str(self.to_account.account_number[6:])
			super(Transactions,self).save(*args,**kwargs)

		except ValueError:
			return False




