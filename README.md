Automated Form Fill Bot for Django CRUD Example
This bot streamlines the process of populating form fields in the Django CRUD example repository. It utilizes Selenium, a web testing library, to navigate through the web application, log in with provided credentials, and dynamically fill in form fields with data from an Excel file. The bot is designed to enhance efficiency during testing or data entry tasks.

Setup Instructions
Follow these steps to set up and run the bot:

Clone the Django CRUD Example Repository:

```bash

git clone https://github.com/MarcosStanquini/django-crud-example
```

Create a Virtual Environment:

```bash

python -m venv venv
```

Activate the Virtual Environment:

```bash
venv\Scripts\activate
```

On macOS/Linux:
```bash
source venv/bin/activate
```

Install Required Libraries:

```bash
pip install -r requirements.txt
```

Run the Django Server:

```bash

python manage.py runserver
```

Download the Form Fill Bot Repository:

```bash

git clone https://github.com/MarcosStanquini/form-fill-bot.git
```

Create a .env File:

Inside the form fill bot directory, create a .env file.
Add the following lines and replace placeholders with your actual credentials:
```env

USERNAME_TEST=your_username
PASSWORD=your_password
```

Run the Form Fill Bot:

```bash

python your_bot_script.py
```

Ensure that your bot script appropriately handles Excel data and interacts with the Django CRUD example web pages.

Note:

The bot script may modify information in the Excel file based on its logic.
Make sure to adapt the bot script if there are any changes in the structure of the Django CRUD example website.
