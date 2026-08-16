from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id="netflix_pipeline",
    start_date=datetime(2026, 1, 1),
    schedule="* * * * *",
    catchup=False,
    tags=["cicd-demo"],
) as dag:

    extract_watch = BashOperator(
        task_id="extract_watch"
        bash_command="python scripts/extract_watch.py",
    )

    extract_users = BashOperator(
        task_id="extract_users",
        bash_command="python scripts/extract_users.py",
    )

    validate = BashOperator(
        task_id="validate",
        bash_command="python scripts/validate.py",
    )

    [extract_watch, extract_users] >> validate
