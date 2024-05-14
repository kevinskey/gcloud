import os
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

SCOPES = ['https://www.googleapis.com/auth/calendar']

def main():
    # Update the path to your client secrets JSON file
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        'credentials.json', SCOPES)

    # Run the local server to handle the OAuth 2.0 flow
    creds = flow.run_local_server(port=0)

    # Save the credentials for future use
    with open('token.json', 'w') as token:
        token.write(creds.to_json())

if __name__ == '__main__':
    main()
curl -X POST http://localhost:5000/twilio-webhook \
    -d "inviteeEmail=kpj64110@gmail.com" \
    -d "inviteeFirstName=John" \
    -d "inviteeLastName=Doe" \
    -d "startTime=2024-06-01T12:00:00-07:00" \
    -d "endTime=2024-06-01T13:00:00-09:00"
