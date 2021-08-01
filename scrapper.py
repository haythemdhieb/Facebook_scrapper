from facebook_scraper import get_posts

class Scrapper:
    def __init__(self):
        pass
    def scrape_fb_page(self,FbPage,pages):
        posts=[]
        try:
            for post in get_posts(FbPage,pages=pages):
                posts.append({"post_id":post["post_id"],"text":post["text"]})
            return(posts)   
        except: 
            print("no such facebook  page found")
            return([])


