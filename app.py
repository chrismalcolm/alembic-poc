from flask import Flask
from models import Counters
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os


load_dotenv(override=True)

app = Flask(__name__)

user = os.environ["POSTGRES_USER"]
password = os.environ["POSTGRES_PASSWORD"]
host = os.environ["POSTGRES_HOST"]
port = os.environ["POSTGRES_PORT"]
database = os.environ["POSTGRES_DB"]

engine = create_engine(f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}")

Session = sessionmaker(bind=engine)

@app.route('/hello/<name>')
def hello_name(name: str):
    name = name.strip().lower()
    with Session() as session:
        if session.query(Counters).filter(Counters.name == name).first() is None:
            session.add(Counters(name=name))
        counter = session.query(Counters).filter(Counters.name == name).first()
        counter.value += 1
        value = counter.value
        session.commit()
    return f"Hello {name.capitalize()}! You have visited {value} times."

if __name__ == '__main__':
    app.run()