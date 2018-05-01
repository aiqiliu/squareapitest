#!/usr/bin/env python
# coding: utf-8
from __future__ import print_function
import uuid
import cgi

import squareconnect
from squareconnect.rest import ApiException
from squareconnect.apis.transactions_api import TransactionsApi
from squareconnect.apis.locations_api import LocationsApi
from squareconnect.apis.customers_api import CustomersApi

# Create instance of FieldStorage
form = cgi.FieldStorage()

# Get data from fields
nonce = form.getvalue('nonce')
# Get amount data
donation = form.getvalue('amount')

boxChecked = form.getvalue('boxChecked')
firstName = form.getvalue('firstname')
lastName = form.getvalue('lastname')
email = form.getvalue('email')


# The access token to use in all Connect API requests. Use your *sandbox* access
# token if you're just testing things out.
squareconnect.configuration.access_token = 'sandbox-sq0atb-kfvpHvEa9Mz2098Nozk1RQ'

# The ID of the business location to associate processed payments with.
# See [Retrieve your business's locations]
# (https://docs.connect.squareup.com/articles/getting-started/#retrievemerchantprofile)
# for an easy way to get your business's location IDs.
# If you're testing things out, use a sandbox location ID.
location_id = 'CBASEGLb1fOhVH4Uvvi1aY_bOawgAQ'

transactions_api_instance = TransactionsApi()
customers_api_instance = CustomersApi()

# Every payment you process with the SDK must have a unique idempotency key.
# If you're unsure whether a particular payment succeeded, you can reattempt
# it with the same idempotency key without worrying about double charging
# the buyer.
idempotency_key = str(uuid.uuid1())

# Monetary amounts are specified in the smallest unit of the applicable currency.
# This amount is in cents. It's also hard-coded for $1.00, which isn't very useful.
amount = {'amount': int(donation) * 100, 'currency': 'USD'}

customersList = []

# Add a customer to file
if boxChecked == "true": 
	heading = "Recurring Donation"
	customerRequest = {'given_name': firstName, 'family_name': lastName, 'email_address': email}

	try:
		customerResponse = customers_api_instance.create_customer(customerRequest)
	except ApiException as e:
		print ("customer creation failed")
		print (e)
		exit()

	customer = customerResponse.customer
	customerCardRequest = {'card_nonce': nonce}

	try:
		customerCardResponse = customers_api_instance.create_customer_card(customer.id, customerCardRequest)
	except:
		print ("customer card creation failed")
		exit()

	customerCard = customerCardResponse.card

	body = {'customer_id': customer.id, 'customer_card_id': customerCard.id, 'idempotency_key': idempotency_key, 'amount_money': amount}
	customersList = customers_api_instance.list_customers()
else:
	# To learn more about splitting transactions with additional recipients,
	# see the Transactions API documentation on our [developer site]
	# (https://docs.connect.squareup.com/payments/transactions/overview#mpt-overview).
	heading = "One time Donation"
	body = {'idempotency_key': idempotency_key, 'card_nonce': nonce, 'amount_money': amount}
	# customersList = Non


# The SDK throws an exception if a Connect endpoint responds with anything besides
# a 200-level HTTP code. This block catches any exceptions that occur from the request.
try:
  api_response = transactions_api_instance.charge(location_id, body)
  res = api_response.transaction
except ApiException as e:
  res = "Exception when calling TransactionApi->charge: {}".format(e)

# Display the result
print ('Content-type:text/html\r\n\r\n')
print ('<html>')
print ('<head>')
print ('<title>Square Payment</title>')
print ('</head>')
print ('<body>')
print ('<h2>Result: </h2>')
print( '<h2>{}</h2>'.format(heading))
print ('<p>{}</p>'.format(res))
if customersList:
	print( '<h2>Customers stored on File: </h2>')
	for customer in customersList.customers:
		print ('<p>{}</p>'.format(customer))

print ('</body>')
print ('</html>')
