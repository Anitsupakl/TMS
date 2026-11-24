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

CMDB_URL = "http://localhost:8080/api/servers"


parser = argparse.ArgumentParser(description="Список всех серверов")
parser.add_argument("--env", help="окружение: dev, prod, stage ")
parser.add_argument(
    "--status",
    choices=["running", "stopped", "maintenance"],
    help="состояние сервера",
)
args = parser.parse_args()

try:
    response = requests.get(CMDB_URL, timeout=10)
    response.raise_for_status() 
except requests.exceptions.RequestException as error:
    print(f"Не удалось получить данные из CMDB: {error}")
    sys.exit(1)

servers = response.json() 

if args.env:
    servers = [s for s in servers if s["environment"] == args.env]
if args.status:
    servers = [s for s in servers if s["status"] == args.status]

if not servers:
    print("Серверы не найдены")
else:
    print(f"{'ID':<4} {'HOSTNAME':<16} {'IP':<16} {'ОКРУЖЕНИЕ':<10} {'СОСТОЯНИЕ':<12}")
    print("-" * 62)
    for s in servers:
        print(
            f"{s['id']:<4} "
            f"{s['hostname']:<16} "
            f"{s['ip_address']:<16} "
            f"{s['environment']:<10} "
            f"{s['status']:<12}"
        )
    print(f"\nВсего: {len(servers)}")
