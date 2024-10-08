# Dockerfile for Apache Airflow
FROM apache/airflow:2.7.1-python3.10

# Install PostgreSQL client and other dependencies
USER root
RUN apt-get update \
    && apt-get install -y postgresql-client libpq-dev nano \
    && apt-get clean

USER airflow
