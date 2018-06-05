# BankProj
Problem Statement - 
	The goal of this mini project is to write a simple micro web service to mimic a “Bank Account”. Through this web service, one can query about the balance, deposit money, and withdraw money. Just like any Bank, there are restrictions on how many transactions/amounts it can handle. The details are described below.
	● Write a simple “Bank Account” web service using REST API design principles. You can use either the Scala/Play or Java/Spring/Tomcat framework.
	○ Program should have 3 REST API endpoints: One to get the current balance, one to make a deposit, and one to make a withdrawal
	○ No requirement for authentication - assume the web service is for one account only and is open to the world
	○ No requirement for the backend store - you can store it in a file or database (your decision)
	■ Bonus points for a solution that won’t easily run out of memory after long periods of up-time
	○ Balance endpoint - this will return the outstanding balance
	○ Deposit endpoint - credits the account with the specified amount
	■ Max deposit for the day = $150K
	■ Max deposit per transaction = $40K
	■ Max deposit frequency = 4 transactions/day
	○ Withdrawal endpoint - deducts the account with the specified amount
	■ Max withdrawal for the day = $50K
	■ Max withdrawal per transaction = $20K
	■ Max withdrawal frequency = 3 transactions/day
	■ Cannot withdraw when balance is less than withdrawal amount
	● The service should handle all the error cases and return the appropriate error HTTP
	status code and error message (Eg. If an attempt is to withdraw greater than $20k in a single transaction, the error message should say “Exceeded Maximum Withdrawal Per Transaction”).
	● Write tests against your web service. ( Bonus:  implement a code coverage tool and show code coverage numbers for your tests)
	○ Ideally tests should be held to the same standard as main code
	● Make sure your code is readable and can be run.
	● Check in your code to bitbucket and write instructions on readme on how to run.

Tech Stack - 
	python2.7 - (you can use python 3 also , it will need small change in make file . Example - pip to pip3 , python to python3)
	Django - rest framework in python
	SQLite - light weight sql database.
	

Directory structure

	├── bankapp
	│   └── migrations
	├── bankproj
	├── buildapp
	└── testfiles

Build Process
	Initial Step - Go to root directory

	1 - Change directory to buildapp folder
			cd buildapp

	2 - Run "make" file for installing dependencies , creating db and settingup databases structure with test content .You can check the requirements in requirements.txt file inside buildapp folder
			Command - ./make

	3 - Run "run" file to start Django server on https://localhost:8000/ . If you want to change port number or host , open run file with any editor of you choice and update host and port number on line 7 .Once you are done save the file and run the below command.
			Command - ./run

	4 - Once server starts successfully , you can start using endpoints discussed in API section below.

TestCases
	Initial Step - Go to root directory

	1 - Change directory to buildapp folder
			cd buildapp
	2 - Run "testapp" file for running testcases for all endpoints with different scenarios in all 3 testcases.Test files are there in testfiles directory.
			Command - ./testapp


API endpoints 

There are 4 API endpoints
	1 - bankapp/v1/account/ - POST
		This API is for creating test content for an account to run different transaction scenarios on that account . No param is needed for this api.
		Warning - Don't use this API . Its main use is for test cases else it will re initialize account details.

	2 - bankapp/v1/account/ - GET
		This API is for getting account details of test account .
		Sample Success Response - {
								"message": "Account details.",
								"data": {
									"account_balance": 5.0,
									"currency": "$"
								}
							}
							
	3 - bankapp/v1/account/deposit POST
		This API is for depositing amount in that test account . It has several response based on validations and internal rule checks.
		Param - {"amount": "19.00"}
		Sucess Response - {
						"message": "Amount of $ 19.0 Successfully Deposited."
						}
	4 - bankapp/v1/account/withdrawl POST
		This API is for withdrawing amount in that test account . It has several response based on validations and internal rule checks.
		Param - {"amount": "10.00"}
		Sucess Response - {
						"message": "Amount of $ 10.0 Successfully Withdrawn."
						}


Extras - 
	To directly access database 
		Run python manage.py dbshell inside root directory
		