import gflags
import httplib2
import datetime
import pprint

from apiclient.discovery import build
from oauth2client.file import Storage
from oauth2client.client import OAuth2WebServerFlow
from oauth2client.tools import run

FLAGS = gflags.FLAGS

FLOW = OAuth2WebServerFlow(
    client_id='777520625445-7md8r21em7k31ukcqpb9n249ps09or4n.apps.googleusercontent.com',
    client_secret='Z-9F_50oJkyEEIDrd381rZF5',
    scope='https://www.googleapis.com/auth/calendar',
    user_agent='iago/2')

storage = Storage('calendar.dat')
credentials = storage.get()
if credentials is None or credentials.invalid == True:
    credentials = run(FLOW, storage)

http = httplib2.Http()
http = credentials.authorize(http)

service = build(serviceName='calendar', version='v3', http=http,
   developerKey='AIzaSyDdcplN3xcS-h2VqO3VPj9fHaHhycIvSnY')

minDate = (datetime.datetime.utcnow() - datetime.timedelta(days=10)).isoformat('T')
maxDate = (datetime.datetime.utcnow() + datetime.timedelta(days=1)).isoformat('T')

print minDate, maxDate

cal_id = "primary"

l = service.events().list(calendarId=cal_id,  timeMin=minDate+'Z', timeMax=maxDate+'Z', pageToken=None).execute()

running = 1
items = []

while running:
    print 'loading...'
    for i in l['items']:
        items.append(i)
    page_token = l.get('nextPageToken')
    print page_token
    if not page_token:
        running = 0
    else:
        l = service.events().list(calendarId=cal_id, timeMin=minDate+'Z', timeMax=maxDate+'Z', pageToken=page_token).execute()

items = sorted(items, key=lambda x: x.get('start', {}).get('dateTime', '').split('T')[-1])

print len(items)

print items
