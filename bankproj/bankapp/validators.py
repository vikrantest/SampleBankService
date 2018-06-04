# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sys


class Validator:
	"""
	validator class for validating amounts and otherthing
	"""
	@staticmethod
	def isValidAmount(amount):
		if not isinstance(amount,float):
			try:
				return float(amount),True
			except ValueError:
				return amount,False
		return amount,True
