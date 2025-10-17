mkdir ~/airflow_lab && cd ~/airflow_lab
mkdir dags logs plugins

docker run -d \
  -p 8080:8080 \
  -v $(pwd)/05_Orchestration/airflow/lab/dags:/opt/airflow/dags \
  -v $(pwd)/05_Orchestration/airflow/lab/logs:/opt/airflow/logs \
  -v $(pwd)/05_Orchestration/airflow/lab/plugins:/opt/airflow/plugins \
  --env-file .env \
  -e AIRFLOW__CORE__EXECUTOR=LocalExecutor \
  -e AIRFLOW__CORE__LOAD_EXAMPLES=True \
  -e AIRFLOW__CORE__FERNET_KEY=$(python3 -c "from cryptography.fernet import Fernet; print(Fernet.generate_key().decode())") \
  --name airflow-lab apache/airflow:2.8.0 webserver

docker exec airflow-lab airflow db init
docker exec airflow-lab airflow users create \
    --username admin \
    --firstname Air \
    --lastname Flow \
    --role Admin \
    --email admin@example.com \
    --password admin

docker exec -d airflow-lab airflow scheduler
