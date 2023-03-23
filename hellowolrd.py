from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

def print_hello():
    print("Hello, world!")

dag = DAG('hello_world', description='Print Hello World', schedule_interval=None, start_date=datetime(2023, 3, 23))

hello_operator = PythonOperator(task_id='print_hello', python_callable=print_hello, dag=dag)

hello_operator
