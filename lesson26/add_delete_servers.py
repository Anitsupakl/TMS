#/usr/bin/python
"""
скрипт, который обращается к CMDB API и добавляет или удаляет сервер
"""

import argparse
import sys

import requests

#https://github.com/anestesia001/cmdb-37/tree/main
CMDB_URL = "http://localhost:8080/api/servers"   


parser = argparse.ArgumentParser(description="добавить или удалить сервер")
parser.add_argument("action", choices=["add", "delete"], help="шо сделать")
parser.add_argument("name", help="имя сервера, web-01 из примера")
parser.add_argument("--env", default="dev", help="окружение для add, по дефолту dev")
parser.add_argument(
    "--status",
    default="running",
    choices=["running", "stopped", "maintenance"],
    help="состояние для add, по дефолту running",
)
args = parser.parse_args()

try:
    if args.action == "add":
        new_server = {
            "name": args.name,
            "environment": args.env,
            "status": args.status,
        }
        response = requests.post(CMDB_URL, json=new_server, timeout=10)
        response.raise_for_status()
        print(f"Сервер {args.name} добавлен")

    else:
        response = requests.delete(f"{CMDB_URL}/{args.name}", timeout=10)
        response.raise_for_status()
        print(f"Сервер {args.name} удалён")

except requests.exceptions.RequestException as error:
    print(f"Ошибка при обращении к CMDB: {error}")
    sys.exit(1)