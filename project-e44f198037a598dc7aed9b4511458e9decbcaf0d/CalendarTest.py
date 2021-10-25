import datetime
import unittest
from unittest import mock
from unittest.mock import Mock, MagicMock
from Calendar import Calendar
# import Calendar
from mock import patch


# Add other imports here if needed


class CalendarTest(unittest.TestCase):

    def test_get_events_reminders_in_the_future(self):
        # This is because the function is dependent on the api() and has no conditions or branches
        # Test 1: Getting the future events from
        # the api (statement coverage as this function does not contain any branches)
        mock_api = Mock()
        calendar = Calendar()
        # Assuming that the date today is 14/10/2020
        time_now = '2020-10-13T16:59:25.423Z'
        # expected output the function should provide
        future_events = {'kind': 'calendar#events',
                         'etag': '"p32cd7ue3oenuo0g"',
                         'summary': 'tsut0005@student.monash.edu',
                         'updated': '2020-10-12T16:59:25.423Z',
                         'timeZone': 'Asia/Kuala_Lumpur',
                         'accessRole': 'owner',
                         'defaultReminders': [{'method': 'popup', 'minutes': 10}],
                         'items': [
                             {'kind': 'calendar#event',
                              'etag': '"3196377768156000"',
                              'id': '197qogoh7r4rehiieelecnul98_20201014T040000Z',
                              'status': 'confirmed',
                              'htmlLink': 'https://www.google.com/calendar/event?eid'
                                          '=MTk3cW9nb2g3cjRyZWhpaWVlbGVjbnVsOThfMjAyMDEwMTRUMDQwMDAwWiB0c3V0MDAwNUBzdHV'
                                          'kZW50Lm1vbmFzaC5lZHU',
                              'created': '2020-08-13T02:33:40.000Z',
                              'updated': '2020-08-23T13:21:24.078Z',
                              'summary': 'FIT2107 TESTING LECTURE',
                              'creator': {
                                  'email': 'tsut0005@student.monash.edu',
                                  'self': True},
                              'organizer': {
                                  'email': 'tsut0005@student.monash.edu',
                                  'self': True},
                              'start': {'dateTime': '2020-10-14T12:00:00+08:00'},
                              'end': {'dateTime': '2020-10-14T13:00:00+08:00'},
                              'recurringEventId': '197qogoh7r4rehiieelecnul98',
                              'originalStartTime': {'dateTime': '2020-10-14T12:00:00+08:00'},
                              'iCalUID': '197qogoh7r4rehiieelecnul98@google.com',
                              'sequence': 0,
                              'reminders': {'useDefault': True}
                              },
                             {'kind': 'calendar#event',
                              'etag': '"3204656707822000"',
                              'id': '6qilic69tedq4305c6dftvtblr',
                              'status': 'confirmed',
                              'htmlLink': 'https://www.google.com/calendar/event?eid=NnFpbGljNjl0ZWRxNDMwNWM2ZGZ0dnRibH'
                                          'IgdHN1dDAwMDVAc3R1ZGVudC5tb25hc2guZWR1',
                              'created': '2020-10-10T11:11:31.000Z',
                              'updated': '2020-10-10T11:11:31.229Z',
                              'summary': 'FIT2107 TESTING LECTURE 2',
                              'creator': {
                                  'email': 'tsut0005@student.monash.edu',
                                  'self': True},
                              'organizer': {
                                  'email': 'tsut0005@student.monash.edu',
                                  'self': True},
                              'start': {'dateTime': '2020-10-15T13:30:00+08:00'},
                              'end': {'dateTime': '2020-10-15T14:30:00+08:00'},
                              'iCalUID': '6qilic69tedq4305c6dftvtblr@google.com',
                              'sequence': 0,
                              'reminders': {'useDefault': False}
                              },
                             {'kind': 'calendar#event',
                              'etag': '"3204656707822000"',
                              'id': '6qilic69tedq4305c6dftvtblr',
                              'status': 'confirmed',
                              'htmlLink': 'https://www.google.com/calendar/event?eid=NnFpbGljNjl0ZWRxNDMwNWM2ZGZ0dnRibH'
                                          'IgdHN1dDAwMDVAc3R1ZGVudC5tb25hc2guZWR1',
                              'created': '2020-10-10T11:11:31.000Z',
                              'updated': '2020-10-10T11:11:31.229Z',
                              'summary': 'FIT2107 TESTING LECTURE 3',
                              'creator': {
                                  'email': 'tsut0005@student.monash.edu',
                                  'self': True},
                              'organizer': {
                                  'email': 'tsut0005@student.monash.edu',
                                  'self': True},
                              'start': {'dateTime': '2020-10-15T13:30:00+08:00'},
                              'end': {'dateTime': '2020-10-15T14:30:00+08:00'},
                              'iCalUID': '6qilic69tedq4305c6dftvtblr@google.com',
                              'sequence': 0,
                              'reminders': {'useDefault': False,
                                            "overrides": [
                                                {
                                                    "method": "email",
                                                    "minutes": 30
                                                },
                                            ]}
                              }
                         ]
                         }
        # setting up api
        mock_api.events.return_value.list.return_value.execute.return_value = future_events
        # Testing the function call
        returned_request = calendar.get_events_reminders_in_the_future(mock_api, time_now)
        self.assertEqual(returned_request, future_events)

    def test_get_past_events(self):
        # Testing to get event and reminders in the past 5 years. Only one test will be Conducted.
        # This is because the function is dependent on the api() and has no conditions or branches
        # Test 1: Getting the future events from
        # the api (statement coverage as this function does not contain any branches)
        # Assuming that the date today is 14/10/2020
        time_now = '2020-10-16T16:59:25.423Z'
        mock_api = Mock()
        calendar = Calendar()
        # Assuming that the date today is 14/10/2020
        time_now = '2020-10-13T16:59:25.423Z'
        # expected output the function should provide
        past_events = {'kind': 'calendar#events',
                       'etag': '"p32cd7ue3oenuo0g"',
                       'summary': 'tsut0005@student.monash.edu',
                       'updated': '2020-10-12T16:59:25.423Z',
                       'timeZone': 'Asia/Kuala_Lumpur',
                       'accessRole': 'owner',
                       'defaultReminders': [{'method': 'popup', 'minutes': 10}],
                       'items': [
                           {'kind': 'calendar#event',
                            'etag': '"3196377768156000"',
                            'id': '197qogoh7r4rehiieelecnul98_20201014T040000Z',
                            'status': 'confirmed',
                            'htmlLink': 'https://www.google.com/calendar/event?eid'
                                        '=MTk3cW9nb2g3cjRyZWhpaWVlbGVjbnVsOThfMjAyMDEwMTRUMDQwMDAwWiB0c3V0MDAwNUBzdHV'
                                        'kZW50Lm1vbmFzaC5lZHU',
                            'created': '2020-08-13T02:33:40.000Z',
                            'updated': '2020-08-23T13:21:24.078Z',
                            'summary': 'FIT2107 TESTING LECTURE',
                            'creator': {
                                'email': 'tsut0005@student.monash.edu',
                                'self': True},
                            'organizer': {
                                'email': 'tsut0005@student.monash.edu',
                                'self': True},
                            'start': {'dateTime': '2020-10-14T12:00:00+08:00'},
                            'end': {'dateTime': '2020-10-14T13:00:00+08:00'},
                            'recurringEventId': '197qogoh7r4rehiieelecnul98',
                            'originalStartTime': {'dateTime': '2020-10-14T12:00:00+08:00'},
                            'iCalUID': '197qogoh7r4rehiieelecnul98@google.com',
                            'sequence': 0,
                            'reminders': {'useDefault': True}
                            },
                           {'kind': 'calendar#event',
                            'etag': '"3204656707822000"',
                            'id': '6qilic69tedq4305c6dftvtblr',
                            'status': 'confirmed',
                            'htmlLink': 'https://www.google.com/calendar/event?eid=NnFpbGljNjl0ZWRxNDMwNWM2ZGZ0dnRibH'
                                        'IgdHN1dDAwMDVAc3R1ZGVudC5tb25hc2guZWR1',
                            'created': '2020-10-10T11:11:31.000Z',
                            'updated': '2020-10-10T11:11:31.229Z',
                            'summary': 'FIT2107 TESTING LECTURE 2',
                            'creator': {
                                'email': 'tsut0005@student.monash.edu',
                                'self': True},
                            'organizer': {
                                'email': 'tsut0005@student.monash.edu',
                                'self': True},
                            'start': {'dateTime': '2020-10-15T13:30:00+08:00'},
                            'end': {'dateTime': '2020-10-15T14:30:00+08:00'},
                            'iCalUID': '6qilic69tedq4305c6dftvtblr@google.com',
                            'sequence': 0,
                            'reminders': {'useDefault': False}
                            },
                           {'kind': 'calendar#event',
                            'etag': '"3204656707822000"',
                            'id': '6qilic69tedq4305c6dftvtblr',
                            'status': 'confirmed',
                            'htmlLink': 'https://www.google.com/calendar/event?eid=NnFpbGljNjl0ZWRxNDMwNWM2ZGZ0dnRibH'
                                        'IgdHN1dDAwMDVAc3R1ZGVudC5tb25hc2guZWR1',
                            'created': '2020-10-10T11:11:31.000Z',
                            'updated': '2020-10-10T11:11:31.229Z',
                            'summary': 'FIT2107 TESTING LECTURE 3',
                            'creator': {
                                'email': 'tsut0005@student.monash.edu',
                                'self': True},
                            'organizer': {
                                'email': 'tsut0005@student.monash.edu',
                                'self': True},
                            'start': {'dateTime': '2020-10-15T13:30:00+08:00'},
                            'end': {'dateTime': '2020-10-15T14:30:00+08:00'},
                            'iCalUID': '6qilic69tedq4305c6dftvtblr@google.com',
                            'sequence': 0,
                            'reminders': {'useDefault': False,
                                          "overrides": [
                                              {
                                                  "method": "email",
                                                  "minutes": 30
                                              },
                                          ]}
                            }
                       ]
                       }
        # setting up api
        mock_api.events.return_value.list.return_value.execute.return_value = past_events
        # Testing the function call
        returned_request = calendar.get_events_reminders_in_the_future(mock_api, time_now)
        self.assertEqual(returned_request, past_events)

    @patch('builtins.print')
    def test_delete_event_reminder_No_reminder(self, mock_print=None):
        """This test will test the functionality of delete events and reminders.
        Condition 1: No reminder (default =F, override =F)
        branches based on the preference of the user of whether they would like to delete the whole event
        or just the reminder"""
        mock_api = Mock()
        calendar = Calendar()
        event_id = '197qogoh7r4rehiieelecnul98_20201014T040000Z'

        # Test 1: There is no event reminder(default == false, override == none), user wants to delete the event
        event_no_reminder = {'kind': 'calendar#event',
                             'etag': '"3196377768156000"',
                             'id': '197qogoh7r4rehiieelecnul98_20201014T040000Z',
                             'status': 'confirmed',
                             'htmlLink': 'https://www.google.com/calendar/event?eid'
                                         '=MTk3cW9nb2g3cjRyZWhpaWVlbGVjbnVsOThfMjAyMDEwMTRUMDQwMDAwWiB0c3V0MDAwNUBzdHV'
                                         'kZW50Lm1vbmFzaC5lZHU',
                             'created': '2020-08-13T02:33:40.000Z',
                             'updated': '2020-08-23T13:21:24.078Z',
                             'summary': 'FIT2107 TESTING LECTURE',
                             'creator': {
                                 'email': 'tsut0005@student.monash.edu',
                                 'self': True},
                             'organizer': {
                                 'email': 'tsut0005@student.monash.edu',
                                 'self': True},
                             'start': {'dateTime': '2020-10-14T12:00:00+08:00'},
                             'end': {'dateTime': '2020-10-14T13:00:00+08:00'},
                             'recurringEventId': '197qogoh7r4rehiieelecnul98',
                             'originalStartTime': {'dateTime': '2020-10-14T12:00:00+08:00'},
                             'iCalUID': '197qogoh7r4rehiieelecnul98@google.com',
                             'sequence': 0,
                             'reminders': {'useDefault': False}
                             }
        mock_api.events.return_value.get.return_value.execute.return_value = event_no_reminder
        with patch('builtins.input', side_effect=['1']):
            calendar.delete_event_reminder(mock_api, event_id)
            mock_print.assert_called_with("Event deleted successfully")

        # Test 2: There is no event reminder (default == false, override == none), user does not want to delete the
        # event
        with patch('builtins.input', side_effect=['2']):
            calendar.delete_event_reminder(mock_api, event_id)
            mock_print.assert_called_with("Event is not deleted")

        # Test 3: There is no event reminder (default == false, override == none), user inputs invalid input
        # shows that there are two options, deleting an event and exiting but not deleting reminder
        # as there is already no reminder for this tested event
        with patch('builtins.input', side_effect=['3']):
            with self.assertRaises(ValueError):
                calendar.delete_event_reminder(mock_api, event_id)

    @patch('builtins.print')
    def test_delete_event_reminder_custom_reminder(self, mock_print=None):
        """This test will test the functionality of delete events and reminders when there are customised reminders
        Condition 2: custom reminder(default =F, override =T)
        branches based on the preference of the user of whether they would like to delete the whole event
        or just the reminder"""
        mock_api = Mock()
        calendar = Calendar()
        event_id = '197qogoh7r4rehiieelecnul98_20201014T040000Z'
        # Test 4: There is a customised reminder (default =F, override =T), user wants to delete the event
        event_reminder = {'kind': 'calendar#event',
                          'etag': '"3196377768156000"',
                          'id': '197qogoh7r4rehiieelecnul98_20201014T040000Z',
                          'status': 'confirmed',
                          'htmlLink': 'https://www.google.com/calendar/event?eid'
                                      '=MTk3cW9nb2g3cjRyZWhpaWVlbGVjbnVsOThfMjAyMDEwMTRUMDQwMDAwWiB0c3V0MDAwNUBzdHV'
                                      'kZW50Lm1vbmFzaC5lZHU',
                          'created': '2020-08-13T02:33:40.000Z',
                          'updated': '2020-08-23T13:21:24.078Z',
                          'summary': 'FIT2107 TESTING LECTURE',
                          'creator': {
                              'email': 'tsut0005@student.monash.edu',
                              'self': True},
                          'organizer': {
                              'email': 'tsut0005@student.monash.edu',
                              'self': True},
                          'start': {'dateTime': '2020-10-14T12:00:00+08:00'},
                          'end': {'dateTime': '2020-10-14T13:00:00+08:00'},
                          'recurringEventId': '197qogoh7r4rehiieelecnul98',
                          'originalStartTime': {'dateTime': '2020-10-14T12:00:00+08:00'},
                          'iCalUID': '197qogoh7r4rehiieelecnul98@google.com',
                          'sequence': 0,
                          'reminders': {'useDefault': False,
                                        "overrides": [
                                            {
                                                "method": "email",
                                                "minutes": 30
                                            },
                                        ]}
                          }
        mock_api.events.return_value.get.return_value.execute.return_value = event_reminder
        with patch('builtins.input', side_effect=['1']):
            calendar.delete_event_reminder(mock_api, event_id)
            mock_print.assert_called_with("Event deleted successfully")

        # Test 2: There is a customised reminder (default =F, override =T), user wants to delete the reminder
        with patch('builtins.input', side_effect=['2']):
            calendar.delete_event_reminder(mock_api, event_id)
            mock_print.assert_called_with("Reminder for the event is deleted successfully")

        # Test 3: There is a customised reminder (default =F, override =T), user wants to exit without deleting anything
        # Shows that there are three options when there is a reminder
        with patch('builtins.input', side_effect=['3']):
            calendar.delete_event_reminder(mock_api, event_id)
            mock_print.assert_called_with("No deleted elements")

        # Test 4: There is a customised reminder (default =F, override =T), user inputs invalid input
        with patch('builtins.input', side_effect=['4']):
            with self.assertRaises(ValueError):
                calendar.delete_event_reminder(mock_api, event_id)

    @patch('builtins.print')
    def test_delete_event_reminder_default_reminder(self, mock_print=None):
        """This test will test the functionality of delete events and reminders when there are default reminder
        Condition 3: custom reminder(default =T)
        branches based on the preference of the user of whether they would like to delete the whole event
        or just the reminder"""
        mock_api = Mock()
        calendar = Calendar()
        event_id = '197qogoh7r4rehiieelecnul98_20201014T040000Z'
        # Test 4: There is a customised reminder (default =F, override =T), user wants to delete the event
        event_reminder = {'kind': 'calendar#event',
                          'etag': '"3196377768156000"',
                          'id': '197qogoh7r4rehiieelecnul98_20201014T040000Z',
                          'status': 'confirmed',
                          'htmlLink': 'https://www.google.com/calendar/event?eid'
                                      '=MTk3cW9nb2g3cjRyZWhpaWVlbGVjbnVsOThfMjAyMDEwMTRUMDQwMDAwWiB0c3V0MDAwNUBzdHV'
                                      'kZW50Lm1vbmFzaC5lZHU',
                          'created': '2020-08-13T02:33:40.000Z',
                          'updated': '2020-08-23T13:21:24.078Z',
                          'summary': 'FIT2107 TESTING LECTURE',
                          'creator': {
                              'email': 'tsut0005@student.monash.edu',
                              'self': True},
                          'organizer': {
                              'email': 'tsut0005@student.monash.edu',
                              'self': True},
                          'start': {'dateTime': '2020-10-14T12:00:00+08:00'},
                          'end': {'dateTime': '2020-10-14T13:00:00+08:00'},
                          'recurringEventId': '197qogoh7r4rehiieelecnul98',
                          'originalStartTime': {'dateTime': '2020-10-14T12:00:00+08:00'},
                          'iCalUID': '197qogoh7r4rehiieelecnul98@google.com',
                          'sequence': 0,
                          'reminders': {'useDefault': True}
                          }
        mock_api.events.return_value.get.return_value.execute.return_value = event_reminder
        with patch('builtins.input', side_effect=['1']):
            calendar.delete_event_reminder(mock_api, event_id)
            mock_print.assert_called_with("Event deleted successfully")

        # Test 2: There is a customised reminder (default =F, override =T), user wants to delete the reminder
        with patch('builtins.input', side_effect=['2']):
            calendar.delete_event_reminder(mock_api, event_id)
            mock_print.assert_called_with("Reminder for the event is deleted successfully")

        # Test 3: There is a customised reminder (default =F, override =T), user wants to exit without deleting anything
        # Shows that there are three options when there is a reminder
        with patch('builtins.input', side_effect=['3']):
            calendar.delete_event_reminder(mock_api, event_id)
            mock_print.assert_called_with("No deleted elements")

        # Test 4: There is a customised reminder (default =F, override =T), user inputs invalid input
        with patch('builtins.input', side_effect=['4']):
            with self.assertRaises(ValueError):
                calendar.delete_event_reminder(mock_api, event_id)

    @patch('Calendar.Calendar.delete_event_reminder')
    @patch('builtins.print')
    def test_keyword(self, mock_print=None, mock_delete_event_reminder=None):
        """Testing the get_event_by_keyword function, according to MC/DC branching. For each
        combination that gives true, all the kind of reminders( default, not default, not existing) are tested
        """
        mock_delete_event_reminder.return_value = ""  # mocking delete function, which is called inside the function being tested
        calendar = Calendar()
        mock_calendar_api = MagicMock()  # mocked api
        time_now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
        event_list = {'accessRole': 'owner',
                      'defaultReminders': [{'method': 'popup', 'minutes': 10}],
                      'etag': '"p32scrp51quguo0g"',
                      'items': [{'created': '2020-10-07T04:26:42.000Z',
                                 'creator': {'email': 'tsut0001@student.monash.edu', 'self': True},
                                 'end': {'dateTime': '2020-01-01T01:00:00+08:00'},
                                 'etag': '"3204089717326000"',
                                 'htmlLink': 'https://www.google.com/calendar/event?eid=M25pbjFnOGhkcGRnN2RrcDZlbWZoMHFsczgganRhbjAxNjRAc3R1ZGVudC5tb25hc2guZWR1',
                                 'iCalUID': '3nin1g8hdpdg7dkp6emfh0qls8@google.com',
                                 'id': '3nin1g8hdpdg7dkp6emfh0qls8',
                                 'kind': 'calendar#event',
                                 'organizer': {'email': 'tsut0001@student.monash.edu', 'self': True},
                                 'reminders': {'useDefault': True},
                                 'sequence': 0,
                                 'start': {'dateTime': '2020-01-01T00:00:00+08:00'},
                                 'status': 'confirmed',
                                 'summary': 'Summary + default reminder',
                                 'updated': '2020-10-07T04:27:38.663Z'},
                                {'created': '2020-10-07T04:49:47.000Z',
                                 'creator': {'email': 'tsut0005@student.monash.edu', 'self': True},
                                 'end': {'dateTime': '2020-12-31T23:59:00+08:00'},
                                 'etag': '"3204092452294000"',
                                 'htmlLink': 'https://www.google.com/calendar/event?eid=N21ub2xtOG90bG9tYTBscWhwbGxnZW5xbnQganRhbjAxNjRAc3R1ZGVudC5tb25hc2guZWR1',
                                 'iCalUID': '7mnolm8otloma0lqhpllgenqnt@google.com',
                                 'id': '7mnolm8otloma0lqhpllgenqnt',
                                 'kind': 'calendar#event',
                                 'organizer': {'email': 'tsut0005@student.monash.edu', 'self': True},
                                 'reminders': {'useDefault': True},
                                 'sequence': 0,
                                 'start': {'dateTime': '2020-12-31T23:00:00+08:00'},
                                 'status': 'confirmed',
                                 'summary': 'Event, organizer, default',
                                 'updated': '2020-10-07T04:50:26.147Z'},
                                {'created': '2020-10-07T04:49:47.000Z',
                                 'creator': {'email': 'tsut1234@student.monash.edu', 'self': True},
                                 'end': {'dateTime': '2020-12-31T23:59:00+08:00'},
                                 'etag': '"3204092452294000"',
                                 'htmlLink': 'https://www.google.com/calendar/event?eid=N21ub2xtOG90bG9tYTBscWhwbGxnZW5xbnQganRhbjAxNjRAc3R1ZGVudC5tb25hc2guZWR1',
                                 'iCalUID': '7mnolm8otloma0lqhpllgenqnt@google.com',
                                 'id': '7mnolm8otloma0lqhpllgenqnt',
                                 'kind': 'calendar#event',
                                 'organizer': {'email': 'tsut1234@student.monash.edu', 'self': True},
                                 'reminders': {'useDefault': False,
                                               "overrides": [
                                                   {
                                                       "method": "email",
                                                       "minutes": 30
                                                   },
                                               ]},
                                 'sequence': 0,
                                 'start': {'dateTime': '2020-12-31T23:00:00+08:00'},
                                 'status': 'confirmed',
                                 'summary': 'Event, organizer, non-default',
                                 'updated': '2020-10-07T04:50:26.147Z'},
                                {'created': '2020-10-07T04:49:47.000Z',
                                 'creator': {'email': 'tsut0001@student.monash.edu', 'self': True},
                                 'end': {'dateTime': '2020-12-31T23:59:00+08:00'},
                                 'etag': '"3204092452294000"',
                                 'htmlLink': 'https://www.google.com/calendar/event?eid=N21ub2xtOG90bG9tYTBscWhwbGxnZW5xbnQganRhbjAxNjRAc3R1ZGVudC5tb25hc2guZWR1',
                                 'iCalUID': '7mnolm8otloma0lqhpllgenqnt@google.com',
                                 'id': '7mnolm8otloma0lqhpllgenqnt',
                                 'kind': 'calendar#event',
                                 'organizer': {'email': 'jsoh0003@student.monash.edu', 'self': True},
                                 'reminders': {'useDefault': False,
                                               "overrides": [
                                                   {
                                                       "method": "email",
                                                       "minutes": 30
                                                   },
                                               ]},
                                 'sequence': 0,
                                 'start': {'dateTime': '2020-12-31T23:00:00+08:00'},
                                 'status': 'confirmed',
                                 'summary': 'Summary + non default reminder',
                                 'updated': '2020-10-07T04:50:26.147Z'},
                                {'created': '2020-10-07T04:49:47.000Z',
                                 'creator': {'email': 'tsut1111@student.monash.edu', 'self': True},
                                 'end': {'dateTime': '2020-12-31T23:59:00+08:00'},
                                 'etag': '"3204092452294000"',
                                 'htmlLink': 'https://www.google.com/calendar/event?eid=N21ub2xtOG90bG9tYTBscWhwbGxnZW5xbnQganRhbjAxNjRAc3R1ZGVudC5tb25hc2guZWR1',
                                 'iCalUID': '7mnolm8otloma0lqhpllgenqnt@google.com',
                                 'id': '7mnolm8otloma0lqhpllgenqnt',
                                 'kind': 'calendar#event',
                                 'organizer': {'email': 'tsut1111@student.monash.edu', 'self': True},
                                 'sequence': 0,
                                 'start': {'dateTime': '2020-12-31T23:00:00+08:00'},
                                 'status': 'confirmed',
                                 'summary': 'Event, organizer, no reminder',
                                 'reminders': {'useDefault': False},
                                 'updated': '2020-10-07T04:50:26.147Z'
                                 },
                                {'created': '2020-10-07T04:49:47.000Z',
                                 'creator': {'email': 'tsut9999@student.monash.edu', 'self': True},
                                 'end': {'dateTime': '2020-12-31T23:59:00+08:00'},
                                 'etag': '"3204092452294000"',
                                 'htmlLink': 'https://www.google.com/calendar/event?eid=N21ub2xtOG90bG9tYTBscWhwbGxnZW5xbnQganRhbjAxNjRAc3R1ZGVudC5tb25hc2guZWR1',
                                 'iCalUID': '7mnolm8otloma0lqhpllgenqnt@google.com',
                                 'id': '7mnolm8otloma0lqhpllgenqnt',
                                 'kind': 'calendar#event',
                                 'organizer': {'email': 'tsut9999@student.monash.edu', 'self': True},
                                 'sequence': 0,
                                 'start': {'dateTime': '2020-12-31T23:00:00+08:00'},
                                 'status': 'confirmed',
                                 'summary': 'Summary + no reminder',
                                 'reminders': {'useDefault': False},
                                 'updated': '2020-10-07T04:50:26.147Z'
                                 }
                                ],
                      'kind': 'calendar#events',
                      'summary': 'tsut0005@student.monash.edu',
                      'timeZone': 'Asia/Kuala_Lumpur',
                      'updated': '2020-10-07T04:50:26.147Z'}
        # getting required information from mock
        mock_calendar_api.events.return_value.list.return_value.execute.return_value = event_list
        getter = calendar.get_events_reminders_in_the_future(mock_calendar_api,
                                                             time_now)  # gets the info about the events in the future
        events_in_two_years = getter.get('items', [])  # gets the events
        defaultReminder = getter.get('defaultReminders', [])  # gets the default reminder values
        events_in_five_years = calendar.get_past_events(mock_calendar_api, time_now).get('items', [])
        common_events = events_in_two_years + events_in_five_years

        # MC/DC testing:
        # conditions:
        # A = subtype ==””
        # B = event[type] == key_word
        # C = event[subtype][type] == key_word

        # test 1: F, F, F ->F (returns that no events are found)
        subtype = 'organizer'
        type = 'email'
        key_word = 'wrong key word'  # event with the following keyword does not exist
        calendar.get_event_by_keyword(mock_calendar_api, common_events, subtype, type, key_word, defaultReminder)
        mock_print.assert_called_with("No events found")

        # test 2: F, F, T -> T(returns the proper event, which is found in the mocked api)
        # default reminder
        subtype = 'organizer'
        type = 'email'
        key_word = 'tsut0005@student.monash.edu'  # proper keyword
        calendar.get_event_by_keyword(mock_calendar_api, common_events, subtype, type, key_word, defaultReminder)
        mock_print.assert_called_with('2020-12-31T23:00:00+08:00', 'Event, organizer, default',
                                      'Default reminder: popup, 10 minutes')
        # non-default reminder
        key_word = 'tsut1234@student.monash.edu'  # proper keyword
        calendar.get_event_by_keyword(mock_calendar_api, common_events, subtype, type, key_word, defaultReminder)
        mock_print.assert_called_with('2020-12-31T23:00:00+08:00', 'Event, organizer, non-default',
                                      'Reminder: email, 30 minutes')
        # no reminder
        key_word = 'tsut1111@student.monash.edu'  # event with the following keyword does not exist
        calendar.get_event_by_keyword(mock_calendar_api, common_events, subtype, type, key_word, defaultReminder)
        mock_print.assert_called_with('2020-12-31T23:00:00+08:00', 'Event, organizer, no reminder',
                                      'This event does not have a reminder')

        # test 3: F, T, F ->F (raises an assertion)
        subtype = 'organizer'
        type = 'summary'
        key_word = 'End year'  # event with the following keyword does not exist
        with self.assertRaises(KeyError):
            calendar.get_event_by_keyword(mock_calendar_api, common_events, subtype, type, key_word, defaultReminder)

        # test 4: T, F, F  ->F (returns that no events are found)
        subtype = ''
        type = 'summary'
        key_word = 'wrong key word'  # event with the following keyword does not exist
        calendar.get_event_by_keyword(mock_calendar_api, common_events, subtype, type, key_word, defaultReminder)
        mock_print.assert_called_with("No events found")

        # test 5: T, T, F
        #default reminder
        subtype = ''
        type = 'summary'
        key_word = 'Summary + default reminder'  # event with the following keyword does not exist
        calendar.get_event_by_keyword(mock_calendar_api, common_events, subtype, type, key_word, defaultReminder)
        mock_print.assert_called_with('2020-01-01T00:00:00+08:00', 'Summary + default reminder',
                                      'Default reminder: popup, 10 minutes')
        # event with manually created reminder
        key_word = 'Summary + non default reminder'  # event with the following keyword does not exist
        calendar.get_event_by_keyword(mock_calendar_api, common_events, subtype, type, key_word, defaultReminder)
        mock_print.assert_called_with('2020-12-31T23:00:00+08:00', 'Summary + non default reminder',
                                      'Reminder: email, 30 minutes')
        # no reminder
        key_word = 'Summary + no reminder'  # event with the following keyword does not exist
        calendar.get_event_by_keyword(mock_calendar_api, common_events, subtype, type, key_word, defaultReminder)
        mock_print.assert_called_with('2020-12-31T23:00:00+08:00', 'Summary + no reminder',
                                      'This event does not have a reminder')


    @patch('Calendar.Calendar.get_event_by_keyword')
    @patch('builtins.print')
    @patch('builtins.input', side_effect=['2020', '1', 'End Year'])
    def test_timeline_valid(self, mock_input, mock_print=None, mock_get_event_by_keyword=None):
        """Tests get_event_by_timeline with the valid inputs: 2020, 1 ( The whole year), End year."""
        mock_get_event_by_keyword.return_value = ""
        # mocking delete function, which is called inside the function being tested
        mock_calendar_api = MagicMock()
        calendar = Calendar()
        event_list = {'kind': 'calendar#events',
                      'etag': '"p32cd7ue3oenuo0g"',
                      'summary': 'tsut0005@student.monash.edu',
                      'updated': '2020-10-12T16:59:25.423Z',
                      'timeZone': 'Asia/Kuala_Lumpur',
                      'accessRole': 'owner',
                      'defaultReminders': [{'method': 'popup', 'minutes': 10}],
                      'items': [
                          {'kind': 'calendar#event',
                           'etag': '"3196377768156000"',
                           'id': '197qogoh7r4rehiieelecnul98_20201014T040000Z',
                           'status': 'confirmed',
                           'htmlLink': 'https://www.google.com/calendar/event?eid'
                                       '=MTk3cW9nb2g3cjRyZWhpaWVlbGVjbnVsOThfMjAyMDEwMTRUMDQwMDAwWiB0c3V0MDAwNUBzdHVkZW50Lm1vbmFzaC5lZHU',
                           'created': '2020-08-13T02:33:40.000Z',
                           'updated': '2020-08-23T13:21:24.078Z',
                           'summary': 'Event 25.05.20',
                           'creator': {
                               'email': 'tsut0005@student.monash.edu',
                               'self': True},
                           'organizer': {
                               'email': 'tsut0005@student.monash.edu',
                               'self': True},
                           'start': {'dateTime': '2020-05-25T12:00:00+08:00'},
                           'end': {'dateTime': '2020-10-14T13:00:00+08:00'},
                           'recurringEventId': '197qogoh7r4rehiieelecnul98',
                           'originalStartTime': {'dateTime': '2020-10-14T12:00:00+08:00'},
                           'iCalUID': '197qogoh7r4rehiieelecnul98@google.com',
                           'sequence': 0,
                           'reminders': {'useDefault': True}
                           },
                          {'kind': 'calendar#event',
                           'etag': '"3204656707822000"',
                           'id': '6qilic69tedq4305c6dftvtblr',
                           'status': 'confirmed',
                           'htmlLink': 'https://www.google.com/calendar/event?eid=NnFpbGljNjl0ZWRxNDMwNWM2ZGZ0dnRibHIgdHN1dDAwMDVAc3R1ZGVudC5tb25hc2guZWR1',
                           'created': '2020-10-10T11:11:31.000Z',
                           'updated': '2020-10-10T11:11:31.229Z',
                           'summary': 'Event 29.02.20',
                           'creator': {
                               'email': 'tsut0005@student.monash.edu',
                               'self': True},
                           'organizer': {
                               'email': 'tsut0005@student.monash.edu',
                               'self': True},
                           'start': {'dateTime': '2020-02-29T13:30:00+08:00'},
                           'end': {'dateTime': '2020-10-15T14:30:00+08:00'},
                           'iCalUID': '6qilic69tedq4305c6dftvtblr@google.com',
                           'sequence': 0,
                           'reminders': {'useDefault': False}
                           },
                          {'kind': 'calendar#event',
                           'etag': '"3204656707822000"',
                           'id': '6qilic69tedq4305c6dftvtblr',
                           'status': 'confirmed',
                           'htmlLink': 'https://www.google.com/calendar/event?eid=NnFpbGljNjl0ZWRxNDMwNWM2ZGZ0dnRibHIgdHN1dDAwMDVAc3R1ZGVudC5tb25hc2guZWR1',
                           'created': '2020-10-10T11:11:31.000Z',
                           'updated': '2020-10-10T11:11:31.229Z',
                           'summary': 'FIT2107 TESTING LECTURE 3',
                           'creator': {
                               'email': 'tsut0005@student.monash.edu',
                               'self': True},
                           'organizer': {
                               'email': 'tsut0005@student.monash.edu',
                               'self': True},
                           'start': {'dateTime': '2020-10-15T13:30:00+08:00'},
                           'end': {'dateTime': '2020-10-15T14:30:00+08:00'},
                           'iCalUID': '6qilic69tedq4305c6dftvtblr@google.com',
                           'sequence': 0,
                           'reminders': {'useDefault': False,
                                         "overrides": [
                                             {
                                                 "method": "email",
                                                 "minutes": 30
                                             },
                                         ]}
                           }
                      ]
                      }
        mock_calendar_api.events.return_value.list.return_value.execute.return_value = event_list
        calendar.get_event_by_timeline(mock_calendar_api)
        mock_print.assert_called_with(
            '2020-05-25T12:00:00+08:00 Event 25.05.20 Default reminder: popup, 10 minutes Organizer: '
            'tsut0005@student.monash.edu\n2020-02-29T13:30:00+08:00 Event 29.02.20 This event does not have a '
            'reminder Organizer: tsut0005@student.monash.edu\n2020-10-15T13:30:00+08:00 FIT2107 TESTING LECTURE 3 '
            'Reminder: email, 30 minutes Organizer: tsut0005@student.monash.edu\n')



    @patch('Calendar.Calendar.get_event_by_keyword')
    @patch('builtins.print')
    def test_timeline_invalid(self, mock_print=None, mock_get_event_by_keyword=None):
        """Tests get_event_by_timeline with the invalid inputs in any field"""
        mock_get_event_by_keyword.return_value = ""
        # mocking delete function, which is called inside the function being tested
        mock_calendar_api = MagicMock()
        calendar = Calendar()
        event_list = {'kind': 'calendar#events',
                      'etag': '"p32cd7ue3oenuo0g"',
                      'summary': 'tsut0005@student.monash.edu',
                      'updated': '2020-10-12T16:59:25.423Z',
                      'timeZone': 'Asia/Kuala_Lumpur',
                      'accessRole': 'owner',
                      'defaultReminders': [{'method': 'popup', 'minutes': 10}],
                      'items': [
                          {'kind': 'calendar#event',
                           'etag': '"3196377768156000"',
                           'id': '197qogoh7r4rehiieelecnul98_20201014T040000Z',
                           'status': 'confirmed',
                           'htmlLink': 'https://www.google.com/calendar/event?eid'
                                       '=MTk3cW9nb2g3cjRyZWhpaWVlbGVjbnVsOThfMjAyMDEwMTRUMDQwMDAwWiB0c3V0MDAwNUBzdHVkZW50Lm1vbmFzaC5lZHU',
                           'created': '2020-08-13T02:33:40.000Z',
                           'updated': '2020-08-23T13:21:24.078Z',
                           'summary': 'Event 25.05.20',
                           'creator': {
                               'email': 'tsut0005@student.monash.edu',
                               'self': True},
                           'organizer': {
                               'email': 'tsut0005@student.monash.edu',
                               'self': True},
                           'start': {'dateTime': '2020-05-25T12:00:00+08:00'},
                           'end': {'dateTime': '2020-10-14T13:00:00+08:00'},
                           'recurringEventId': '197qogoh7r4rehiieelecnul98',
                           'originalStartTime': {'dateTime': '2020-10-14T12:00:00+08:00'},
                           'iCalUID': '197qogoh7r4rehiieelecnul98@google.com',
                           'sequence': 0,
                           'reminders': {'useDefault': True}
                           },
                          {'kind': 'calendar#event',
                           'etag': '"3204656707822000"',
                           'id': '6qilic69tedq4305c6dftvtblr',
                           'status': 'confirmed',
                           'htmlLink': 'https://www.google.com/calendar/event?eid=NnFpbGljNjl0ZWRxNDMwNWM2ZGZ0dnRibHIgdHN1dDAwMDVAc3R1ZGVudC5tb25hc2guZWR1',
                           'created': '2020-10-10T11:11:31.000Z',
                           'updated': '2020-10-10T11:11:31.229Z',
                           'summary': 'Event 29.02.20',
                           'creator': {
                               'email': 'tsut0005@student.monash.edu',
                               'self': True},
                           'organizer': {
                               'email': 'tsut0005@student.monash.edu',
                               'self': True},
                           'start': {'dateTime': '2020-02-29T13:30:00+08:00'},
                           'end': {'dateTime': '2020-10-15T14:30:00+08:00'},
                           'iCalUID': '6qilic69tedq4305c6dftvtblr@google.com',
                           'sequence': 0,
                           'reminders': {'useDefault': False}
                           },
                          {'kind': 'calendar#event',
                           'etag': '"3204656707822000"',
                           'id': '6qilic69tedq4305c6dftvtblr',
                           'status': 'confirmed',
                           'htmlLink': 'https://www.google.com/calendar/event?eid=NnFpbGljNjl0ZWRxNDMwNWM2ZGZ0dnRibHIgdHN1dDAwMDVAc3R1ZGVudC5tb25hc2guZWR1',
                           'created': '2020-10-10T11:11:31.000Z',
                           'updated': '2020-10-10T11:11:31.229Z',
                           'summary': 'FIT2107 TESTING LECTURE 3',
                           'creator': {
                               'email': 'tsut0005@student.monash.edu',
                               'self': True},
                           'organizer': {
                               'email': 'tsut0005@student.monash.edu',
                               'self': True},
                           'start': {'dateTime': '2020-10-15T13:30:00+08:00'},
                           'end': {'dateTime': '2020-10-15T14:30:00+08:00'},
                           'iCalUID': '6qilic69tedq4305c6dftvtblr@google.com',
                           'sequence': 0,
                           'reminders': {'useDefault': False,
                                         "overrides": [
                                             {
                                                 "method": "email",
                                                 "minutes": 30
                                             },
                                         ]}
                           }
                      ]
                      }
        mock_calendar_api.events.return_value.list.return_value.execute.return_value = event_list
        # Test 1: inserting the wrong navigation value
        with patch('builtins.input', side_effect=['2020', '3']):
            with self.assertRaises(ValueError):
                calendar.get_event_by_timeline(mock_calendar_api)

        # Test 2: inserting the invalid month input
        # Part A: month <0
        with patch('builtins.input', side_effect=['2020', '2', '0']):
            with self.assertRaises(ValueError):
                calendar.get_event_by_timeline(mock_calendar_api)

        # Part B: month>12
        with patch('builtins.input', side_effect=['2020', '2', '13']):
            with self.assertRaises(ValueError):
                calendar.get_event_by_timeline(mock_calendar_api)

        # Test 3: Inserting invalid input to navigate between whole month or specific date
        # Only two choices are given hence a valid input will be greater than 2 or smaller than 1
        with patch('builtins.input', side_effect=['2020', '2', '1', '3']):
            with self.assertRaises(ValueError):
                calendar.get_event_by_timeline(mock_calendar_api)

        # Test 4: Inserting invalid date value
        # Part A: (date <0)
        with patch('builtins.input', side_effect=['2020', '2', '1', '2', '0']):
            with self.assertRaises(ValueError):
                calendar.get_event_by_timeline(mock_calendar_api)

        # Part B: date greater than 31 when it is jan/mar/may/jul/aug/oct/dec
        # Assumption that if the test pass with one month, it will pass with other months
        with patch('builtins.input', side_effect=['2020', '2', '10', '2', '32']):
            with self.assertRaises(ValueError):
                calendar.get_event_by_timeline(mock_calendar_api)

        # Part C: date greater than 30 when it is apr/jun/sep/nov
        # Assumption that if the test pass with one month, it will pass with other months
        with patch('builtins.input', side_effect=['2020', '2', '4', '2', '31']):
            with self.assertRaises(ValueError):
                calendar.get_event_by_timeline(mock_calendar_api)

        # Part C: date greater than 29 when it is feb (leap year)
        with patch('builtins.input', side_effect=['2020', '2', '2', '2', '30']):
            with self.assertRaises(ValueError):
                calendar.get_event_by_timeline(mock_calendar_api)

        # Part D: date greater than 28 when it is feb (not a leap year)
        with patch('builtins.input', side_effect=['2021', '2', '2', '2', '29']):
            with self.assertRaises(ValueError):
                calendar.get_event_by_timeline(mock_calendar_api)


    @patch('Calendar.Calendar.get_event_by_keyword')
    @patch('builtins.print')
    @patch('builtins.input', side_effect=['2020', '2', '1', '1', 'Event 10.01.20'])
    def test_timeline_31_day(self, mock_input, mock_print=None, mock_get_event_by_keyword=None):
        """Tests get_event_by_timeline with the valid inputs: 2020, 2 (Specific month), 1(January), 1(The whole month), Event 10.01.20.
        Tests if the function works properly with the month of 31 day"""
        mock_get_event_by_keyword.return_value = ""  # mocking delete function, which is called inside the function being tested
        mock_calendar_api = MagicMock()
        calendar = Calendar()
        event_list = {'kind': 'calendar#events',
                      'etag': '"p32cd7ue3oenuo0g"',
                      'summary': 'tsut0005@student.monash.edu',
                      'updated': '2020-10-12T16:59:25.423Z',
                      'timeZone': 'Asia/Kuala_Lumpur',
                      'accessRole': 'owner',
                      'defaultReminders': [{'method': 'popup', 'minutes': 10}],
                      'items': [
                          {'kind': 'calendar#event',
                           'etag': '"3204656707822000"',
                           'id': '6qilic69tedq4305c6dftvtblr',
                           'status': 'confirmed',
                           'htmlLink': 'https://www.google.com/calendar/event?eid=NnFpbGljNjl0ZWRxNDMwNWM2ZGZ0dnRibHIgdHN1dDAwMDVAc3R1ZGVudC5tb25hc2guZWR1',
                           'created': '2020-10-10T11:11:31.000Z',
                           'updated': '2020-10-10T11:11:31.229Z',
                           'summary': 'Event 10.01.20',
                           'creator': {
                               'email': 'tsut0005@student.monash.edu',
                               'self': True},
                           'organizer': {
                               'email': 'tsut0005@student.monash.edu',
                               'self': True},
                           'start': {'dateTime': '2020-01-10T13:30:00+08:00'},
                           'end': {'dateTime': '2020-01-15T14:30:00+08:00'},
                           'iCalUID': '6qilic69tedq4305c6dftvtblr@google.com',
                           'sequence': 0,
                           'reminders': {'useDefault': False,
                                         "overrides": [
                                             {
                                                 "method": "email",
                                                 "minutes": 30
                                             },
                                         ]}
                           }
                      ]
                      }
        mock_calendar_api.events.return_value.list.return_value.execute.return_value = event_list
        calendar.get_event_by_timeline(mock_calendar_api)
        mock_print.assert_called_with(
            '2020-01-10T13:30:00+08:00 Event 10.01.20 Reminder: email, 30 minutes Organizer: tsut0005@student.monash.edu\n')


    @patch('Calendar.Calendar.get_event_by_keyword')
    @patch('builtins.print')
    @patch('builtins.input', side_effect=['2020', '2', '2', '1', 'Event 10.02.2020'])
    def test_timeline_feb_leap(self, mock_input, mock_print=None, mock_get_event_by_keyword=None):
        """Tests get_event_by_timeline with the valid inputs: 2020( leap year), 2 (Specific month), 2(February), 1(The whole month), Event 10.02.20.
        Tests if the function works properly with the february in the leap year(29 days)"""
        mock_get_event_by_keyword.return_value = ""  # mocking delete function, which is called inside the function being tested
        mock_calendar_api = MagicMock()
        calendar = Calendar()
        event_list = {'kind': 'calendar#events',
                      'etag': '"p32cd7ue3oenuo0g"',
                      'summary': 'tsut0005@student.monash.edu',
                      'updated': '2020-10-12T16:59:25.423Z',
                      'timeZone': 'Asia/Kuala_Lumpur',
                      'accessRole': 'owner',
                      'defaultReminders': [{'method': 'popup', 'minutes': 10}],
                      'items': [
                          {'kind': 'calendar#event',
                           'etag': '"3204656707822000"',
                           'id': '6qilic69tedq4305c6dftvtblr',
                           'status': 'confirmed',
                           'htmlLink': 'https://www.google.com/calendar/event?eid=NnFpbGljNjl0ZWRxNDMwNWM2ZGZ0dnRibHIgdHN1dDAwMDVAc3R1ZGVudC5tb25hc2guZWR1',
                           'created': '2020-10-10T11:11:31.000Z',
                           'updated': '2020-10-10T11:11:31.229Z',
                           'summary': 'Event 10.02.2020',
                           'creator': {
                               'email': 'tsut0005@student.monash.edu',
                               'self': True},
                           'organizer': {
                               'email': 'tsut0005@student.monash.edu',
                               'self': True},
                           'start': {'dateTime': '2020-02-10T13:30:00+08:00'},
                           'end': {'dateTime': '2020-02-15T14:30:00+08:00'},
                           'iCalUID': '6qilic69tedq4305c6dftvtblr@google.com',
                           'sequence': 0,
                           'reminders': {'useDefault': False,
                                         "overrides": [
                                             {
                                                 "method": "email",
                                                 "minutes": 30
                                             },
                                         ]}
                           }
                      ]
                      }
        mock_calendar_api.events.return_value.list.return_value.execute.return_value = event_list
        calendar.get_event_by_timeline(mock_calendar_api)
        mock_print.assert_called_with(
            '2020-02-10T13:30:00+08:00 Event 10.02.2020 Reminder: email, 30 minutes Organizer: tsut0005@student.monash.edu\n')

    @patch('Calendar.Calendar.get_event_by_keyword')
    @patch('builtins.print')
    @patch('builtins.input', side_effect=['2021', '2', '2', '1', 'Event 10.02.2021'])
    def test_timeline_feb_not_leap(self, mock_input, mock_print=None, mock_get_event_by_keyword=None):
        """Tests get_event_by_timeline with the valid inputs: 2021(not leap year), 2 (Specific month), 2(February), 1(The whole month), Event 10.02.21.
        Tests if the function works properly with the february in the non-leap year(28 days)"""
        mock_get_event_by_keyword.return_value = ""  # mocking delete function, which is called inside the function being tested
        mock_calendar_api = MagicMock()
        calendar = Calendar()
        event_list = {'kind': 'calendar#events',
                      'etag': '"p32cd7ue3oenuo0g"',
                      'summary': 'tsut0005@student.monash.edu',
                      'updated': '2020-10-12T16:59:25.423Z',
                      'timeZone': 'Asia/Kuala_Lumpur',
                      'accessRole': 'owner',
                      'defaultReminders': [{'method': 'popup', 'minutes': 10}],
                      'items': [
                          {'kind': 'calendar#event',
                           'etag': '"3204656707822000"',
                           'id': '6qilic69tedq4305c6dftvtblr',
                           'status': 'confirmed',
                           'htmlLink': 'https://www.google.com/calendar/event?eid=NnFpbGljNjl0ZWRxNDMwNWM2ZGZ0dnRibHIgdHN1dDAwMDVAc3R1ZGVudC5tb25hc2guZWR1',
                           'created': '2020-10-10T11:11:31.000Z',
                           'updated': '2020-10-10T11:11:31.229Z',
                           'summary': 'Event 10.02.2021',
                           'creator': {
                               'email': 'tsut0005@student.monash.edu',
                               'self': True},
                           'organizer': {
                               'email': 'tsut0005@student.monash.edu',
                               'self': True},
                           'start': {'dateTime': '2021-02-10T13:30:00+08:00'},
                           'end': {'dateTime': '2021-02-15T14:30:00+08:00'},
                           'iCalUID': '6qilic69tedq4305c6dftvtblr@google.com',
                           'sequence': 0,
                           'reminders': {'useDefault': False,
                                         "overrides": [
                                             {
                                                 "method": "email",
                                                 "minutes": 30
                                             },
                                         ]}
                           }
                      ]
                      }
        mock_calendar_api.events.return_value.list.return_value.execute.return_value = event_list
        calendar.get_event_by_timeline(mock_calendar_api)
        mock_print.assert_called_with(
            '2021-02-10T13:30:00+08:00 Event 10.02.2021 Reminder: email, 30 minutes Organizer: tsut0005@student.monash.edu\n')


    @patch('Calendar.Calendar.get_event_by_keyword')
    @patch('builtins.print')
    @patch('builtins.input', side_effect=['2020', '2', '4', '1', 'Event 10.04.2020'])
    def test_timeline_30_days(self, mock_input, mock_print=None, mock_get_event_by_keyword=None):
        """Tests get_event_by_timeline with the valid inputs: 2020, 2 (Specific month), 4(April), 1(The whole month), Event 10.04.20.
        Tests if the function works properly with the month of 30 days"""
        mock_get_event_by_keyword.return_value = ""  # mocking delete function, which is called inside the function being tested
        mock_calendar_api = MagicMock()
        calendar = Calendar()
        event_list = {'kind': 'calendar#events',
                      'etag': '"p32cd7ue3oenuo0g"',
                      'summary': 'tsut0005@student.monash.edu',
                      'updated': '2020-10-12T16:59:25.423Z',
                      'timeZone': 'Asia/Kuala_Lumpur',
                      'accessRole': 'owner',
                      'defaultReminders': [{'method': 'popup', 'minutes': 10}],
                      'items': [
                          {'kind': 'calendar#event',
                           'etag': '"3204656707822000"',
                           'id': '6qilic69tedq4305c6dftvtblr',
                           'status': 'confirmed',
                           'htmlLink': 'https://www.google.com/calendar/event?eid=NnFpbGljNjl0ZWRxNDMwNWM2ZGZ0dnRibHIgdHN1dDAwMDVAc3R1ZGVudC5tb25hc2guZWR1',
                           'created': '2020-10-10T11:11:31.000Z',
                           'updated': '2020-10-10T11:11:31.229Z',
                           'summary': 'Event 10.04.2020',
                           'creator': {
                               'email': 'tsut0005@student.monash.edu',
                               'self': True},
                           'organizer': {
                               'email': 'tsut0005@student.monash.edu',
                               'self': True},
                           'start': {'dateTime': '2020-04-10T13:30:00+08:00'},
                           'end': {'dateTime': '2020-04-15T14:30:00+08:00'},
                           'iCalUID': '6qilic69tedq4305c6dftvtblr@google.com',
                           'sequence': 0,
                           'reminders': {'useDefault': False,
                                         "overrides": [
                                             {
                                                 "method": "email",
                                                 "minutes": 30
                                             },
                                         ]}
                           }
                      ]
                      }
        mock_calendar_api.events.return_value.list.return_value.execute.return_value = event_list
        calendar.get_event_by_timeline(mock_calendar_api)
        mock_print.assert_called_with(
            '2020-04-10T13:30:00+08:00 Event 10.04.2020 Reminder: email, 30 minutes Organizer: tsut0005@student.monash.edu\n')


    @patch('Calendar.Calendar.get_event_by_keyword')
    @patch('builtins.print')
    @patch('builtins.input', side_effect=['2020', '2', '1', '2', '15', 'Event 10.01.20'])
    def test_timeline_31day_specific_day(self, mock_input, mock_print=None, mock_get_event_by_keyword=None):
        """Tests get_event_by_timeline with the valid inputs: 2020, 2 (Specific month), 1(January), 2(Specific day),15, Event 10.01.20.
        Tests if the function works properly with the month of 31 day"""
        mock_get_event_by_keyword.return_value = ""  # mocking delete function, which is called inside the function being tested
        mock_calendar_api = MagicMock()
        calendar = Calendar()
        event_list = {'kind': 'calendar#events',
                      'etag': '"p32cd7ue3oenuo0g"',
                      'summary': 'tsut0005@student.monash.edu',
                      'updated': '2020-10-12T16:59:25.423Z',
                      'timeZone': 'Asia/Kuala_Lumpur',
                      'accessRole': 'owner',
                      'defaultReminders': [{'method': 'popup', 'minutes': 10}],
                      'items': [
                          {'kind': 'calendar#event',
                           'etag': '"3204656707822000"',
                           'id': '6qilic69tedq4305c6dftvtblr',
                           'status': 'confirmed',
                           'htmlLink': 'https://www.google.com/calendar/event?eid=NnFpbGljNjl0ZWRxNDMwNWM2ZGZ0dnRibHIgdHN1dDAwMDVAc3R1ZGVudC5tb25hc2guZWR1',
                           'created': '2020-10-10T11:11:31.000Z',
                           'updated': '2020-10-10T11:11:31.229Z',
                           'summary': 'Event 10.01.20',
                           'creator': {
                               'email': 'tsut0005@student.monash.edu',
                               'self': True},
                           'organizer': {
                               'email': 'tsut0005@student.monash.edu',
                               'self': True},
                           'start': {'dateTime': '2020-01-10T13:30:00+08:00'},
                           'end': {'dateTime': '2020-01-15T14:30:00+08:00'},
                           'iCalUID': '6qilic69tedq4305c6dftvtblr@google.com',
                           'sequence': 0,
                           'reminders': {'useDefault': False,
                                         "overrides": [
                                             {
                                                 "method": "email",
                                                 "minutes": 30
                                             },
                                         ]}
                           }
                      ]
                      }
        mock_calendar_api.events.return_value.list.return_value.execute.return_value = event_list
        calendar.get_event_by_timeline(mock_calendar_api)
        mock_print.assert_called_with(
            '2020-01-10T13:30:00+08:00 Event 10.01.20 Reminder: email, 30 minutes Organizer: tsut0005@student.monash.edu\n')


    @patch('Calendar.Calendar.get_event_by_keyword')
    @patch('builtins.print')
    @patch('builtins.input', side_effect=['2020', '2', '2', '2', '10', 'Event 10.02.20'])
    def test_timeline_feb_leap_specific_day(self, mock_input, mock_print=None, mock_get_event_by_keyword=None):
        """Tests get_event_by_timeline with the valid inputs: 2020(leap year), 2 (Specific month), 2(Feb), 2(Specific day),10, Event 10.02.20.
        Tests if the function works properly with the feb in the leap year"""
        mock_get_event_by_keyword.return_value = ""  # mocking delete function, which is called inside the function being tested
        mock_calendar_api = MagicMock()
        calendar = Calendar()
        event_list = {'kind': 'calendar#events',
                      'etag': '"p32cd7ue3oenuo0g"',
                      'summary': 'tsut0005@student.monash.edu',
                      'updated': '2020-10-12T16:59:25.423Z',
                      'timeZone': 'Asia/Kuala_Lumpur',
                      'accessRole': 'owner',
                      'defaultReminders': [{'method': 'popup', 'minutes': 10}],
                      'items': [
                          {'kind': 'calendar#event',
                           'etag': '"3204656707822000"',
                           'id': '6qilic69tedq4305c6dftvtblr',
                           'status': 'confirmed',
                           'htmlLink': 'https://www.google.com/calendar/event?eid=NnFpbGljNjl0ZWRxNDMwNWM2ZGZ0dnRibHIgdHN1dDAwMDVAc3R1ZGVudC5tb25hc2guZWR1',
                           'created': '2020-10-10T11:11:31.000Z',
                           'updated': '2020-10-10T11:11:31.229Z',
                           'summary': 'Event 10.02.20',
                           'creator': {
                               'email': 'tsut0005@student.monash.edu',
                               'self': True},
                           'organizer': {
                               'email': 'tsut0005@student.monash.edu',
                               'self': True},
                           'start': {'dateTime': '2020-02-10T13:30:00+08:00'},
                           'end': {'dateTime': '2020-02-15T14:30:00+08:00'},
                           'iCalUID': '6qilic69tedq4305c6dftvtblr@google.com',
                           'sequence': 0,
                           'reminders': {'useDefault': False,
                                         "overrides": [
                                             {
                                                 "method": "email",
                                                 "minutes": 30
                                             },
                                         ]}
                           }
                      ]
                      }
        mock_calendar_api.events.return_value.list.return_value.execute.return_value = event_list
        calendar.get_event_by_timeline(mock_calendar_api)
        mock_print.assert_called_with(
            '2020-02-10T13:30:00+08:00 Event 10.02.20 Reminder: email, 30 minutes Organizer: tsut0005@student.monash.edu\n')

    @patch('Calendar.Calendar.get_event_by_keyword')
    @patch('builtins.print')
    @patch('builtins.input', side_effect=['2021', '2', '2', '2', '10', 'Event 10.02.21'])
    def test_timeline_feb_not_leap_specific_day(self, mock_input, mock_print=None, mock_get_event_by_keyword=None):
        """Tests get_event_by_timeline with the valid inputs: 2021(non-leap year), 2 (Specific month), 2(Feb), 2(Specific day),10, Event 10.02.21.
        Tests if the function works properly with the feb in the non-leap year"""
        mock_get_event_by_keyword.return_value = ""  # mocking delete function, which is called inside the function being tested
        mock_calendar_api = MagicMock()
        calendar = Calendar()
        event_list = {'kind': 'calendar#events',
                      'etag': '"p32cd7ue3oenuo0g"',
                      'summary': 'tsut0005@student.monash.edu',
                      'updated': '2020-10-12T16:59:25.423Z',
                      'timeZone': 'Asia/Kuala_Lumpur',
                      'accessRole': 'owner',
                      'defaultReminders': [{'method': 'popup', 'minutes': 10}],
                      'items': [
                          {'kind': 'calendar#event',
                           'etag': '"3204656707822000"',
                           'id': '6qilic69tedq4305c6dftvtblr',
                           'status': 'confirmed',
                           'htmlLink': 'https://www.google.com/calendar/event?eid=NnFpbGljNjl0ZWRxNDMwNWM2ZGZ0dnRibHIgdHN1dDAwMDVAc3R1ZGVudC5tb25hc2guZWR1',
                           'created': '2020-10-10T11:11:31.000Z',
                           'updated': '2020-10-10T11:11:31.229Z',
                           'summary': 'Event 10.02.21',
                           'creator': {
                               'email': 'tsut0005@student.monash.edu',
                               'self': True},
                           'organizer': {
                               'email': 'tsut0005@student.monash.edu',
                               'self': True},
                           'start': {'dateTime': '2021-02-10T13:30:00+08:00'},
                           'end': {'dateTime': '2021-02-15T14:30:00+08:00'},
                           'iCalUID': '6qilic69tedq4305c6dftvtblr@google.com',
                           'sequence': 0,
                           'reminders': {'useDefault': False,
                                         "overrides": [
                                             {
                                                 "method": "email",
                                                 "minutes": 30
                                             },
                                         ]}
                           }
                      ]
                      }
        mock_calendar_api.events.return_value.list.return_value.execute.return_value = event_list
        calendar.get_event_by_timeline(mock_calendar_api)
        mock_print.assert_called_with(
            '2021-02-10T13:30:00+08:00 Event 10.02.21 Reminder: email, 30 minutes Organizer: tsut0005@student.monash.edu\n')

    @patch('Calendar.Calendar.get_event_by_keyword')
    @patch('builtins.print')
    @patch('builtins.input', side_effect=['2020', '2', '4', '2', '10', 'Event 10.04.20'])
    def test_timeline_30day_specific_day(self, mock_input, mock_print=None, mock_get_event_by_keyword=None):
        """Tests get_event_by_timeline with the valid inputs: 2020, 2 (Specific month), 4(April), 2(Specific day),10, Event 10.04.20.
        Tests if the function works properly with the month of 30 days"""
        mock_get_event_by_keyword.return_value = ""  # mocking delete function, which is called inside the function being tested
        mock_calendar_api = MagicMock()
        calendar = Calendar()
        event_list = {'kind': 'calendar#events',
                      'etag': '"p32cd7ue3oenuo0g"',
                      'summary': 'tsut0005@student.monash.edu',
                      'updated': '2020-10-12T16:59:25.423Z',
                      'timeZone': 'Asia/Kuala_Lumpur',
                      'accessRole': 'owner',
                      'defaultReminders': [{'method': 'popup', 'minutes': 10}],
                      'items': [
                          {'kind': 'calendar#event',
                           'etag': '"3204656707822000"',
                           'id': '6qilic69tedq4305c6dftvtblr',
                           'status': 'confirmed',
                           'htmlLink': 'https://www.google.com/calendar/event?eid=NnFpbGljNjl0ZWRxNDMwNWM2ZGZ0dnRibHIgdHN1dDAwMDVAc3R1ZGVudC5tb25hc2guZWR1',
                           'created': '2020-10-10T11:11:31.000Z',
                           'updated': '2020-10-10T11:11:31.229Z',
                           'summary': 'Event 10.04.20',
                           'creator': {
                               'email': 'tsut0005@student.monash.edu',
                               'self': True},
                           'organizer': {
                               'email': 'tsut0005@student.monash.edu',
                               'self': True},
                           'start': {'dateTime': '2020-04-10T13:30:00+08:00'},
                           'end': {'dateTime': '2020-04-15T14:30:00+08:00'},
                           'iCalUID': '6qilic69tedq4305c6dftvtblr@google.com',
                           'sequence': 0,
                           'reminders': {'useDefault': False,
                                         "overrides": [
                                             {
                                                 "method": "email",
                                                 "minutes": 30
                                             },
                                         ]}
                           }
                      ]
                      }
        mock_calendar_api.events.return_value.list.return_value.execute.return_value = event_list
        calendar.get_event_by_timeline(mock_calendar_api)
        mock_print.assert_called_with(
            '2020-04-10T13:30:00+08:00 Event 10.04.20 Reminder: email, 30 minutes Organizer: tsut0005@student.monash.edu\n')


    @patch('Calendar.Calendar.get_event_by_keyword')
    @patch('builtins.print')
    @patch('builtins.input', side_effect=['2020', '2', '4', '2', '10', 'Event 10.04.20'])
    def test_timeline_with_no_events(self, mock_input, mock_print=None, mock_get_event_by_keyword=None):
        """Tests get_event_by_timeline with the valid inputs but no events in the database"""
        mock_get_event_by_keyword.return_value = ""  # mocking delete function, which is called inside the function being tested
        mock_calendar_api = MagicMock()
        calendar = Calendar()
        event_list = {'kind': 'calendar#events',
                      'etag': '"p32cd7ue3oenuo0g"',
                      'summary': 'tsut0005@student.monash.edu',
                      'updated': '2020-10-12T16:59:25.423Z',
                      'timeZone': 'Asia/Kuala_Lumpur',
                      'accessRole': 'owner',
                      'defaultReminders': [{'method': 'popup', 'minutes': 10}],
                      'items': []
                      }
        mock_calendar_api.events.return_value.list.return_value.execute.return_value = event_list
        calendar.get_event_by_timeline(mock_calendar_api)
        mock_print.assert_called_with('No events found')

    @patch('builtins.print')
    def test_represent_reminders(self, mock_print):
        """Tests represent_events_reminders using branch coverage:
        When event = None (empty) or when there are events.
        If there are events if the event reminder exists, is default or not default"""
        calendar = Calendar()
        # Test 1: when there are event, with default reminder
        events_default = {'kind': 'calendar#events',
                          'etag': '"p32cd7ue3oenuo0g"',
                          'summary': 'tsut0005@student.monash.edu',
                          'updated': '2020-10-12T16:59:25.423Z',
                          'timeZone': 'Asia/Kuala_Lumpur',
                          'accessRole': 'owner',
                          'defaultReminders': [{'method': 'popup', 'minutes': 10}],
                          'items': [
                              {'kind': 'calendar#event',
                               'etag': '"3204656707822000"',
                               'id': '6qilic69tedq4305c6dftvtblr',
                               'status': 'confirmed',
                               'htmlLink': 'https://www.google.com/calendar/event?eid=NnFpbGljNjl0ZWRxNDMwNWM2ZGZ0dnRibH'
                                           'IgdHN1dDAwMDVAc3R1ZGVudC5tb25hc2guZWR1',
                               'created': '2020-10-10T11:11:31.000Z',
                               'updated': '2020-10-10T11:11:31.229Z',
                               'summary': 'FIT2107 TESTING LECTURE 2',
                               'creator': {
                                   'email': 'tsut0005@student.monash.edu',
                                   'self': True},
                               'organizer': {
                                   'email': 'tsut0005@student.monash.edu',
                                   'self': True},
                               'start': {'dateTime': '2020-10-15T13:30:00+08:00'},
                               'end': {'dateTime': '2020-10-15T14:30:00+08:00'},
                               'iCalUID': '6qilic69tedq4305c6dftvtblr@google.com',
                               'sequence': 0,
                               'reminders': {'useDefault': True}
                               }
                          ]
                          }

        # Don't change the formatting of this one as it will raise an error due to it being in a different formation
        # of the expected string
        output = "2020-10-15T13:30:00+08:00 FIT2107 TESTING LECTURE 2 Default reminder: popup, 10 minutes Organizer: tsut0005@student.monash.edu\n"
        self.assertEqual(calendar.represent_events_remiders(events_default), output)

        # Test 2 when there are event, with customised reminder
        events_customised = {'kind': 'calendar#events',
                             'etag': '"p32cd7ue3oenuo0g"',
                             'summary': 'tsut0005@student.monash.edu',
                             'updated': '2020-10-12T16:59:25.423Z',
                             'timeZone': 'Asia/Kuala_Lumpur',
                             'accessRole': 'owner',
                             'defaultReminders': [{'method': 'popup', 'minutes': 10}],
                             'items': [
                                 {'kind': 'calendar#event',
                                  'etag': '"3204656707822000"',
                                  'id': '6qilic69tedq4305c6dftvtblr',
                                  'status': 'confirmed',
                                  'htmlLink': 'https://www.google.com/calendar/event?eid'
                                              '=NnFpbGljNjl0ZWRxNDMwNWM2ZGZ0dnRibH '
                                              'IgdHN1dDAwMDVAc3R1ZGVudC5tb25hc2guZWR1',
                                  'created': '2020-10-10T11:11:31.000Z',
                                  'updated': '2020-10-10T11:11:31.229Z',
                                  'summary': 'FIT2107 TESTING LECTURE 2',
                                  'creator': {
                                      'email': 'tsut0005@student.monash.edu',
                                      'self': True},
                                  'organizer': {
                                      'email': 'tsut0005@student.monash.edu',
                                      'self': True},
                                  'start': {'dateTime': '2020-10-15T13:30:00+08:00'},
                                  'end': {'dateTime': '2020-10-15T14:30:00+08:00'},
                                  'iCalUID': '6qilic69tedq4305c6dftvtblr@google.com',
                                  'sequence': 0,
                                  'reminders': {'useDefault': False,
                                                "overrides": [
                                                    {
                                                        "method": "email",
                                                        "minutes": 30
                                                    },
                                                ]}
                                  }
                             ]
                             }

        # Don't change the formatting of this one as it will raise an error due to it being in a different formation
        # of the expected string
        output = "2020-10-15T13:30:00+08:00 FIT2107 TESTING LECTURE 2 Reminder: email, 30 minutes Organizer: tsut0005@student.monash.edu\n"
        self.assertEqual(calendar.represent_events_remiders(events_customised), output)

        # Test 3 when there are event, with no reminder
        events_no = {'kind': 'calendar#events',
                     'etag': '"p32cd7ue3oenuo0g"',
                     'summary': 'tsut0005@student.monash.edu',
                     'updated': '2020-10-12T16:59:25.423Z',
                     'timeZone': 'Asia/Kuala_Lumpur',
                     'accessRole': 'owner',
                     'defaultReminders': [{'method': 'popup', 'minutes': 10}],
                     'items': [
                         {'kind': 'calendar#event',
                          'etag': '"3204656707822000"',
                          'id': '6qilic69tedq4305c6dftvtblr',
                          'status': 'confirmed',
                          'htmlLink': 'https://www.google.com/calendar/event?eid=NnFpbGljNjl0ZWRxNDMwNWM2ZGZ0dnRibH'
                                      'IgdHN1dDAwMDVAc3R1ZGVudC5tb25hc2guZWR1',
                          'created': '2020-10-10T11:11:31.000Z',
                          'updated': '2020-10-10T11:11:31.229Z',
                          'summary': 'FIT2107 TESTING LECTURE 2',
                          'creator': {
                              'email': 'tsut0005@student.monash.edu',
                              'self': True},
                          'organizer': {
                              'email': 'tsut0005@student.monash.edu',
                              'self': True},
                          'start': {'dateTime': '2020-10-15T13:30:00+08:00'},
                          'end': {'dateTime': '2020-10-15T14:30:00+08:00'},
                          'iCalUID': '6qilic69tedq4305c6dftvtblr@google.com',
                          'sequence': 0,
                          'reminders': {'useDefault': False}
                          }
                     ]
                     }
        # Don't change the formatting of this one as it will raise an error due to it being in a different formation
        # of the expected string
        output = "2020-10-15T13:30:00+08:00 FIT2107 TESTING LECTURE 2 This event does not have a reminder Organizer: tsut0005@student.monash.edu\n"
        self.assertEqual(calendar.represent_events_remiders(events_no), output)

        # Test 4 when there are no events
        no_events = {'kind': 'calendar#events',
                     'etag': '"p32cd7ue3oenuo0g"',
                     'summary': 'tsut0005@student.monash.edu',
                     'updated': '2020-10-12T16:59:25.423Z',
                     'timeZone': 'Asia/Kuala_Lumpur',
                     'accessRole': 'owner',
                     'defaultReminders': [{'method': 'popup', 'minutes': 10}],
                     'items': []
                     }
        # Don't change the formatting of this one as it will raise an error due to it being in a different formation
        # of the expected string
        output = ""
        self.assertEqual(calendar.represent_events_remiders(no_events), output)
        mock_print.assert_called_with("No events found.")


# coverage run project\CalendarTest.py
def main():
    # Create the test suite from the cases above.
    suite = unittest.TestLoader().loadTestsFromTestCase(CalendarTest)
    # This will run the test suite.
    unittest.TextTestRunner(verbosity=2).run(suite)


main()
