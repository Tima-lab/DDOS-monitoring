#!/bin/bash

#len=$(lastb | wc -l)

#lastb | head -$((len - 2)) > temp1

now_day=$(date +%d)
now_mon=$(date +%b)

while read login from nday mon day time year a b c d e f zero ip ; do
	echo "$login $from $nday $mon $day $time $year $a $b $c $d $e $f $zero $ip" >> temp2
	echo "$login $from $nday $mon $day $time $year $a $b $c $d $e $f $zero $ip"
done < history_ssh.out | head -20

grep -F -v -f uniq_text temp2 > uniq_text

rm temp2
echo "Ввод данных в бд"

while read login ssh nday mon day time year a b c d e f zero ip ; do
	curl -s "http://ip-api.com/json/$ip?lang=ru&fields=209" | jq '.' > temp
	country=$(cat temp | grep country | awk '{ print $2 }' | cut -c 2- | sed s/..$//)
	lat=$(cat temp | grep lat | awk '{ print $2 }' | sed s/.$//)
	lon=$(cat temp | grep lon | awk '{ print $2 }')
	echo "ip = $ip, country = $country, lat = $lat, lon = $lon, login = $login"
	sqlite3 db.sqlite <<EOF 
INSERT INTO bad_users (ip_address, country, lat, lon, login) VALUES ("$ip", "$country", "$lat", "$lon", "$login");
EOF
done < uniq_text

rm temp
