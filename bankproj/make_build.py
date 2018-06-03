from bankapp.models import AccountRules,BankCurrency,BankAccountProfile,BankAccount


class MakeBuild:

	def __init__(self):
		self.account_request_data = {'first_name':'vikrant','last_name':'singh','date_of_birth':651024128,'gender':'male','address':'bangalore','pincode':'560076',
								'account_id_num':'DULPS1990V','account_number':'HSBC100023456','ifsc_code':'HSBC1000'}
		self.currency_request_data = {'currency_name':'dollar','currency_symbol':'$'}
		self.account_rules_date = {'max_deposit_per_transaction':40,'max_deposit_per_day_frequency':4,'max_deposit_per_day':150,
						'min_withdrawl_per_transaction':20,'min_withdrawl_per_day_frequency':3,'min_withdrawl_per_day':50}

	def setup(self):
		account_request = self.account_request_data
		currency_request = self.currency_request_data
		account_rules = self.account_rules_dat
		currency_obj = BankCurrency.objects.create(currency_name=currency_request_data['currency_name'],currency_symbol=currency_request_data['currency_symbol'])
		account_rules_obj = AccountRules.objects.create(max_deposit_per_transaction=account_rules['max_deposit_per_transaction'],
							max_deposit_per_day_frequency=account_rules['max_deposit_per_day_frequency'],
							max_deposit_per_day=account_rules['max_deposit_per_day'],
							min_withdrawl_per_transaction=account_rules['min_withdrawl_per_transaction'],
							min_withdrawl_per_day_frequency=account_rules['min_withdrawl_per_day_frequency'],
							min_withdrawl_per_day=account_rules['min_withdrawl_per_day'])
		account_profile_obj = BankAccountProfile.objects.create(first_name=account_request_data['first_name'],last_name=account_request_data['last_name'],
						date_of_birth=account_request_data['date_of_birth'],gender=account_request_data['gender'],pincode=account_request_data['pincode'],
						address=account_request_data['address'],account_id_num=account_request_data['account_id_num'])
		account_obj = BankAccount.objects.create(account_profile=account_profile_obj,account_number=account_request_data['account_number'],
						account_rules=account_rules_obj,account_ifsc=account_request_data['ifsc_code'],account_currency=currency_obj)
