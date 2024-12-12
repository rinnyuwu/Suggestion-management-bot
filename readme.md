# Suggestion management bot

This bot allows users to submit suggestions to a Discord server. Administrators can accept or decline these suggestions. Suggestions are displayed in an embed format, and their statuses are updated dynamically based on the admin's actions.

## Features
- Submit suggestions: Users can submit suggestions using the `/suggest` command.
- Accept suggestions: Administrators can accept suggestions using the `/accept` command.
- Decline suggestions: Administrators can decline suggestions using the `/decline` command.
- Suggestion statuses: Suggestions are marked as "approved", or "declined".
- Role-based access: Only users with specified admin roles can accept or decline suggestions.

![msedge_wpU2fNt3y8](https://github.com/user-attachments/assets/ee3c1da8-5dcd-430c-b4df-bcfb16b6f377)

## Requirements
- Programming Language: Python
- Required Libraries: disnake (for interacting with Discord's API), sqlite3 (for managing the database)

Install the required libraries using pip:
```
pip3 install disnake
```

## Setup
1. Create a bot on Discord:
- Go to the [Discord Developer Portal](https://discord.com/developers).
- Create a new application, then create a bot and obtain the bot token.
- Replace the placeholder `INSERT-TOKEN` in the code with your bot token.
2. Configure the bot:
- Set the `SUGGESTIONS_CHANNEL_ID` in `config/config.py` to the ID of the channel where suggestions will be sent.
- Set the `ADMIN_ROLES` in `config/config.py` to a list of role IDs that can accept or decline suggestions.
3. Install Dependencies:
- On your machine, ensure Python 3.8+ is installed. You can check this by running:
```
python3 --version
```
- Install pip if it's not installed:
```
sudo apt install python3-pip
```
- Install the required libraries with pip:
```
pip3 install disnake
```
4. Run the bot:
- You can run the bot using the following command:
```
python3 app.py
```
Make sure you are in the same directory as the `app.py` file or provide the full path to it.

## How to Use
- Deploy: Clone the repository and configure your bot with the bot token.
- Run: Launch the bot on your server.
- Interaction:
  - Users can submit suggestions using the `/suggest` command.
  - Administrators can accept suggestions using the `/accept` command.
  - Administrators can decline suggestions using the `/decline` command.

## Links
[Boosty developer](https://boosty.to/mao-mao)

[GitHub](https://github.com/rinnyuwu)

[Donation Alerts](https://www.donationalerts.com/r/rinnyuwu)
