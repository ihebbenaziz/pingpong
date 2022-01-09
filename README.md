# pingpong

This project is a take home test.

The folllowing is a user manual.

Web application:

First step is to build the docker image: docker build -t planetly/ping:1 -f Dockerfile  .

Second step is to run the container and then you have the web application running: docker run -p 5000:5000 -d --name ping-pong planetly/ping:1

The web application will be reachable locally through the url: http://localhost:5000/ping

CLI:

For the CLI you should install python, the requests library (pip install requests) and then run the script under /CLI/CLI.py specifying the endpoint and the value of the header x-secret-key, exapmple: py CLI.py "http://localhost:5000/ping" 4
