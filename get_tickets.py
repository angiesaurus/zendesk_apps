import requests

url = 'https://{subdomain}.zendesk.com/api/v2/tickets.json'
user = 'email'
pwd = 'password'

response = requests.get(url, auth=(user, pwd))

if response.status_code != 200:
	print('Status:', response.status_code, 'Problem with the request. Exiting.')
	exit()

data = response.json()

#create any sort methods below
ticket_list = data['tickets']
for ticket in ticket_list:
	if ticket['status'] == 'pending':
		print(ticket['id'], ticket['status'], ticket['type'], ticket['priority'] , ticket['requester_id'], ticket['submitter_id'], ticket['organization_id'])
