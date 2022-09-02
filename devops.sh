if [ ! $1 ];then
  echo -e "\033[41;37m image name is null \033[0m"
  exit
fi
if [ ! $2 ];then
  echo -e "\033[41;37m image version is null \033[0m"
  exit
fi
image_name=$1
image_version=$2
local_path="/data/pytrader"
docker_path="/home/app/trader/volume"

echo "============开始构建============="
echo -e "镜像名称：${image_name} \n 镜像版本：${image_version}"

if [ -d pytrader ]; then
    rm -f pytrader
    echo "删除旧代码成功"
fi

echo "开始下载最新pytrader代码"
git clone https://github.com/yaoshuoshenme/pytrader.git  pytrader

cd pytrader || exit
echo "构建docker镜像----开始"
docker build -t "$image_name":"$image_version" .
echo "构建docker镜像----成功"

# 停止、删除运行中容器
container_id=$(docker ps -a | grep "${image_name}" | awk '{print $1}')
docker stop "$container_id"
docker rm "$container_id"
# 删除旧镜像
old_image_id=$(docker images | grep "${image_name}" | grep -v "$image_version" | awk '{print $3}')
docker rmi "$old_image_id"
echo "删除旧容器成功"

# 获取新镜像id
new_image_id=$(docker images | grep "$image_name" | grep "$image_version" | awk '{print $3}')
# 创建并新容器
docker run -d -p 8808:8808 -v "$local_path":"$docker_path" --name "$image_name" --network local-network --ip 192.168.0.101 "$new_image_id"

echo "容器${image_name}:${image_version}启动成功, 内网ip:192.169.0.101, port:8808"