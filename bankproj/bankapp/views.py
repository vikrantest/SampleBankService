# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from bankapp.models import AccountRules,BankCurrency,BankAccountProfile,BankAccount
from bankapp.serializers import AccountSerializers


class AccountView(APIView):
	"""
	Account VIew to get account status
	"""

	
	def get(self,request):
		print(request.data)
		account_obj = BankAccount.objects.filter()[0]
		account_obj_data = AccountSerializers(account_obj).data
		return Response({"body": account_obj_data},status=status.HTTP_200_OK)