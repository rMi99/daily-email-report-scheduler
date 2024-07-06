# Daily Email Report Scheduler

This project automates the sending of daily email reports using a Flask web interface. Users can configure their email settings and schedule emails to be sent at a specific time each day.

## Features

- Web interface to configure email settings
- Schedule daily emails
- Uses Flask for the web interface
- Utilizes `smtplib` for sending emails
- `schedule` library for scheduling tasks

## Prerequisites

- Python 3.12 or higher
- pip

## Setup

### Step 1: Clone the Repository

Clone this repository to your local machine:

```bash
git clone https://github.com/rmi99/daily-email-report-scheduler.git
cd daily-email-report-scheduler

cp .env.example .env

