#!/usr/bin/env python
from __future__ import print_function
import uuid
import cgi

import squareconnect
from squareconnect.rest import ApiException
from squareconnect.apis.transactions_api import TransactionsApi

squareconnect.configuration.access_token = 'sandbox-sq0atb-kfvpHvEa9Mz2098Nozk1RQ'
location_id = 'CBASEGLb1fOhVH4Uvvi1aY_bOawgAQ'

# Create instance of FieldStorage
form = cgi.FieldStorage()
transaction_id = form.getvalue('transaction_id')
amount_money = int(form.getvalue('amount_money'))
tender_id = form.getvalue('tender_id')

api_instance = TransactionsApi()
idempotency_key = str(uuid.uuid1())
amount = {'amount': amount_money, 'currency': 'USD'}
body = {'idempotency_key': idempotency_key, 'tender_id': tender_id, 'amount_money': amount}


try:
  api_response = api_instance.create_refund(location_id, transaction_id, body)
  res = api_response.refund
  header = '<h2>Refund Success: </h2>'
except ApiException as e:
  res = "Exception when calling TransactionApi->refund: {}".format(e)
  header = '<h2>Refund Failed: </h2>'

print ('Content-type:text/html\r\n\r\n')
print ('<html>')
print ('<head>')
print ('<title>Square Payment</title>')
print ('</head>')
print (header)
print ('<body>')
print ('<p>{}</p>'.format(res))
print ('</body>')
print ('</html>')