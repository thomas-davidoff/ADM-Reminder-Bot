# ADM-Reminder-Bot

This bot connects to a Google Sheet, managed by the Atlanta Ballet medical staff, containing appointment information for the dancers, 
and sends automated email reminders to those dancers at a specific time every day.

## Description

The script is hosted on [Python Anywhere](https://www.pythonanywhere.com/), where there are a few additional resources not committed 
to this repo, including recipient emails, authentication tokens, and credentials for accessing Google's API.

I initially planned to use Github's VCS with PythonAnywhere, but they don't make it particularly easy. I can create a git repo within PythonAnywhere
but as far as I know I need to create it as a web app so I can use webhooks to send requests to GH.

## Getting Started

### Dependencies

* Python 3.9
* Check requirements.txt for full list of dependencies.


## Version History

* v1.1.1
    * Added ability to run main.py script from full path without having to change working directory
    * See [commit change](https://github.com/thomas-davidoff/ADM-Reminder-Bot/tree/v1.1.1)
* v1.1.0
    * Bug fixes; first working version
    * See [commit change](https://github.com/thomas-davidoff/ADM-Reminder-Bot/tree/v1.1.0)
* v1.0.0 > v1.0.15
    * Initial Release - added relevant files individually

## License

This project is licensed under the [MIT] License - see the LICENSE.md file for details

## Acknowledgments

* [Python Anywhere](https://pythonanywhere.com)
