FROM python:3
WORKDIR /usr/src/app
COPY requirements.txt requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt
COPY . /usr/src/app
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
EXPOSE 8000
