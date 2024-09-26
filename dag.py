from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.providers.google.cloud.operators.datafusion import CloudDataFusionStartPipelineOperator
from airflow.utils.dates import days_ago

default_args = {
    'owner': 'airflow',
    'start_date': days_ago(1),  # Use a past date or `days_ago`
    'depends_on_past': False,
    'email': ['bidhanpanta123@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG('employee_data',
          default_args=default_args,
          description='Runs an external Python script and triggers a DataFusion pipeline',
          schedule_interval='@daily',
          catchup=False)

with dag:
    run_script_task = BashOperator(
        task_id='data_extraction',
        bash_command='python /home/airflow/gcs/dags/script/data_extraction.py',
    )

    start_pipeline = CloudDataFusionStartPipelineOperator(
    location="europe-west2",
    pipeline_name="employee-pipeline",
    instance_name="data-fusion-dev",
    task_id="start_pipeline",
    )

    run_script_task >> start_pipeline

