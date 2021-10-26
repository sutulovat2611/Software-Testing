# Software-Testing
## Calendar.py
This is the application that the test cases are to be written for. The application is developed so that it communicates with the Google Calendar API and in order to access it an API key has to be registered ( more details: https://developers.google.com/calendar).
The application provides the following features, which are to be tested in CalendarTest.py:
1. As a user, I can see events and reminders for at least 5 years in past from the today’s 
date.
2. As a user, I can see events and reminders for at least next two years (in future).
3. As a user, I can navigate through different days, months, and years in the calendar so 
that I can view the details of events. For example, if the year 2019 is selected, all 
events, reminders, and notifications will be shown. On selecting the specific event or
reminder I can see the detailed information.
4. As a user, I can search events and reminders using different key words.
5. As a user, I can delete events and reminders.


## CalendarTest.py
The test for __Calendar.py__, which examines it's functional correctness. The CalenderTest.py is to be run using the unittest module. The strategies that were used to select the test cases are explicitly documented in the document named __test-strategy.pdf__, which may be found in the Documents folder.



