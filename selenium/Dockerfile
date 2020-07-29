# Starting with a prebuilt docker image with chromedriver
# because chromedriver takes forever to install:

FROM joyzoursky/python-chromedriver

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD wait-for-it --service web:3000 --timeout 30 -- pytest
