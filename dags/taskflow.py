from airflow.decorators import dag,task
from datetime import datetime

@dag(
    start_date=datetime(2024,7,2),
    schedule_interval='@daily',
    tags=['taskflow']
)

def taskflow():

    @task
    def task_a():
        print("Task A")

    @task
    def task_b(value):
        print("Task B")
        print(value)

    task_b(task_a())



taskflow()