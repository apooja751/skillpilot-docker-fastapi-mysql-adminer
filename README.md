
# SkillPilot Task 3: Multi-Container Development Environment

## Aim
Build a multi-container development environment using FastAPI, MySQL, Adminer, and Docker Compose.

## Technologies Used
- Python 3.12
- FastAPI
- MySQL 8.4
- Adminer
- Docker
- Docker Compose

## Architecture
- **FastAPI:** Provides the REST API on port 8000.
- **MySQL:** Stores application data in a persistent Docker volume.
- **Adminer:** Provides a browser-based database management interface on port 8080.
- **Docker Compose:** Defines and manages all three services.

## Project Files
- `main.py` — FastAPI application and database connectivity test.
- `requirements.txt` — Python dependencies.
- `Dockerfile` — Builds the FastAPI image.
- `docker-compose.yml` — Configures the three services.
- `.env.example` — Documents required environment variables.
- `.gitignore` — Excludes environment secrets and temporary files.

## Prerequisites
- Docker Desktop with Docker Engine running
- Docker Compose

## Setup Instructions

1. Clone this repository:
   ```bash
   git clone <YOUR_REPOSITORY_URL>
   cd skillpilot-task3-fastapi-mysql-adminer
   ```

2. Create a local environment file:
   ```bash
   cp .env.example .env
   ```

3. Edit `.env` and replace the example passwords with strong local passwords.

4. Start the services:
   ```bash
   docker compose up --build -d
   ```

5. Check service status:
   ```bash
   docker compose ps
   ```

## Verification

- API home: http://localhost:8000/
- API health: http://localhost:8000/health
- Database connectivity: http://localhost:8000/db-test
- Interactive API documentation: http://localhost:8000/docs
- Adminer: http://localhost:8080

For Adminer, use:
- System: MySQL
- Server: `db`
- Username: the value of `DB_USER` in `.env`
- Password: the value of `DB_PASSWORD` in `.env`
- Database: the value of `DB_NAME` in `.env`

## Persistent Storage
MySQL data is stored in the named Docker volume `mysql_data`, so it survives normal container recreation.

## Stop the Environment
```bash
docker compose down
```

To also delete the database volume and its data:
```bash
docker compose down -v
```

**Warning:** The second command permanently deletes the project's stored database data.

## Result
The project is configured to run FastAPI, MySQL, and Adminer as a multi-container environment. Successful execution and database connectivity must be verified after starting the Docker services.
