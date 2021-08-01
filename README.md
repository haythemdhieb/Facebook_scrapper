# Facebook_scrapper
In this project, we are going to scrape data from "nous sommes les ingénieurs facebook page".
## Environement Setup
================================================================================

1- We use:
- [conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html)
  to setup our environment,
- and python 3.7

Setup our environment:
```bash
conda --version
#clone the repo from
git clone https://github.com/haythemdhieb/Facebook_scrapper.git
cd Facebook_scrapper/
# Create a conda env
conda env create -f environment.yml
# Activate
conda activate FbScrapper
```
## 1. Running the workflow (Script Mode)
--------------------------------------------------------------------------------
to run the application, we have to run this command:
 ``` uvicorn storage:app --reload```
## 2. Testing
 ``` pytest test_scrapping.py```
## 3. Dockerization:
to run the docker container, we have to run these commands:
1 - ``` docker-compose build```

2-  ``` docker-compose up```
