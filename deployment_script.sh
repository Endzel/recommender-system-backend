# Substitute this environmental variables with the ones referring your directories!
export WORKING_DIR=C:/dev/recommender-system-backend
export STACK_NETWORK=recommender_network
export STACK_NAME=recommender_deployment

docker stack rm $STACK_NAME

sleep 15

CHECK_NETWORK=`docker network ls | grep "$STACK_NETWORK " | wc -l`;

if [ "$CHECK_NETWORK" -eq 0 ]
then
    echo "[network.sh] Creating network $STACK_NETWORK..."
    docker network create --attachable -d overlay ${STACK_NETWORK}
else
    echo "[network.sh] Network $STACK_NETWORK already existing"
fi

docker build -t $STACK_NAME .

envsubst < ./deploy.yml > ./after-deploy.yml

docker stack deploy -c ./after-deploy.yml $STACK_NAME

rm ./after-deploy.yml
