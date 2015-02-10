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

cal_id = "angelica@dropbox.com"

event = {
  'summary': 'Luncbox Lunch',
  'location': 'Tuckshop',
  'start': {
    'dateTime': '2014-06-03T10:00:00.000-07:00'
  },
  'end': {
    'dateTime': '2014-06-03T10:25:00.000-07:00'
  },
  'attendees': [
    {
      'email': 'smarx@dropbox.com',
      'email': 'angelicacoleman3@gmail.com',
    },
  ],
}

created_event = service.events().insert(calendarId='angelica@dropbox.com', body=event).execute()

print created_event['id']
