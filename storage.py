from scrapper import Scrapper
from pymongo import MongoClient
from fastapi import FastAPI

app = FastAPI()


def get_db():
    try:
        client = MongoClient("mongodb://haythem:1234@mongo:27017")
        print("Connected successfully!!!")
        db = client["FbData"]
        return db
    except:
        print("Could not connect to MongoDB")


@app.get("/")
def scrape_data():
    # Scraping data
    scrapper = Scrapper()
    scrapped_data = scrapper.scrape_fb_page("nous.sommes.les.ingenieurs", 5)
    print("data scrapped successfully!!!")
    # database
    # db = conn.database
    db = get_db()
    # insert data
    records = db.FbData.insert_many(scrapped_data)
    print("Data inserted with record ids", records)
    # Printing the data inserted
    print("data inserted and stored successfully")
    posts = [scrapped_data[i]["text"] for i in range(len(scrapped_data))]
    return " ".join(posts)
