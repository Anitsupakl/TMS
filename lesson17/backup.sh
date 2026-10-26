#!/bin/bash
source .env

BACKUP_DIR="/data/backups"
DATE="$(date +%Y%m%d)"
DB_NAME='autos'
DB_USER=$DB_USER
DB_PASS=$DB_PASS

mkdir -p $BACKUP_DIR
PGPASSWORD=$DB_PASS pg_dump -U $DB_USER -d $DB_NAME  > ${BACKUP_DIR}/${DB_NAME}-${DATE}.sql


