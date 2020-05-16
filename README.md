# DDOS-monitoring

## Шаги для запуска
### 1) Нужно установить sqlite3
sudo apt install sqlite3
### 2) Надо создать таблицу
sqlite3 db.sqlite 
и в sqlite3 вводим: create virtual table bad_users using fts4 (ip_addres, country, lat, lon, login, tokenize=simple);

Файл ddos_search1.sh сделан для того, чтобы загрузить в бд информацию с файла history_ssh.out
