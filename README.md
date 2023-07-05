
# UBC Course Availability Notifier

The Course Availability Notifier is a Python script that allows users to receive notifications via Discord when a specific course for the University of British Columbia, Vancouver becomes available. This script automates the process of checking the availability of a course and sends real-time updates to a designated Discord server.

Multiple courses can be monitored simultaneously. The script runs periodically, at an interval that can be customized, and a notification is sent whenever the course has seats available.



## Prerequisites

To use the Course Availability Notifier, ensure you have the following:

- Python: Make sure you have Python 3.6 or later installed on your system.
-  Discord Account: You will need a Discord account and a server with or channel where notifications will be sent.
- Dependencies: Install the required Python packages by running pip install for the several modules used.


## Deployment

- To deploy this project create a discord server to receive the notifications, navigate to integrations, add a webhook, and paste the webhook URL in main.py (line 12)

```bash
discord = Discord(url="<web hook url>")
```

- Add however many courses in the suitable format in the dictionary in the file main.py (line 17) 

```bash
  courses = {"Department Abbreviation": "Course Number"}
```

- The restriction for the course monitoring can be changed in main.py (line 42)

```bash
if term == "1" and type == "Lecture" and status == '':
```

