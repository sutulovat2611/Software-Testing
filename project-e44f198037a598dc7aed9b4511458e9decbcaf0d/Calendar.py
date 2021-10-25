# Make sure you are logged into your Monash student account.
# Go to: https://developers.google.com/calendar/quickstart/python
# Click on "Enable the Google Calendar API"
# Configure your OAuth client - select "Desktop app", then proceed
# Click on "Download Client Configuration" to obtain a credential.json file
# Do not share your credential.json file with anybody else, and do not commit it to your A2 git repository.
# When app is run for the first time, you will need to sign in using your Monash student account.
# Allow the "View your calendars" permission request.


# Students must have their own api key
# No test cases needed for authentication, but authentication may required for running the app very first time.
# http://googleapis.github.io/google-api-python-client/docs/dyn/calendar_v3.html


# Code adapted from https://developers.google.com/calendar/quickstart/python
from __future__ import print_function
import datetime
import pickle
import os.path

from dateutil.relativedelta import relativedelta
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar']


class Calendar:
    def get_calendar_api(self):
        """
        Get an object which allows you to consume the Google Calendar API.
        You do not need to worry about what this function exactly does, nor create test cases for it.
        """
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

        return build('calendar', 'v3', credentials=creds)

    def get_events_reminders_in_the_future(self, api, starting_time):
        """
            Represent events and reminders in next two years from today date.
            Prints the start and name of the next n events on the user's calendar.
        """
        current_time = datetime.datetime.today()
        ending_time = (current_time + relativedelta(years=+2)).isoformat() + 'Z'
        events_result = api.events().list(calendarId='primary', timeMax=ending_time, timeMin=starting_time,
                                          singleEvents=True, orderBy='startTime').execute()
        return events_result

    def get_event_by_keyword(self, api, common_events, subtype, type, key_word, defaultReminder):
        """
            Looking for an event by the key word that user inputs.
            Prints out its details and asks if the user wants to delete it.
        """
        print("Events found:\n")
        count = False
        if subtype == '':
            for event in common_events:
                if event[type] == key_word:
                    count = True
                    start = event['start'].get('dateTime', event['start'].get('date'))
                    override = event['reminders'].get('overrides')
                    default = event['reminders'].get('useDefault')
                    if default:
                        reminder = "Default reminder: " + defaultReminder[0]['method'] + ", " + str(
                            defaultReminder[0]['minutes']) + " minutes"
                    elif not default:
                        if override is None:
                            reminder = "This event does not have a reminder"
                        else:
                            reminder = "Reminder: " + event['reminders']['overrides'][0]['method'] + ", " + str(
                                event['reminders']['overrides'][0]['minutes']) + " minutes"
                    print(start, event['summary'], reminder)
                    # As a user, I can delete events and reminders
                    self.delete_event_reminder(api, event['id'])
        else:
            for event in common_events:
                if event[subtype][type] == key_word:
                    count = True
                    start = event['start'].get('dateTime', event['start'].get('date'))
                    override = event['reminders'].get('overrides')
                    default = event['reminders'].get('useDefault')
                    if default:
                        reminder = "Default reminder: " + defaultReminder[0]['method'] + ", " + str(
                            defaultReminder[0]['minutes']) + " minutes"
                    elif not default:
                        if override is None:
                            reminder = "This event does not have a reminder"
                        else:
                            reminder = "Reminder: " + event['reminders']['overrides'][0]['method'] + ", " + str(
                                event['reminders']['overrides'][0]['minutes']) + " minutes"
                    print(start, event['summary'], reminder)
                    # As a user, I can delete events and reminders
                    self.delete_event_reminder(api, event['id'])
        if not count:
            print("No events found")

    def get_past_events(self, api, starting_time):
        """
        Represent events and reminders past five years from today date.
        Prints the start and name of the next n events on the user's calendar.
        """
        # calculation for the past 5 years
        current_time = datetime.datetime.today()
        past_time = (current_time - relativedelta(days=+1826)).isoformat() + 'Z'
        # Implementing the functionality
        events_result = api.events().list(calendarId='primary', timeMin=past_time,
                                          timeMax=starting_time, singleEvents=True,
                                          orderBy='startTime').execute()

        return events_result

    def delete_event_reminder(self, api, eventId):
        """Deletes an event based on the event ID"""
        event = api.events().get(calendarId='primary', eventId=eventId).execute()
        override = event['reminders'].get('overrides')
        default = event['reminders'].get('useDefault')
        if not default and override is None:
            check = input("would you like to delete: \n 1. event \n 2. exit \n")
            if check == "1":
                api.events().delete(calendarId='primary', eventId=eventId, sendUpdates='all').execute()
                print("Event deleted successfully")
            elif check == '2':
                print("Event is not deleted")
            else:
                raise ValueError("Invalid Input")
        else:
            check = input("would you like to delete: \n 1. event \n 2. reminder \n 3. exit \n")
            if check == "1":
                api.events().delete(calendarId='primary', eventId=eventId, sendUpdates='all').execute()
                print("Event deleted successfully")
            elif check == "2":
                event['reminders'] = {
                    "useDefault": 'False',
                    "overrides": []
                }
                api.events().patch(calendarId='primary', eventId=eventId, body=event).execute()
                print("Reminder for the event is deleted successfully")
            elif check == '3':
                print("No deleted elements")
            else:
                raise ValueError("Invalid Input")

    def get_event_by_timeline(self, api):
        """Allows to find the events within the certain time range and choose one of them to represent the information about"""
        year = int(input('Input year: '))
        navigate = input('Navigate through: \n 1. Whole Year \n 2. Specific month \n')
        if navigate == '1':
            starting_time = datetime.datetime(year, 1, 1, 0, 0).isoformat() + 'Z'
            ending_time = datetime.datetime(year, 12, 31, 23, 59).isoformat() + 'Z'
        elif navigate == '2':
            month = int(input('Input month (in numbers e.g. 1 = January): '))
            if month < 1 or month > 12:
                raise ValueError("Month has to be between 1~12")
            navigateMonth = input('Navigate through: \n 1. Whole Month \n 2. Specific date \n')
            if navigateMonth == '1':
                starting_time = datetime.datetime(year, month, 1, 0, 0).isoformat() + 'Z'
                if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
                    ending_time = datetime.datetime(year, month, 31, 23, 59).isoformat() + 'Z'
                elif month == 2:
                    # checks for leap year
                    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
                        ending_time = datetime.datetime(year, month, 29, 23, 59).isoformat() + 'Z'
                    else:
                        ending_time = datetime.datetime(year, month, 28, 23, 59).isoformat() + 'Z'
                elif month == 4 or month == 6 or month == 9 or month == 11:
                    ending_time = datetime.datetime(year, month, 30, 23, 59).isoformat() + 'Z'
            elif navigateMonth == '2':
                if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
                    date = int(input('Insert day date (from 1 ~ 31)'))
                    if date < 1 or date > 31:
                        raise ValueError("Date must be between 1 and 31 ")
                elif month == 2:
                    # checks for leap year
                    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
                        date = int(input('Insert day date (from 1 ~ 29)'))
                        if date < 1 or date > 29:
                            raise ValueError("Date must be between 1 and 29 ")
                    else:
                        date = int(input('Insert day date (from 1 ~ 28)'))
                        if date < 1 or date > 28:
                            raise ValueError("Date must be between 1 and 28 ")
                elif month == 4 or month == 6 or month == 9 or month == 11:
                    date = int(input('Insert day date (from 1 ~ 30)'))
                    if date < 1 or date > 30:
                        raise ValueError("Date must be between 1 and 30 ")
                starting_time = datetime.datetime(year, month, date, 0, 0).isoformat() + 'Z'
                ending_time = datetime.datetime(year, month, date, 23, 59).isoformat() + 'Z'
            else:
                raise ValueError("Wrong navigation value")
        else:
            raise ValueError("Wrong navigation value")
        # getting the events from calendar
        events_result = api.events().list(calendarId='primary', timeMin=starting_time,
                                          timeMax=ending_time, singleEvents=True,
                                          orderBy='startTime').execute()
        defaultReminder = events_result.get('defaultReminders', [])
        eventList = events_result.get('items', [])
        if not eventList:
            print('No events found')
        else:
            print(self.represent_events_remiders(events_result))
            title = input("select event by typing it's title: \n")
            self.get_event_by_keyword(api, eventList, '', 'summary', title, defaultReminder)

    def represent_events_remiders(self, events_to_represent):
        """Represents the reminders for the list of events passed as a parameter"""
        events = events_to_represent.get('items', [])
        defaultReminder = events_to_represent.get('defaultReminders', [])
        output = ""
        if not events:
            print('No events found.')
        else:
            for event in events:
                start = event['start'].get('dateTime', event['start'].get('date'))
                override = event['reminders'].get('overrides')
                default = event['reminders'].get('useDefault')
                if default:
                    reminder = "Default reminder: " + defaultReminder[0]['method'] + ", " + str(
                        defaultReminder[0]['minutes']) + " minutes"
                elif not default:
                    if override is None:
                        reminder = "This event does not have a reminder"
                    else:
                        reminder = "Reminder: " + event['reminders']['overrides'][0]['method'] + ", " + str(
                            event['reminders']['overrides'][0]['minutes']) + " minutes"
                output += start + " " + event['summary'] + " " + reminder + " Organizer: " + event['organizer'][
                    'email'] + "\n"
        return output


