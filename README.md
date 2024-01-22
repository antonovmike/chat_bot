# Chat Bot

## Description

Chat Bot is a Python project that allows you to create and run a Telegram bot using the aiogram library. 

## Installation

To install and run this project, you need to have Python 3.7 or higher and pip installed on your system. Then follow these steps:

•  Clone this repository to your local machine.

•  Create and activate a virtual environment.

•  Install the required dependencies using `pip install -r requirements.txt`.

•  Create a Telegram bot using BotFather and get your API token.

•  Create a `.env` file in the root directory of the project and add your API token as `TOKEN=<your_token>`.

•  Add your ChatGPT key to the `.env` file as 'GPT=<your_key>'.

•  Run the `main.py` file using `python3 main.py`.


## Database Setup
This project uses PostgreSQL 14.10 as the database for storing and retrieving chat data. The database name is "test_bot" and it consists of the following tables:

users
id | telegram_id | username | first_name | last_name | registration_date

report
id | user_message | gpt_message | gpt_response_time | message_date_time

To set up the database, you need to follow these steps:

1. Install type and version of database on your machine or use a cloud service provider.
2. Create a user and a password for accessing the database. You can use the following commands: 
```bash
sudo su postgres
psql
```
```sql
ALTER ROLE postgres WITH PASSWORD '123';
```
3. Create the database:
```sql
CREATE DATABASE test_bot;
```
If the tables were not created automatically when the program was started, use the following commands:
```sql
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    telegram_id TEXT,
    username TEXT,
    first_name TEXT,
    last_name TEXT,
    registration_date DATETIME
);
CREATE TABLE IF NOT EXISTS report (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_message TEXT,
    gpt_message TEXT,
    gpt_response_time TEXT,
    message_date_time DATETIME
);
```
4. Populate the database with some sample data using the provided script:
```sql
INSERT INTO users VALUES (NULL, ?, ?, ?, ?), ("100000000", "username", "first_name", "last_name", "2024-01-02 11:22:33.445566");
INSERT INTO report VALUES (NULL, ?, ?, ?, ?), ("some user message", "some gpt response", "0:00:04.050607", "2024-01-02 12:34:56.778899");
```
5. To install all the dependencies file you can use the following command: 
```bash
pip install -r requirements.txt
```
to install dependencies from the `requirements.txt`  file. Or
```bash
poetry install
```
to install all the dependencies from the `pyproject.toml` file.

6. To connect to the database from your code, you need to provide the connection details and credentials in the `.env` file. 
Add your DATA_BASE address to the `.env` file as 'DATA_BASE=DATA_BASE=postgresql://<db_name>:<db_passward>@localhost/test_bot'.

## Usage

Once you run the `main.py` file, your bot will be ready to receive and send messages on Telegram. You can test it by opening a chat with your bot and typing `/start` to see the welcome message. Then you can type your question to ChatGPT.

![chat_bot](https://raw.githubusercontent.com/antonovmike/chat_bot/main/screenshot.png)