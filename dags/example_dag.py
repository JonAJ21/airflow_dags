from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator

with DAG(
    "example_dag",
    schedule_interval="@daily",
    start_date=datetime(2024, 1, 1),
    catchup=False,
) as dag:
    task = BashOperator(
        task_id="print_hello",
        bash_command="echo 'Hello from GitSync!'",
    )