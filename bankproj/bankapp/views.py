# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from bankapp.models import AccountRules,BankCurrency,BankAccountProfile,BankAccount
from bankapp.serializers import AccountSerializers
from bankapp.validators import Validator
from bankapp.engine import ResponseEngine,RuleEngine
from bankapp.utils import get_time


class TransationValidations:
	"""
	TransationValidations for validating transactions based on rules for different ops on account
	"""


	@staticmethod
	def isValidTransaction(bank_account,amount,transaction_time,transaction_type):
		rule_engine = RuleEngine(bank_account.account_rules,transaction_time)
		valid_transaction = rule_engine(transaction_type,bank_account,amount)
		return valid_transaction


class AccountView(APIView):
	"""
	AccountView to get account status awith current balance and currency support for that account
	"""

	
	def get(self,request):
		response = ResponseEngine()
		bank_account = BankAccount.objects.filter()[0]
		if not bank_account:
			return response('error',{'message':'No account found.','status_code':'400'})
		account_obj_data = AccountSerializers(bank_account).data
		return response('success',{'message':'Account details.','status_code':'200','body':account_obj_data})



class AccountMoneyDeposit(APIView):
	"""
	AccountMoneyDeposit for depositing money into account
	"""

	def post(self,request):#for past dates
		request_data = request.data
		response = ResponseEngine()
		transaction_time = get_time()
		transaction_type = 'credit'
		amount,valid_amount = Validator.isValidAmount(request_data.get('amount'))
		if not valid_amount:
			return response('error',{'message':'Invalid amount for deposit - {}.'.format(str(amount)),'status_code':'400'})

		bank_account = BankAccount.objects.filter()[0]
		if not bank_account:
			return response('error',{'message':'No account found.','status_code':'400'})

		valid_transaction,message = TransationValidations.isValidTransaction(bank_account,amount,transaction_time,transaction_type)
		if not valid_transaction:
			return response('error',{'message':message,'status_code':'400'})

		bank_account.initiateTransaction(amount,transaction_time,transaction_type)
		bank_account.account_balance += amount
		bank_account.save()


		return response('success',{'message':'Amount of {} {} successfully deposited.'.format(str(bank_account.getAccountCurrency()),str(amount)),'status_code':'200','body':{}})


class AccountMoneyWithdrawl(APIView):
	"""
	AccountMoneyDeposit for depositing money into account
	"""

	def post(self,request):#for past dates
		request_data = request.data
		response = ResponseEngine()
		transaction_time = get_time()
		transaction_type = 'debit'
		amount,valid_amount = Validator.isValidAmount(request_data.get('amount'))
		if not valid_amount:
			return response('error',{'message':'Invalid amount for withdrawn - {}.'.format(str(amount)),'status_code':'400'})


		bank_account = BankAccount.objects.filter()[0]
		if not bank_account:
			return response('error',{'message':'No account found.','status_code':'400'})

		valid_transaction,message = TransationValidations.isValidTransaction(bank_account,amount,transaction_time,transaction_type)
		if not valid_transaction:
			return response('error',{'message':message,'status_code':'400'})

		bank_account.initiateTransaction(amount,transaction_time,transaction_type)
		bank_account.account_balance -= amount
		bank_account.save()


		return response('success',{'message':'Amount of {} {} successfully withdrawn.'.format(str(bank_account.getAccountCurrency()),str(amount)),'status_code':'200','body':{}})
