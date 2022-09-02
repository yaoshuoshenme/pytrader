server_ip=$(cat < account.json | jq .server.ip | sed -r 's/"//g')

echo "$server_ip"