def main():
    """Allows the user to interact with the calendar, works as an I/O console"""
    calendar = Calendar()
    menu = ""
    api = calendar.get_calendar_api()
    time_now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time

    while menu != '5':
        menu = input(
            "Menu\n 1.Show events in last 5 years\n 2.Show events in next two years\n 3.Navigate through years, "
            "months and dates\n "
            "4.Search for an event using a keyword\n 5.Exit\n")
        # 1. As a user, I can see events and reminders for at least 5 years in past from the today's date
        if menu == '1':
            print('Past events for the last 5 years: ')
            past_events = calendar.get_past_events(api, time_now)
            print(calendar.represent_events_remiders(past_events))

        # 2. As a user, I can see events and reminders for at least next two years (in future)
        elif menu == '2':
            print('Future events for the upcoming two years: ')
            events_in_two_years = calendar.get_events_reminders_in_the_future(api, time_now)
            print(calendar.represent_events_remiders(events_in_two_years))

        # 3. As a user, I can navigate through different days, months, and years in the calendar so that  I  can  view
        # the  details  of  events.  For  example,  if  the  year  2019  is  selected,  all  events, reminders,
        # and notifications will be shown. On selecting the specific event or reminder I can see the detailed
        # information.
        elif menu == '3':
            calendar.get_event_by_timeline(api)

        # 4. As a user, I can search events and reminders using different key words get_event_by_keyword(
        # api, time_now)
        elif menu == '4':
            check = False
            subtype = ''
            while check == False:
                check = True
                choice_input = input(
                    "What kind of key word would you like to use? \n 1.Organizer email\n 2.Title of the event \n "
                    "3.Location\n "
                    "4.Date and time\n")
                if choice_input == "1" or choice_input == "Organizer":
                    subtype = 'organizer'
                    type = 'email'
                elif choice_input == '2' or choice_input == "Title of the event":
                    type = 'summary'
                elif choice_input == '3' or choice_input == "Location":
                    type = 'location'
                elif choice_input == '4' or choice_input == "Date and time":
                    subtype = 'originalStartTime'
                    type = 'dateTime'
                else:
                    print("Invalid input.Try again")
                    check = False

            key_word = input("Input the keyword\n")  # keyword that is used to find the event
            getter = calendar.get_events_reminders_in_the_future(api,
                                                                 time_now)  # gets the info about the events in the
            # future
            events_in_two_years = getter.get('items', [])  # gets the events
            defaultReminder = getter.get('defaultReminders', [])  # gets the default reminder values
            events_in_five_years = calendar.get_past_events(api, time_now).get('items', [])
            common_events = events_in_two_years + events_in_five_years
            if not common_events:
                print('No events found')
            else:
                calendar.get_event_by_keyword(api, common_events, subtype, type, key_word, defaultReminder)
        # exit
        elif menu == '5':
            break
        # invalid input
        else:
            print('Invalid input, choose the number between 1-5')


#

if __name__ == "__main__":  # Prevents the main() function from being called by the test suite runner
    main()
