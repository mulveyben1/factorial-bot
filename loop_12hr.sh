#!/usr/bin/env bash

chmod +x fac_bot.py

while true; do

./fac_bot.py

PID=$!

sleep 12h

kill ${PID}

done