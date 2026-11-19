#!/usr/bin/env python3

import subprocess

containers_name = ["redis", "mongo", "application_go"]

result = subprocess.run(
    ["docker", "ps", "--format", "{{.Names}}"],
    capture_output=True,
    text=True,
    check=True
    )
active_containers = result.stdout

for containers in containers_name:
    if containers in active_containers:
        print(f"Контейнер '{containers}' запущен.")

