from flask import Flask, request, jsonify
import os
import googleapiclient.discovery
from google.oauth2.credentials import Credentials

app = Flask(__name__)

SCOPES = ['https://www.googleapis.com/auth/calendar']

# Load the credentials from the token.json file
creds = None
if os.path.exists('token.json'):
    creds = Credentials.from_authorized_user_file('token.json', SCOPES)

@app.route('/twilio-webhook', methods=['POST'])
def twilio_webhook():
    data = request.form
    invitee_email = data.get('inviteeEmail')
    invitee_first_name = data.get('inviteeFirstName')
    invitee_last_name = data.get('inviteeLastName')
    start_time = data.get('startTime')
    end_time = data.get('endTime')

    # Create a new event
    service = googleapiclient.discovery.build('calendar', 'v3', credentials=creds)
    event = {
        'summary': f'Appointment with {invitee_first_name} {invitee_last_name}',
        'start': {
            'dateTime': start_time,
            'timeZone': 'America/Los_Angeles',
        },
        'end': {
            'dateTime': end_time,
            'timeZone': 'America/Los_Angeles',
        },
        'attendees': [
            {'email': invitee_email}
        ],
    }
    event = service.events().insert(calendarId='primary', body=event).execute()

    return jsonify(event)

if __name__ == '__main__':
    app.run(port=5000, debug=True)

if __name__ == '__main__':
    app.run(port=5001, debug=True)

