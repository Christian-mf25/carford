FROM python

WORKDIR /user/app
COPY requirements.txt /user/app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /user/app