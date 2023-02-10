# ADM-Reminder-Bot

This bot utilizes Google API to connect to a GSheet containing PT appointment information for the dancers of Atlanta Ballet, to automatically send appointment reminder emails on the day before and the day of the appointment.

## Description

The script is hosted on [Python Anywhere](https://www.pythonanywhere.com/), where the built-in task scheduler functionality executes the main.py script at 17:00 UTC every day. There are a few resources not committed to this repo - namely the authentication token files used to access [Google API](https://cloud.google.com/apis) endpoints and a dict of emails for the appointment holders.

Future plans include:
* Admin management functions
* Error handling
    * Approximate string matching to handle appointment holder names when they are misspelled in the PT sign-up sheet.
    * Saving a list of emails and messages to send in case of HTTP errors when connecting to building API service
* Full-time monitoring of PT sign-up sheet to allow:
    * Sending of emails to appointment holders who create their appointments after the task's scheduled runtime
    * Cancellation of email sending for those who have cancelled their appointments
    * Would likely require migration to a paid service which would allow for regular scheduled runs of individual scripts or 'always-running' functionality to allow for event-listening.
* Creation of a web app to allow for viewing of a selection of the sheet or a summary of an individual's statistics with identity verification

### Dependencies

* See [requirements.txt](https://github.com/thomas-davidoff/ADM-Reminder-Bot/blob/master/requirements.txt) file.

## Version History

* v1.1.1
    * Added ability to run main.py script from full path without having to change working directory. [See commit change](https://github.com/thomas-davidoff/ADM-Reminder-Bot/tree/v1.1.1)
* v1.1.0
    * Bug fixes; first working version. [See commit change](https://github.com/thomas-davidoff/ADM-Reminder-Bot/tree/v1.1.0)
* v1.0.0 > v1.0.15
    * Initial Release - added relevant files individually

## License

This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/thomas-davidoff/ADM-Reminder-Bot/blob/master/LICENSE.md) file for details

## Acknowledgments

* [Python Anywhere](https://pythonanywhere.com)
* [Google API](https://cloud.google.com/apis)
