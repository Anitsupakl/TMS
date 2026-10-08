#!/bin/bash

FREE_PORT_N1=$1
FREE_PORT_N2=$2
for i in {$FREE_PORT_N1..$FREE_PORT_N2}; do echo "$i"; done;
COUNTER=$FREE_PORT_N2
for ((i = $1; i <= COUNTER; i++)); do echo "i=$i"; done
