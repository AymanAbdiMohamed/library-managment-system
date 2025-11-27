# Group 9 - Library Management System

We have made a Library Management System project. This repository contains the scaffold for a Python application using SQLAlchemy and Alembic.

## Project Overview

Our goal was to build a simple system to manage books and members in a library. We can:
1.  Define the database models.
2.  Set up the database schema using Alembic migrations.
3.  Implement CRUD (Create, Read, Update, Delete) operations.

## Setup Instructions

### Prerequisites
- Python 3.10+
- `pipenv` (Install with `pip install pipenv`)

### Installation

1.  Clone the repository.
2.  Install dependencies:
    ```bash
    pipenv install
    ```
3.  Activate the virtual environment:
    ```bash
    pipenv shell
    ```

## Alembic Setup (Migrations)

**Crucial Step**: You need to initialize Alembic to manage your database migrations.

1.  Initialize Alembic:
    ```bash
    alembic init alembic
    ```
    This will create an `alembic/` directory and an `alembic.ini` file.

2.  **Configure `alembic/env.py`**:
    You must edit `alembic/env.py` to point to your SQLAlchemy models so Alembic can detect changes.
    - Import your `Base` and models in `alembic/env.py`.
    - Set `target_metadata = Base.metadata`.

    *Hint: Look for the "target_metadata" variable in `env.py`.*

3.  **Configure Database URL**:
    - You can set the `sqlalchemy.url` in `alembic.ini` or (better) configure it dynamically in `env.py`.
    - For this project, a simple SQLite database (`sqlite:///library.db`) is sufficient.

## Tasks

### 1. Database Connection (`app/database.py`)
- [ ] Complete the `get_db` function or session handling.
- [ ] Define the `Base` class using `declarative_base`.

### 2. Define Models (`app/models.py`)
- [ ] Define a `Book` model with at least 3 columns (e.g., id, title, author, published_date).
- [ ] Define a `Member` model with at least 3 columns (e.g., id, name, email, joined_date).
- [ ] Ensure different datatypes are used (Integer, String, Date, etc.).

### 3. Create Migrations
- [ ] Generate a migration script:
    ```bash
    alembic revision --autogenerate -m "Initial migration"
    ```
- [ ] Apply the migration:
    ```bash
    alembic upgrade head
    ```

### 4. Implement CRUD (`app/crud.py`)
- [ ] Implement functions to create, read, update, and delete books and members.
- [ ] Use the SQLAlchemy session to interact with the database.

### 5. Run the App (`app/main.py`)
- [ ] Call your CRUD functions in `main.py` to demonstrate they work.

## Resources

- [SQLAlchemy 2.0 Documentation](https://docs.sqlalchemy.org/en/20/)
- [Alembic Tutorial](https://alembic.sqlalchemy.org/en/latest/tutorial.html)
- [SQLAlchemy ORM Quick Start](https://docs.sqlalchemy.org/en/20/orm/quickstart.html)

---

## Group Discussion & Findings

*Use this section to document your learning and decisions.*

### How SQLAlchemy Works
<!-- Discuss how the ORM maps Python classes to database tables -->

### How Alembic Works
<!-- Discuss how Alembic tracks changes and generates SQL scripts -->

### Challenges Faced
<!-- List any issues you encountered and how you solved them -->
