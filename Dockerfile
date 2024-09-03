FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

# Prod creds
ENV POSTGRES_USER=user_prod
ENV POSTGRES_PASSWORD=password_prod
ENV POSTGRES_DB=db_prod
ENV POSTGRES_PORT=5432
ENV POSTGRES_HOST=alembic_poc_production

RUN chmod +x entrypoint.sh

ENTRYPOINT ["/app/entrypoint.sh"]