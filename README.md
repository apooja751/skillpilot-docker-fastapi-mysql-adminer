# SkillPilot Task 3: Multi-Container Development Environment

## Aim

Build a multi-container development environment using FastAPI, MySQL, Adminer, Docker, and Docker Compose.

## Technologies Used

- Python 3.12
- FastAPI
- MySQL 8.4
- Adminer
- Docker
- Docker Compose

## Architecture

- **FastAPI:** Provides REST API endpoints on port 8000.
- **MySQL:** Stores application data using persistent Docker storage.
- **Adminer:** Provides a browser-based database administration interface on port 8080.
- **Docker Compose:** Defines and manages the application services.

## Project Files

```text
skillpilot-docker-fastapi-mysql-adminer/
├── .env.example
├── .gitignore
├── Dockerfile
├── docker-compose.yml
├── main.py
├── requirements.txt
└── README.md
```

The `.env` file contains local environment variables and must not be committed to GitHub.

## Prerequisites

- GitHub Codespaces or a computer with Docker installed
- Docker Compose
- A web browser

## Environment Configuration

Create a local `.env` file using `.env.example` as a template.

Set the following variables in `.env` with your own secure passwords:

```env
DB_NAME=skillpilot_db
DB_USER=appuser
DB_PASSWORD=your_secure_app_password
DB_ROOT_PASSWORD=your_secure_root_password
```

Do not commit `.env` or real credentials to GitHub.

## Running the Application

Build the application image and start the services:

```bash
docker compose up --build -d
```

Check the service status:

```bash
docker compose ps
```

View the logs:

```bash
docker compose logs
```

Stop the services:

```bash
docker compose down
```

To remove the containers while preserving the database volume, use `docker compose down` without the `-v` option.

## API Endpoints

| Endpoint | Purpose |
|---|---|
| `/` | Displays the application welcome response |
| `/health` | Checks API health |
| `/db-test` | Tests the database connection |

In GitHub Codespaces, open port 8000 using the forwarded-port URL.

Append `/health` or `/db-test` to that URL to test the respective endpoint.

The database test should be considered successful only when the API confirms a successful MySQL connection.

## Adminer Database Access

Open port 8080 through the Codespaces forwarded ports.

Use these settings:

- **System:** MySQL / MariaDB
- **Server:** `db`
- **Username:** The value of `DB_USER` in `.env`
- **Password:** The value of `DB_PASSWORD` in `.env`
- **Database:** The value of `DB_NAME` in `.env`

Do not include actual passwords in this README.

## Verification

The FastAPI welcome endpoint and health endpoint returned successful responses during testing. MySQL was reported as healthy, and the Adminer container was running.

The complete database connection and combined Docker Compose deployment require final verification.

## Result

A development environment was configured with FastAPI, MySQL, and Adminer using Docker Compose. The API endpoints were tested, and the database and administration services were started.

## Conclusion

This task demonstrates how to organize an application into multiple containers, configure environment variables, use persistent database storage, and manage services with Docker Compose.
