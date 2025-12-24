Here is the full, non-truncated raw text for your `README.md`.

```markdown
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

```

---

## ⚡ Quick Start (Docker)

The easiest way to run this project is with Docker Compose. This will set up both the Python API and the PostgreSQL database automatically.

### 1. Prerequisites

Ensure you have [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed on your machine.

### 2. Build and Run

Open your terminal in the project directory and run:

```bash
docker-compose up --build

```

* The API will launch at `http://localhost:5000`.
* The Database will be accessible internally on port `5432`.
* **Note:** On the first run, `init_db.sql` will automatically create the tables and a default admin user.

---

## 🔗 API Endpoints

### 1. Authentication

#### Full Login

Validates credentials and returns user details.

* **URL:** `/login-full`
* **Method:** `POST`
* **Body:**
```json
{
  "user": "admin",
  "psw": "12345"
}

```


* **Response:**
```json
{
  "status": 1,
  "name": "System Admin",
  "role": "Admin"
}

```



#### Login Status

Checks if credentials are valid (boolean return).

* **URL:** `/login-status`
* **Method:** `POST`
* **Body:** `{"user": "...", "psw": "..."}`
* **Response:** `{"status": 1}` (or 0)

### 2. Attendance

#### Log Attendance

Records a timestamp.

* **URL:** `/attendance`
* **Method:** `POST`
* **Body:**
```json
{
  "user_id": "admin",
  "log_type": "IN",
  "log_time": "2023-10-27 09:00:00"
}

```



#### Get Records

Fetch records for a specific period.

* **URL:** `/attendance/<user_id>/<period>`
* **Method:** `GET`
* **Params:**
* `period`: `day`, `week`, or `month`
* `?date`: (Optional) Target date in `YYYY-MM-DD` format. Defaults to today.


* **Example:** `GET /attendance/admin/week?date=2023-10-27`
* **Response:**
```json
[
  {
    "id": 1,
    "log_type": "IN",
    "log_time": "2023-10-27T09:00:00"
  }
]

```



---

## 🧪 Testing

The database comes seeded with one default user for testing purposes:

* **User ID:** `admin`
* **Password:** `12345`

You can use **Postman**, **Insomnia**, or **cURL** to test the endpoints.

**Example cURL request:**

```bash
curl -X POST http://localhost:5000/login-full \
   -H "Content-Type: application/json" \
   -d '{"user": "admin", "psw": "12345"}'

```

---

## 🛡 Security Notes

1. **Environment Variables:** In `docker-compose.yml`, the database password is visible. For production, use a `.env` file that is **not** committed to version control.
2. **SQL Injection:** The code uses parameterized queries (`%s`), which protects against SQL injection attacks.

```

### Would you like the raw text for the `.gitignore` or `init_db.sql` files next?

```