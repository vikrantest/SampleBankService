# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class BaseModel(models.Model):
	pass

class BankAccount(BaseModel):
	pass


class AccountRules(BaseModel):
	pass


class Transactions(BaseModel):
	pass
