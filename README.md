# Alembic POC
A small POC using SQLAlchemy and alembic. 

## Summary
This example is a small Flask server. It has a single endpoint GET **/hello/{name}** which when queried, updates a counter value for the given name in a PostgreSQL database, and responds with the value of the current count for that name.
E.g.
```
curl localhost:5000/hello/chris
Hello Chris! You have visited 3 times.
```

## How to run
Pull this repo to your local machine.

1. Set up python virtual environment

* Create virtual environment
```
python3 -m venv venv
```
* Activate virtual environment
```
source venv/bin/activate
```
* Install dependencies
```
pip3 isntall -r requirements.txt
```

2. Run App/Docker containers
* The docker compose file containers a "Local" Postgres instance and a "Production" Postgres instance. The "Local" is meant to mock a local database setup. The "Production" is meant to mock a production setup, where the app is deployed via Docker.
```
docker compose up -d
```
* For "Local", run the app
```
python3 app.py
```
* For "Production", build and run the app docker image
```
docker build -t alembic-poc .
docker run -p 6000:5000 --network alembic-poc_my_network alembic-poc
```

## how to use alembic

* Install the module
```
pip install alembic
```

* Initialise migrations
```
alembic init migrations
```

* Create the initial migration
```
alembic revision --autogenerate -m "Create a baseline migrations"
```

* Create future migrations - update the SQLAlchemy tables and run
```
alembic revision --autogenerate -m "Describe migration"
```

* Upgrade the DB to be in line with lastest migration
`alembic upgrade head`

## Remarks
* After doing the init for alembic, udpate the `migrations/env.py` file with 
```python
user = os.environ["POSTGRES_USER"]
password = os.environ["POSTGRES_PASSWORD"]
host = os.environ["POSTGRES_HOST"]
port = os.environ["POSTGRES_PORT"]
database = os.environ["POSTGRES_DB"]

config.set_main_option("sqlalchemy.url", f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}")
```
to override the default config. This is the url that alembic will alway use to connect to its DB.

* Docker Entrypoint needs to be a script which runs alembic first and then runs the python app

* It's annoying how migrations are not ordered in migrations/ folder. Perhaps there's a away to alter that?

* Useful source
https://medium.com/@johnidouglasmarangon/using-migrations-in-python-sqlalchemy-with-alembic-docker-solution-bd79b219d6a