INFLUXDB_HOST = '{{ INFLUXDB_HOST }}'
INFLUXDB_PORT = '8086'
INFLUXDB_USER = '{{ INFLUXDB_USER }}'
INFLUXDB_PASSWORD = '{{ INFLUXDB_PASSWORD }}'
INFLUXDB_DATABASE = '{{ INFLUXDB_DATABASE }}'

# This will be part of the series name, i.e. `default.server_name.memory.usage`
SERVER_NAME = '{{ inventory_hostname }}'
