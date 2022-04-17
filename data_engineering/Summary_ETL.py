# The ETL function 
import pandas as pd


def extract_table_to_df(tablename, db_engine):
        return pd.read_sql("SELECT * FROM {}".format(tablename),
            db_engine)


def split_columns_transform(df, column, pat, suffixes):
    # Converts column into str and splits it on pat..

def load_df_into_dwh(film_df, tablename, schema, db_engine):
    return pd.to_sql(tablename, db_engine, schema=schema, 
        if_exists="replace")

db_engines={}

def etl():

    #Extract
    film_df = extract_table_to_df("film", db_engines["store"])

    #Transform
    film_df = split_columns_transform(film_df, "rental_rate",".",["_dollar","_cents"])

    # Load 
    load_df_into_dwh(film_df, "film","store",db_engines["dwh"])



# Scheduling with DAGs in Airflow 

from airflow.models import DAG

dag = DAG(dag_id="sample",
        ...,
        schedule_interval="0 0 * * *")


# The DAG definition file 

from airflow.models import DAG
from airflow.operators.python_operator import PythonOperator 

dag = DAG(dag_id="etl_pipeline",
            schedule_interval="0 0 * * *")

etl_task = PythonOperator(task_id = "etl_task",
                python_callable=etl,
                dag=dag)

etl_task.set_upstream(wait_for_this_task)