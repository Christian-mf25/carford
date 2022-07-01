# FROM python:3.11.0b3-alpine3.16

# WORKDIR /app/__init__.py
# COPY requirements.txt /app/__init__.py

# ENV FLASK_ENV development

# RUN pip install --upgrade pip
# RUN pip install -r requirements.txt

# EXPOSE 5000

# CMD ["flask", "run"]