# DDOS-monitoring

## Шаги для запуска
### 1) Нужно установить sqlite3
sudo apt install sqlite3
### 2) Надо создать таблицу
sqlite3 db.sqlite 
и в sqlite3 вводим: create virtual table bad_users using fts4 (ip_addres, country, lat, lon, login, tokenize=simple);

### 3) Запуск скрипта и сайта
<ol>
  <li>Надо сделать файли исполняемым: chmod +x путь/script-ddos-search.sh</li>
  <li>Запуск: ./путь/script-ddos-search.sh</li>
  <li>Теперь надо запустить файл main.py из папки map_ddos_attack: python путь/map_ddos_attack/main.py</li>
<\ol>
### 4) Чтобы запускать скрипт автоматически надо:
<ol>
  <li></li>
</ol>

Файл ddos_search1.sh сделан для того, чтобы загрузить в бд информацию с файла history_ssh.out
