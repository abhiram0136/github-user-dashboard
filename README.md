# GitHub User Analytics Dashboard

## Overview

A Streamlit-based dashboard that fetches GitHub user information using the GitHub API, processes the data, and stores it in PostgreSQL.

## Tech Stack

* Python
* Streamlit
* Pandas
* Requests
* PostgreSQL
* Git & GitHub

## Architecture

```text
GitHub API
     ↓
requests.get()
     ↓
JSON Response
     ↓
Pandas
     ↓
PostgreSQL
     ↓
Streamlit Dashboard
```

## Features

* Fetch GitHub user details
* Display profile image
* Show followers, following, and repositories
* Process API JSON data
* Store user data in PostgreSQL
* Interactive Streamlit dashboard

## Project Structure

```text
github-user-dashboard/
│
├── app.py
├── api.py
├── database.py
├── requirements.txt
└── README.md
```

## Run Project

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Author

Abhiram
