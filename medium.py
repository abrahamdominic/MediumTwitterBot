import requests

URL = "https://api.rss2json.com/v1/api.json?rss_url=https://medium.com/feed/the-gray-area"

# URL To Fetch Latest Post
def fetch_article(url):
    response = requests.get(url)
    posts = response.json()
    if posts["status"] == "ok":
        posts = posts["items"]
        for post in posts:
            post_title = post["title"]
            post_url = post["link"]
            post_image = post["thumbnail"]
            post_categories = post["categories"]
            return {"title": post_title, "thumbnail": post_image, "link": post_url, "categories": post_categories}

# Parse latest post for Twitter
def Title_Link_Post(url):
    post_dict = fetch_article(url)
    if(post_dict):
        catList = post_dict["categories"]
        for category in catList:
            newcat = "#" + category
            catList[catList.index(category)] = newcat
        catList = " ".join(catList)
        catList = catList.replace("-", "")
        post_str = post_dict['title'] + ' \n ' + str(catList) + " \n " + post_dict['link']
        return post_str