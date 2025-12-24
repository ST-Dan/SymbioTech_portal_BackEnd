# Symbiotech Attendance API

A lightweight, Dockerized Flask API designed for managing user authentication and tracking employee attendance logs. This project uses PostgreSQL for data persistence and is configured for easy deployment using Docker Compose.

## 🚀 Features

* **User Authentication:** Validate user credentials and retrieve user roles.
* **Attendance Logging:** Record `IN` and `OUT` timestamps for employees.
* **Reporting:** Retrieve attendance records filtered by day, week, or month.
* **Docker Ready:** Fully containerized application and database environment.

## 🛠 Tech Stack

* **Language:** Python 3.11
* **Framework:** Flask
* **Database:** PostgreSQL 15
* **Driver:** Psycopg2 (Binary)
* **Containerization:** Docker & Docker Compose

---

## 📂 Project Structure

```text
├── app.py               # Main Flask application logic
├── Dockerfile           # Python/Flask container configuration
├── docker-compose.yml   # Orchestrates API and Database containers
├── requirements.txt     # Python dependencies
├── .env                 # Environment variables (Database URL)
├── init_db.sql          # SQL script to initialize tables and dummy data
└── README.md            # Project documentation