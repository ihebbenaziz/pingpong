FROM python:alpine 

EXPOSE 5000

RUN pip install Flask
RUN pip install Flask-Limiter
COPY src/webApp.py app.py

ENTRYPOINT ["flask", "run"]