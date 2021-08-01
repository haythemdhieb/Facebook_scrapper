FROM ubuntu:18.04 AS develop

# RUN apk add --update python make g++ python-dev py-pip && rm -rf /var/cache/apk/*
RUN apt-get update && apt-get install -y wget 
RUN apt-get install -y libmysqlclient-dev wget make g++ curl libspatialindex-dev  python3-pip  python3.7 && rm -rf /var/lib/apt/lists/*
#RUN python3.7 -m pip install --upgrade pip setuptools
RUN apt-get update && apt-get install -y python3 python3-pip

# Set working directory
WORKDIR /Facebook_scrapper/
COPY . .
# install requirements
RUN python3.7 -m pip install --upgrade pip
RUN python3.7 -m pip install -r requirements.txt
RUN pip install uvicorn fastapi
RUN pip install facebook-scraper
# export pythonpath
ENV PYTHONPATH "/Facebook_scrapper"
RUN update-alternatives --install /usr/bin/python python /usr/bin/python3.7 40

EXPOSE 8000

CMD ["uvicorn","storage:app","--host=0.0.0.0" ,"--reload"]












