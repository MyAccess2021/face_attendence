
```
docker build -t face-attendance-app .
```
```
docker run -it -d --rm -p 8001:8001 face-attendance-app
```
```
docker run -d \
  --name face-attendance \
  -p 8001:8001 \
  --network cap-network \
  --restart unless-stopped \
  face-attendance-app
```
