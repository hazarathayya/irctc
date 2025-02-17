# irctc

### Installation & Setup

1. Clone the Repository
git clone https://github.com/your-username/railway-management.git

    cd railway-management


2. Create a Virtual Environment

    python3 -m venv venv

    source venv/bin/activate  # On Mac/Linux

    venv\Scripts\activate     # On Windows


3. Install Dependencies

    pip install -r requirements.txt

4. Set Up PostgreSQL Database

    Ensure PostgreSQL is installed and running. Then create a database:

    CREATE DATABASE railway_db;

    CREATE USER railway_user WITH PASSWORD 'irctc123';

    ALTER ROLE railway_user SET client_encoding TO 'utf8';

    GRANT ALL PRIVILEGES ON DATABASE railway_db TO railway_user;


5. Configure Environment Variables

    Create a .env file in the project root and add:

    DATABASE_URL=postgresql://railway_user:irctc123@localhost/railway_db
    JWT_SECRET_KEY=supersecret


6. Run Database Migrations

    flask db init
    flask db migrate -m "Initial migration"
    flask db upgrade

7. Run the Flask App

    python run.py

    The app will be available at: http://127.0.0.1:5000