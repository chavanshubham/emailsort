from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly',
          'https://www.googleapis.com/auth/gmail.labels',
          'https://www.googleapis.com/auth/gmail.modify']

def main():
    
    # Credentials 

    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('gmail', 'v1', credentials=creds)

    # Check label

    def label_check(label_name):

        results = service.users().labels().list(userId='me').execute()
        labels = results.get('labels', [])

        for label in labels:
        
            if label['name'] == label_name:
                label_id = label['id']
                return label_id
            else:
                continue

    # Create label

    def label_maker(name):

        label_name = name 

        label = {
            'name': label_name
        }

        try:
            created_label = service.users().labels().create(userId = 'me', body = label).execute()
            print('Label created!')
        except:
            print("Error occured. Retry later.")
            exit()

    # Checking all messages for subject line

    def sort_messages(subject_line, filter_method):

        results = service.users().messages().list(userId='me').execute()
        messages = results.get('messages', [])
        message_id_list = []

        for message in messages:
            
            msg = service.users().messages().get(userId='me', id=message['id']).execute()
            headers = msg["payload"]["headers"]
            subject = [i['value'] for i in headers if i["name"]=="Subject"]
            
            # EXACT MATCH
            if filter_method == 1:
                if subject[0] == subject_line:      
                    message_id_list.append(message['id'])

            # CONTAINING THE PHRASE
            else:
                if subject_line in subject[0]:
                    message_id_list.append(message['id'])

        return message_id_list

    # Modify labels of desired messages

    def modify_labels(id_list, label_id):

        request_body = {
            "ids": id_list,
            "addLabelIds": [
                label_id
            ],
            "removeLabelIds": []
            }
        try:
            results = service.users().messages().batchModify(userId = 'me', body = request_body).execute()
            print('Emails added to label!')
        except:
            print("Error. Try again later.")

    # CONTROL FLOW

    label_name = input("Enter the label name: ")
    subject_line = input("Enter the subject line to filter with: ")
    
    while True:
        filter_method = input("Enter 1 for EXACT MATCH, 2 for CONTAINING PHRASE: ")
        if filter_method == '1' or filter_method == '2':
            break 
        else:
            print('Please enter the correct input.')
            continue

    label_id = label_check(label_name)
    if label_id != None: # Label already present, go straight to sort messages
        print('Label already present')
    else:
        label_maker(label_name) # else create label
        label_id = label_check(label_name) # get label ids

    ids = sort_messages(subject_line, filter_method)
    if ids: 
        print('Emails found!')
        modify_labels(ids, label_id)
    else:
        print('No such emails!')

if __name__ == '__main__':
    main()
