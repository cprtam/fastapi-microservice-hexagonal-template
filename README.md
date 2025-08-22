# FastAPI Microservice Hexagonal Template 🚀

Boilerplate for building scalable, maintainable, and decoupled microservices using FastAPI and hexagonal architecture (Ports & Adapters).
Includes preconfigured PostgreSQL, SQLModel, Alembic, Docker, CORS, and Pytest support — everything you need to kickstart production-ready APIs.

## 🛠️ Technologies

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)[![SQLModel](https://img.shields.io/badge/SQLModel-6DB33F?style=for-the-badge&logo=sqlalchemy&logoColor=white)](https://sqlmodel.tiangolo.com/)[![Alembic](https://img.shields.io/badge/Alembic-4B8BBE?style=for-the-badge&logo=sqlalchemy&logoColor=white)](https://alembic.sqlalchemy.org/)[![Pytest](https://img.shields.io/badge/Pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)](https://docs.pytest.org/)[![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)[![Microservices](https://img.shields.io/badge/Microservices-0052CC?style=for-the-badge&logo=microgen&logoColor=white)](https://microservices.io/)[![Hexagonal Architecture](https://img.shields.io/badge/Hexagonal%20Architecture-6C3483?style=for-the-badge&logo=hexo&logoColor=white)](https://alistair.cockburn.us/hexagonal-architecture/)

## 📂 Project Structure

```
fastapi-microservice-hexagonal-template/
│
├── app/
│   ├── application/           # Use cases and orchestration of the business logic
│   ├── domain/                # Domain entities, repositories, and domain services
│   ├── infrastructure/        # Adapters and external implementations (DB, integrations, etc.)
│   │   └── db/                # Database configuration and connection
│   │       ├── alembic/       # Database migrations managed by Alembic
│   │       └── database.py    # Database engine and session configuration
│   ├── interfaces/            # Entry points: API routers, controllers, CLI, events
│   ├── config.py              # Global application configuration (Pydantic settings, environment variables)
│   └── main.py                # Main entrypoint of the FastAPI application
│
├── tests/                     # Unit and integration tests
│   ├── application/           # Tests for use cases
│   ├── domain/                # Tests for domain entities, repositories, and services
│   ├── infrastructure/        # Tests for infrastructure components (DB, integrations, etc.)
│   ├── interface/             # Tests for controllers, routers, and API endpoints
│   └── conftest.py            # Global fixtures for pytest
│
├── .env.example               # Example environment variables file
├── alembic.ini                # Global Alembic configuration file
├── docker-compose.yml         # Docker Compose setup for app + PostgreSQL
├── Dockerfile                 # Base Docker image for the FastAPI application
├── entrypoint.sh              # Startup script for Docker container
├── pytest.ini                 # Pytest configuration file
├── requirements.txt           # Project dependencies
└── README.md                  # Project documentation
```

---

## 🛠️ Quickstart

### 1. Clone the repository

```bash
git clone https://github.com/JohannGaviria/fastapi-microservice-hexagonal-template
cd fastapi-microservice-hexagonal-template
```

### 2. Copy environment variables

Copy `.env.example` to `.env` and edit as needed, or set the variables directly in your environment. See the table below for required variables.

```bash
cp .env.example .env
```

| **Category** | **Variable**             | **Description**                         | **Example**                                                                                                    |
|--------------|--------------------------|-----------------------------------------|----------------------------------------------------------------------------------------------------------------|
| **Database** | `DATABASE_URL`           | Full connection string                  | `postgresql+psycopg2://user:pass@db:5432/db`                                                                   |
|              | `POSTGRES_DB`            | Database name                           | `fastapi`                                                                                                      |
|              | `POSTGRES_USER`          | Database user                           | `postgres`                                                                                                     |
|              | `POSTGRES_PASSWORD`      | DB password                             | `supersecret`                                                                                                  |
|              | `POSTGRES_HOST`          | DB host                                 | `db`                                                                                                           |
|              | `POSTGRES_PORT`          | DB port                                 | `5432`                                                                                                         |
| **App**      | `APP_NAME`               | App name                                | `FastAPI Hexagonal Template`                                                                                   |
|              | `APP_SUMMARY`            | Short summary of the application        | `A FastAPI microservice with hexagonal architecture`                                                           |
|              | `APP_DESCRIPTION`        | Detailed description of the application | `This project is a boilerplate template to build scalable FastAPI microservices using hexagonal architecture.` |
|              | `APP_VERSION`            | App version                             | `1.0.0`                                                                                                        |
|              | `DEBUG`                  | Debug mode                              | `True`                                                                                                         |
| **CORS**     | `CORS_ALLOW_ORIGINS`     | Allowed origins                         | `http://localhost,http://example.com`                                                                          |
|              | `CORS_ALLOW_CREDENTIALS` | Allow CORS credentials (True or False)  | `True`                                                                                                         |
|              | `CORS_ALLOW_METHODS`     | Allowed HTTP methods                    | `GET,POST,PUT,DELETE`                                                                                          |
|              | `CORS_ALLOW_HEADERS`     | Allowed headers                         | `Authorization,Content-Type`                                                                                   |

### ‍💻 Run in a local environment

#### Prerequisites

- [Python 3.11+](https://www.python.org/) (recommended: 3.12 or 3.13)
- [Postgresql](https://www.postgresql.org/) (local or Docker, for development DB)
- [pip](https://pip.pypa.io/en/stable/)
- [virtualenv](https://virtualenv.pypa.io/en/latest/) (optional but recommended)

#### 1. Create and activate a virtual environment (recommended)

```bash
python3 -m virtualenv venv
# En Windows
venv\Scripts\activate
# En Mac/Linux
source venv/bin/activate
```

#### 2. Install dependencies

```bash
pip install -r requirements.txt
```

#### 3. Run database migrations

```bash
alembic revision --autogenerate -m "your migration message"
```

> **NOTE:** After generating a migration, go to the newly created migration file in the `alembic/versions/<filename>.py` directory and add the import statement `import sqlmodel` at the top.
> This ensures that the migration applies correctly and avoids import errors related to `sqlmodel` when running the migration in the database.

```bash
alembic upgrade head
```

#### 4. Start the FastAPI server

```bash
uvicorn app.main:app --reload
```

The API will be available at [http://localhost:8000/docs](http://localhost:8000/docs) (Swagger UI).

#### 5. Running tests

All tests are written using `pytest`.  
Unit tests are fully isolated: no real database or external services are required.

```bash
pytest
```

You can also run a specific test file:

```bash
pytest tests/infrastructure/api/routers/test_router.py
```

### 🐳 Run in a Docker environment

#### Prerequisites
- [Docker](https://docs.docker.com/get-docker/) (v20+ recommended)
- [Docker Compose](https://docs.docker.com/compose/) (v2+)

#### Docker usage

You can run the service and database with Docker Compose:

```bash
docker compose up --build
```

This will start the API and a Postgresql database. The API will be available at [http://0.0.0.0:8000/docs](http://0.0.0.0:8000/docs).

#### Apply Migrations

```bash
docker compose exec fastapi alembic revision --autogenerate -m "your migration message"
```

> **NOTE:** After generating a migration, go to the newly created migration file in the `alembic/versions/<filename>.py` directory and add the import statement `import sqlmodel` at the top.
> This ensures that the migration applies correctly and avoids import errors related to `sqlmodel` when running the migration in the database.

#### Running tests

All tests are written using `pytest`.  
Unit tests are fully isolated: no real database or external services are required.

```bash
docker compose exec fastapi pytest
```

You can also run a specific test file:

```bash
docker compose exec fastapi pytest tests/infrastructure/api/routers/test_router.py
```

---

## ✨ Features

- 🏛 **Hexagonal Architecture** → Decoupled business logic with clear separation of concerns.
- ⚡ **FastAPI** → High-performance async web framework.
- 🗄 **SQLModel + PostgreSQL** → Modern ORM with type safety.
- 🔄 **Alembic** → Automatic database migrations.
- 🐳 **Docker & Compose** → Ready for development and production.
- 🔐 **JWT Authentication** → Token-based secure access.
- 🌐 **CORS Configured** → Multi-origin ready.
- 🧪 **Pytest Integration** → Unit & integration tests included.
- 📦 **Reusable Template** → Designed to bootstrap new microservices faster.

---

## 📚 Further Reading

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [SQLModel Documentation](https://sqlmodel.tiangolo.com/)
- [Pytest Documentation](https://docs.pytest.org/)
- [Docker Documentation](https://docs.docker.com/)

## 📄 License
Distributed under the **MIT License**. See [LICENSE](./LICENSE.txt) for details.

---

> Made with ❤️ by [JohannGaviria](https://github.com/JohannGaviria)