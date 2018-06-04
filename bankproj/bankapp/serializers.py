# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
from rest_framework import serializers
from bankapp.models import *

class AccountSerializers(serializers.ModelSerializer):
	currency = serializers.ReadOnlyField(source = 'getAccountCurrency')
	

	class Meta:
		model = BankAccount
		fields = ('account_balance','currency')
