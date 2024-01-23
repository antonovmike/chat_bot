# Chat Bot

## Description

Chat Bot is a Python project that allows you to create and run a Telegram bot using the aiogram library. 

## Installation

To install and run this project, you need to have Python 3.7 or higher and pip installed on your system. Then follow these steps:

• Clone this repository to your local machine.

• Create and activate a virtual environment.

• Install the required dependencies using `pip install -r requirements.txt`.

• Create a Telegram bot using BotFather and get your API token.

• Create a `.env` file in the root directory of the project and add your API token as `TOKEN=<your_token>`.

• Add your ChatGPT key to the `.env` file as 'GPT=<your_key>'.

• Run the `main.py` file using `python3 main.py`.


## Database Setup
This project uses PostgreSQL 14.10 as the database for storing and retrieving chat data. The database name is "test_bot" and it consists of the following tables:

Table `users` contains the information of the users who interact with the chat bot: id, telegram_id, username, first_name, last_name, registration_date.

Table `report` contains the information of the user's prompts and neural network's responses such as: id, user_message, gpt_message, gpt_response_time, message_date_time.

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
to install dependencies from the `requirements.txt` file. Or you can use 
```bash
pip install poetry
poetry install
```
to install all the dependencies from the `pyproject.toml` file.

6. Migrate the database to the latest version of PostgreSQL. Follow these steps:

Install the latest version of PostgreSQL on your machine or use a cloud service provider. 
Install the `pg_dump` and `pg_restore` tools, which are used to export and import the database data.
Export the data from the current database using the `pg_dump` tool. You can use the following command:
```bash
pg_dump -U postgres -W -F custom -d chat_bot -f chat_bot.dump
```
This command will create a file called `chat_bot.dump` that contains the data from the chat_bot database in a custom format.

Import the data into the new database using the `pg_restore` tool. You can use the following command:
```bash
pg_restore -U postgres -W -F custom -d chat_bot -c chat_bot.dump
```
This command will create a new database called `chat_bot` with the same structure and data as the old one, but using the latest version of PostgreSQL. The `-c` option will drop any existing objects in the new database before restoring them.

Verify that the migration was successful by checking the version and the data of the new database. You can use the following commands:
```bash
psql -U postgres -W -d chat_bot -c "SELECT version();"
```
This command will show you the version of the PostgreSQL server that the new database is running on.
```bash
psql -U postgres -W -d chat_bot -c "\dt"
```
This command will show you the tables in the new database.
```bash
psql -U postgres -W -d chat_bot -c "SELECT * FROM users;"
```
This command will show you the data in the users table. You can replace users with any other table name to see the data in that table.

7. To connect to the database from your code, you need to provide the connection details and credentials in the `.env` file. 
Add your DATA_BASE address to the `.env` file as `DATA_BASE=DATA_BASE=postgresql://<db_name>:<db_passward>@localhost/test_bot`.

## Usage

Once you run the `main.py` file, your bot will be ready to receive and send messages on Telegram. You can test it by opening a chat with your bot and typing `/start` to see the welcome message. Then you can type your question to ChatGPT.

![chat_bot](https://raw.githubusercontent.com/antonovmike/chat_bot/main/screenshot.png)
