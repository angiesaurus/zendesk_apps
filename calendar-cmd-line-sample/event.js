POST https://www.googleapis.com/calendar/v3/calendars/angelica%40dropbox.com/events?maxAttendees=5&sendNotifications=true&key={YOUR_API_KEY}

Content-Type:  application/json
Authorization:  Bearer ya29.1.AADtN_WrddcuR-c6ng1V3U0An2m7Oj_t6uGexpwL1NyIcDoagqUitmRt4disluk
X-JavaScript-User-Agent:  Google APIs Explorer
 
{
 "end": {
  "dateTime": "2014-06-03T10:25:00.000-07:00"
 },
 "start": {
  "dateTime": "2014-06-03T10:00:00.000-07:00"
 },
 "anyoneCanAddSelf": false,
 "creator": {
  "displayName": "Lunchbox Bot"
 },
 "attendees": [
  {
   "email": "leahculver@dropbox.com"
  },
  {
   "email": "smarx@dropbox.com"
  },
  {
   "email": "angelica@dropbox.com"
  }
 ],
 "guestsCanSeeOtherGuests": true,
 "summary": "Lunchbox Lunch",
 "endTimeUnspecified": false
}