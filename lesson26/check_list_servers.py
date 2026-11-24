#/usr/bin/python
"""
cкрипт, который обращается к CMDB API и выводит

    список всех серверов
    список серверов конкретного окружения (dev/prod/etc)
    список серверов в заданном через аргумент состоянии (runnung/stopped/maintenance)

"""
import argparse
import sys

import requests

#https://github.com/anestesia001/cmdb-37/tree/main
CMDB_URL = "http://localhost:8080/api/servers"   

parser = argparse.ArgumentParser(description="Список сервров из CMDB")
parser.add_argument("--env", help="окружение: dev, stage, prod ")
parser.add_argument(
    "--status",
    choices=["running", "stopped", "maintenance"],
    help="состояние сервера",
)
args = parser.parse_args()

params = {}
if args.env:
    params["environment"] = args.env
if args.status:
    params["status"] = args.status

try:
    response = requests.get(CMDB_URL, params=params, timeout=10)
    response.raise_for_status() 
except requests.exceptions.RequestException as error:
    print(f'Не удалось получить данные из CMDB: {error}')
    sys.exit(1)

servers = response.json()

if not servers:
    print("Серверы не найдены")
else:
    print(f"{'ИМЯ':<20} {'ОКРУЖЕНИЕ':<12} {'СОСТОЯНИЕ':<12}")
    print("-" * 46)
    for server in servers:
        print(
            f"{server['name']:<20} "
            f"{server['environment']:<12} "
            f"{server['status']:<12}"
        )
    print(f"\nВсего: {len(servers)}")