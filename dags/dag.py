from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator
from datetime import datetime

# Define the default arguments
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 10, 8),
    'retries': 1,
}

# Define the DAG
with DAG(
    dag_id='create_table_in_postgres_dag',
    default_args=default_args,
    schedule_interval=None,  # Run on demand
    catchup=False
) as dag:

    # Task to create a table in PostgreSQL
    create_table = PostgresOperator(
        task_id='create_table_task',
        postgres_conn_id='yelp',  # Use the connection ID for PostgreSQL
        database='yelp-datalake',
        sql="""
        CREATE TABLE IF NOT EXISTS my_table (
            id SERIAL PRIMARY KEY,
            name VARCHAR(50) NOT NULL,
            age INT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """,
    )

    create_table
