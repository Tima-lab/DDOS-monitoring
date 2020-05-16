#!/bin/bash

crontab -l | grep -v "script_ddos_search.sh" | crontab -

systemctl stop python.service
systemctl disable python.service
rm /etc/systemd/system/python.service
rm /usr/lib/systemd/system/python.service
systemctl daemon-reload
systemctl reset-failed
