import requests

url = 'https://{subdomain}.zendesk.com/api/v2/tickets.json'
user = '{email}'
pwd = '{password}'

response = requests.get(url, auth=(user, pwd))

if response.status_code != 200:
	print('Status:', response.status_code, 'Problem with the request. Exiting.')
	exit()

data = response.json()

ticket_list = data['tickets']
tickets_by_requester =[]
for ticket in ticket_list:
	if ticket['requester_id'] == [id_numbers]:
		tickets_by_requester.append(ticket['id'])
print tickets_by_requester






