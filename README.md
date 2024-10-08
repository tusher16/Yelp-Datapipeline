# Airflow PostgreSQL Integration Project

This project demonstrates the integration of Apache Airflow with PostgreSQL, showcasing how to create database tables using Airflow DAGs.

## Project Overview

The project consists of:
1. A Docker setup for Apache Airflow
2. A PostgreSQL database
3. An Airflow DAG that creates a table in PostgreSQL

## Prerequisites

- Docker and Docker Compose
- Basic knowledge of Apache Airflow and PostgreSQL

## Setup

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/airflow-postgres-project.git
   cd airflow-postgres-project
   ```

2. Build the Docker image:
   ```
   docker build -t custom-airflow:latest .
   ```

3. Start the services using Docker Compose:
   ```
   docker-compose up -d
   ```

4. Access Airflow web interface at `http://localhost:8080`

## Project Structure

- `Dockerfile`: Customizes the Airflow image with PostgreSQL client
- `docker-compose.yml`: Defines services for Airflow and PostgreSQL
- `dags/create_table_in_postgres_dag.py`: DAG file to create a table in PostgreSQL

## Usage

1. Ensure all services are up and running.
2. In the Airflow web interface, navigate to Admin > Connections and set up a new PostgreSQL connection with ID 'yelp'.
3. Trigger the DAG 'create_table_in_postgres_dag' manually from the Airflow UI.
4. Verify the table creation in your PostgreSQL database using a tool like pgAdmin.

## Troubleshooting

If the table is not appearing in pgAdmin:
1. Check Airflow logs for any error messages.
2. Verify PostgreSQL connection details in Airflow.
3. Ensure the DAG is specifying the correct database name.
4. Check permissions for the PostgreSQL user defined in the Airflow connection.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.