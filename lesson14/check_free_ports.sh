#!/bin/bash

FREE_PORT_N1=$1
FREE_PORT_N2=$2
BUSY_PORTS=$(ss -tlpn)

check_busy_ports() {
#  if ( $BUSY_PORTS | grep $FREE_PORT_N1 && $BUSY_PORTS | grep $FREE_PORT_N2 ); then
  if echo "${BUSY_PORTS}" | grep -w "${FREE_PORT_N1}" && echo "${BUSY_PORTS}" | grep -w "${FREE_PORT_N2}" ; then 
   echo "${FREE_PORT_N1} и ${FREE_PORT_N2} - оба порта заняты"
  else
    echo "Порты свободны"
fi
}

check_busy_ports
