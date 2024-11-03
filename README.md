# Gandalf Bot

A web-based chatbot powered by the **Ollama LLM**, allowing users to interact with **Gandalf the Grey** from Middle-earth.

## Features

- **Interactive chat interface**: Engage with Gandalf in a natural dialogue.
- **Natural language responses**: Receive insightful answers as Gandalf would.
- **Chat history maintenance**: Keep track of the conversation context throughout the session.

## Prerequisites

Make sure you have the following installed:

- **Python**: 3.12 or later
- **pip**: Python package manager
- **Virtualenv** (optional but recommended): To create isolated Python environments
- **Django**: 4.2 or later
- Any other dependencies listed in `requirements.txt`

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/nadeemohc/gandalf_bot.git
cd gandalf_bot
```

### 2. Create a Virtual Environment (Optional)

It's a good practice to use a virtual environment for your projects.

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

### 3. Install Required Packages

Install the dependencies listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 4. Set Up the Database

Run the following commands to set up your database:

```bash
# Make migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate
```

### 5. Configure Static Files

You need to collect static files for the Django application:

```bash
python manage.py collectstatic
```

### 6. Run the Development Server

Start the development server:

```bash
python manage.py runserver
```

You can now access the application at **http://127.0.0.1:8000**.

### 7. Interact with the Gandalf Bot

Open your web browser and navigate to the provided URL. You can start chatting with Gandalf the Grey by typing your queries into the chat interface.

## Project Structure

```
gandalf_bot/
│
├── assistant/                # Contains the chat logic and views
├── static/                   # Static files (CSS, JS)
├── templates/                # HTML templates
├── .gitignore                # Git ignore file
├── requirements.txt          # List of dependencies
├── manage.py                 # Django management script
└── ...                       # Other Django files
```

## Acknowledgments

- **Ollama** for providing the LLM model
- **Django** for being an excellent web framework

## Video Presentation

Check out the video presentation of the Gandalf Bot on [YouTube: ](https://youtu.be/sCRTvr36ezk)

Feel free to modify any sections to better reflect your project and its specific requirements.
