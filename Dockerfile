FROM python:3.12.8-slim-bullseye
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["app.handler" ]