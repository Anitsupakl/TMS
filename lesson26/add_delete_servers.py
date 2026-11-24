#/usr/bin/python
"""
скрипт, который обращается к CMDB API и добавляет или удаляет сервер
Запускать так,
 python3 add_delete_servers.py add web-06 --ip 192.168.10.16 --env prod --status running
 python3 add_delete_servers.py delete web-06
"""


#https://github.com/anestesia001/cmdb-37/tree/main
CMDB_URL = "http://localhost:8080/api/servers"   

import argparse
import sys
import requests

parser = argparse.ArgumentParser(description="Добавить или удалить сервер")
parser.add_argument("action", choices=["add", "delete"], help="что сделать")
parser.add_argument("hostname", help="имя сервера")

parser.add_argument("--ip", help="IP-адрес")
parser.add_argument("--os", default="Ubuntu 24.04", help="ОС")
parser.add_argument("--env", default="dev", help="окружение: dev, stage, prod")
parser.add_argument(
    "--status",
    default="running",
    choices=["running", "stopped", "maintenance"],
    help="состояние",
)
parser.add_argument("--cpu", type=int, default=2, help="количество ядер")
parser.add_argument("--ram", type=int, default=2048, help="память в МБ")
parser.add_argument("--team", default="devops", help="команда-владелец")
args = parser.parse_args()

try:
    if args.action == "add":
        if not args.ip:
            print("Для add нужно указать --ip, например: --ip 192.168.10.16")
            sys.exit(1)

        new_server = {
            "hostname": args.hostname,
            "ip_address": args.ip,
            "os": args.os,
            "environment": args.env,
            "status": args.status,
            "cpu": args.cpu,
            "ram": args.ram,
            "team": args.team,
        }
        response = requests.post(CMDB_URL, json=new_server, timeout=10)
        response.raise_for_status()
        print(f"Сервер {args.hostname} добавлен")

    else:
        response = requests.get(CMDB_URL, timeout=10)
        response.raise_for_status()

        server_id = None
        for server in response.json():
            if server["hostname"] == args.hostname:
                server_id = server["id"]

        if server_id is None:
            print(f"Сервер {args.hostname} не найден")
            sys.exit(1)

        response = requests.delete(f"{CMDB_URL}/{server_id}", timeout=10)
        response.raise_for_status()
        print(f"Сервер {args.hostname} (id={server_id}) удалён")

except requests.exceptions.RequestException as error:
    print(f"Ошибка при обращении к CMDB: {error}")
    if error.response is not None:
        print("Ответ сервера:", error.response.text) 
    sys.exit(1)