FROM python:3.11.7-slim

WORKDIR /polls

COPY requirements.txt /polls/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /polls/

EXPOSE 8000

CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]

