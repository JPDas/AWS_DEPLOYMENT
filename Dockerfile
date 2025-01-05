FROM python:3.12.8-slim-bullseye
COPY ./app ./app
COPY ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["app.app.handler"]