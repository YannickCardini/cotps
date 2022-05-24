## Docker

In local machine:
```
docker build -t cotps .
docker save cotps:latest | gzip > cotps.tar.gz
scp cotps.tar.gz ubuntu@51.79.255.217:~/Documents/docker/cotps.tar.gz && rm cotps.tar.gz
```
 
In the VPS:
```
docker load < /home/ubuntu/Documents/docker/cotps.tar.gz && rm /home/ubuntu/Documents/docker/cotps.tar.gz
docker run --name=cotps -v /home/ubuntu/Documents/cotps:/data --restart=always -d cotps
docker logs -f cotps
```
