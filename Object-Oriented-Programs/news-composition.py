class News:
    def __init__(self, sports_news, tech_news, world_news):
        self.sports_news = sports_news
        self.tech_news = tech_news
        self.world_news = world_news



    def get_complete_news(self):
        print("Get all the news under one go--")
        self.sports.sportsInfo()
        self.tech.techInfo()
        self.world.worldInfo()

dnews = News()
dnews.get_complete_news()