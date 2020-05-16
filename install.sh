#!/bin/bash

yum=`command -v yum`
apt=`command -v apt-get`

if [ -n "$yum" ] ; then
	echo "используется yum"
	yum -y install sqlite3
	yum -y install python-pip
elif [ -n "$apt" ] ; then
	echo "используется apt-get"
	sudo apt-get update
	sudo apt-get install sqlite3
	sudo apt instal python-pip
fi

pip install flask
sqlite3 db.ddos "create virtual table bad_users using fts4 (ip_address, country, lat, lon, login, tokenize=simple)"

echo "* * * * * $PWD/install.sh" | crontab

cat > /etc/systemd/system/python.service <<EOF
[Unit]
Description=Python
After=syslog.target

[Service]
Type=idle
ExecStart=/usr/bin/python $PWD/map_ddos_attack/main.py
Restart=always

[Install]
WantedBy=multi-user.target
EOF 
