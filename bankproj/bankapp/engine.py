# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sys
from rest_framework.response import Response
from rest_framework import status
from bankapp.utils import get_time

class ResponseEngine:
	"""
	Response Engine for rendering success and error responses
	"""

	def __init__(self,response='success'):
		self.response = response


	def __call__(self,response_type,dataset):
		if response_type == 'error':
			return self.errorResponse(dataset)
		else:
			return self.successResponse(dataset)

	def errorResponse(self,dataset):
		if dataset['status_code'] == '400':
			status_code = status.HTTP_400_BAD_REQUEST

		response_data = {'error':dataset.get('message','')}


		return Response(response_data,status=status_code)


	def successResponse(self,dataset):
		if dataset['status_code'] == '200':
			status_code = status.HTTP_200_OK
		elif dataset['status_code'] == '201':
			status_code = status.HTTP_201_CREATED

		if not dataset.get('body'):
			response_data = {'message':dataset.get('message','')}
		else:
			response_data = {'message':dataset.get('message',''),'data':dataset.get('body',{})}


		return Response(response_data,status=status_code)



class RuleEngine:
	"""
	Rule engine for validating transaction
	"""

	def __init__(self,rules_set,transaction_time=None):
		self.rules_set = rules_set
		self.__current_time = transaction_time

	def __call__(self,transaction_type,bank_account,amount):
		if transaction_type == 'credit':
			return self.creditTransaction(bank_account,amount)
		elif transaction_type == 'debit':
			return self.debitTransaction(bank_account,amount)

	def currenDayTransactions(self,bank_account,transaction_type):
		return bank_account.getCurrentDayTransaction(self.__current_time,transaction_type=transaction_type)


	def creditTransaction(self,bank_account,amount):
		if self.rules_set.max_deposit_per_transaction < amount:
			return False , 'Exceeded Maximum Deposit Per Transaction.'
		current_day_transaction = self.currenDayTransactions(bank_account,'credit')
		if current_day_transaction[0] >= self.rules_set.max_deposit_per_day_frequency:
			return False , 'Exceeded Maximum Deposit Transaction Per Day.'
		if current_day_transaction[1]+amount >= self.rules_set.max_deposit_per_day:
			return False , 'Exceeded Maximum Deposit Per Day.'
		return True , 'You are eligible for this transaction'

	def debitTransaction(self,bank_account,amount):
		if bank_account.account_balance < amount:
			return False , 'Insufficent Account Balance.'
		if self.rules_set.min_withdrawl_per_transaction < amount:
			return False , 'Exceeded Maximum Withdrawal Per Transaction.'
		current_day_transaction = self.currenDayTransactions(bank_account,'debit')
		if current_day_transaction[0] >= self.rules_set.min_withdrawl_per_day_frequency:
			return False , 'Exceeded Maximum Withdrawal Transaction Per Day.'
		if current_day_transaction[1]+amount >= self.rules_set.min_withdrawl_per_day:
			return False , 'Exceeded Maximum Withdrawal Per Day.'
		return True , 'You are eligible for this transaction'
