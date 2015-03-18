import requests

url = 'https://{subdomain}.zendesk.com/api/v2/tickets.json'
<<<<<<< HEAD
user = '{email}'
pwd = '{password}'
=======
user = 'email'
pwd = 'password'
>>>>>>> 5989b90bb202555f07c48b78669ba7974f3c7a0d

response = requests.get(url, auth=(user, pwd))

if response.status_code != 200:
	print('Status:', response.status_code, 'Problem with the request. Exiting.')
	exit()

data = response.json()

<<<<<<< HEAD
ticket_list = data['tickets']
tickets_by_requester =[]
for ticket in ticket_list:
	if ticket['requester_id'] == [id_numbers]:
		tickets_by_requester.append(ticket['id'])
print tickets_by_requester






=======
#create any sort methods below
ticket_list = data['tickets']
for ticket in ticket_list:
	if ticket['status'] == 'pending':
		print(ticket['id'], ticket['status'], ticket['type'], ticket['priority'] , ticket['requester_id'], ticket['submitter_id'], ticket['organization_id'])
>>>>>>> 5989b90bb202555f07c48b78669ba7974f3c7a0d
