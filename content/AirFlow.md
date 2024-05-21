---
title: "AirFlow"
date: 2024-05-21T22:59:03+09:00
---

# Airflow

## 概要

Airflowは、Apache Software Foundationが提供するオープンソースのワークフロー管理プラットフォーム。データパイプラインのスケジューリングと監視を行うために使用される。Pythonで記述された柔軟なDAG（Directed Acyclic Graph）を使用してワークフローを定義することができる。

## 特徴

- **スケーラビリティ**: ワークフローのスケジュールと実行を容易に拡張可能。
- **柔軟性**: 複雑なワークフローをシンプルに記述できる。
- **モジュール性**: 各タスクが独立しており、再利用が容易。
- **可観測性**: Webインターフェースを通じてワークフローの監視とデバッグが可能。
- **スケジューリング**: 時間やイベントに基づくタスクのスケジューリングが可能。
- **拡張性**: カスタムプラグインやオペレーターの追加が容易。

## 主なコンポーネント

- **DAG（Directed Acyclic Graph）**: ワークフローを構成するタスクとその依存関係を定義する。
- **Operator**: 個々のタスクの定義と実行を行う。例えば、BashOperator、PythonOperatorなどがある。
- **Scheduler**: DAGに従ってタスクをスケジュールし、実行タイミングを管理する。
- **Executor**: タスクの実行方法を定義する。例えば、LocalExecutor、CeleryExecutorなどがある。
- **Web UI**: ワークフローの状態監視、ログの確認、タスクの再実行などが可能なユーザーインターフェース。

## 利用方法

1. **インストール**: 
   - pipを使用してインストール可能。
     ```bash
     pip install apache-airflow
     ```

2. **DAGの定義**: 
   - PythonスクリプトとしてDAGを定義する。
     ```python
     from airflow import DAG
     from airflow.operators.bash import BashOperator
     from datetime import datetime

     default_args = {
         'owner': 'airflow',
         'start_date': datetime(2023, 1, 1),
     }

     dag = DAG(
         'example_dag',
         default_args=default_args,
         schedule_interval='@daily',
     )

     t1 = BashOperator(
         task_id='print_date',
         bash_command='date',
         dag=dag,
     )

     t2 = BashOperator(
         task_id='sleep',
         bash_command='sleep 5',
         dag=dag,
     )

     t1 >> t2
     ```

3. **Web UIでの監視**: 
   - AirflowのWebサーバーを起動し、http://localhost:8080でDAGの状態を監視する。
     ```bash
     airflow webserver --port 8080
     ```

4. **スケジューラーの起動**: 
   - DAGをスケジュールするためのスケジューラーを起動する。
     ```bash
     airflow scheduler
     ```