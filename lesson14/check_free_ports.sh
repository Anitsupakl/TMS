#!/bin/bash

FREE_PORT_N1=$1
FREE_PORT_N2=$2
#BUSY_PORTS=$(ss -tlpn)

#check_busy_ports() {
#  if ( $BUSY_PORTS | grep $FREE_PORT_N1 && $BUSY_PORTS | grep $FREE_PORT_N2 ); then
#  if echo "${BUSY_PORTS}" | grep -w "${FREE_PORT_N1}" && echo "${BUSY_PORTS}" | grep -w "${FREE_PORT_N2}" ; then 
#   echo "${FREE_PORT_N1} и ${FREE_PORT_N2} - оба порта заняты"
#  else
#    echo "Порты свободны"
#fi
#}

BUSY_PORTS=$(ss -tln | awk 'NR>1 {print $4}')

COUNTER=$FREE_PORT_N2
for ((i = FREE_PORT_N1; i <= COUNTER; i++)); do
  if echo "${BUSY_PORTS}" | awk -F: '{print $NF}' | grep -qw "$i"; then
    echo "Порт $i занят"
  else
    echo "Порт $i свободен"
    # exit 0
  fi
done
# ничего лучше не придумано как проверять /check_free_ports.sh 1 8010 | grep "занят" (свободен)
