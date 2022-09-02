echo "复制部署脚本到服务器"
server_ip=$(cat < account.json | jq .server.ip | sed -r 's/"//g')
#echo "devops.sh root@$server_ip:/root/scripts"
scp -r devops.sh root@"$server_ip":/root/scripts
echo "复制脚本成功"