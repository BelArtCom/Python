# to run server:
```
PORT=8080 python3.10 server.py
```

# to develop:
```
npx nodemon --exec PORT=3100 python3.10 server.py
```
# to test
```
python3.10 -m unittest test_server.py 
```

# to build Docker image:
```
docker build -t server .
```
# to run Docker container:
```
docker run -e PORT=3100 -p 3100:3100 server
```
