git pull
docker build -t alva/sealbot:v1 .
docker run -d --name sealbot alva/sealbot:v1