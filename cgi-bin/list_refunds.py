#!/usr/bin/env python
from __future__ import print_function
import cgi

import squareconnect
from squareconnect.rest import ApiException
from squareconnect.apis.transactions_api import TransactionsApi

squareconnect.configuration.access_token = 'sandbox-sq0atb-kfvpHvEa9Mz2098Nozk1RQ'
location_id = 'CBASEGLb1fOhVH4Uvvi1aY_bOawgAQ'

api_instance = TransactionsApi()

try:
  api_response = api_instance.list_transactions(location_id)
  res = api_response.transactions
except ApiException as e:
  res = "Exception when calling TransactionApi->list_transactions: {}".format(e)

 # Display the result
print ('Content-type:text/html\r\n\r\n')
print ('<html>')
print ('<head>')
print ('<title>Past Transactions</title>')
print ('</head>')
print ('<body>')
print ('<h2>Past Transactions: </h2>')
for transaction in res:
	print ('<p>{}</p>'.format(transaction))
	if not transaction.refunds:
		transaction_id = transaction.tenders[0].transaction_id
		amount_money = int(transaction.tenders[0].amount_money.amount)
		tender_id = transaction.tenders[0].id
		form = '''<form action="/cgi-bin/execute-refund.py" method="post">
			<input type="hidden" name="transaction_id" value="''' + str(transaction_id) + '''"">
			<input type="hidden" name="amount_money" value="''' + str(amount_money) + '''"">
			<input type="hidden" name="tender_id" value="''' + str(tender_id) + '''"">
	       <button type="submit"> Refund </button>
	    </form>'''
		print (form)

print ('</body>')
print ('</html>')
