import unittest
from models import news

News = news.News
Sources = news.Sources

# _______________________________________News Class____________________________________________________________

class NewsTest(unittest.TestCase):
    """
    Test Class to test behaviour of News class
    """

    def setUp(self):
        """
        Set Up method that will run before each test
        """
        self.new_news = News(
            #  title
            "Hackers",
            # description
            "In een video die zaterdag op Youtube werd geplaatst",
            # url
            "https://www.ad.nl/tech/hackers-van-anonymous-klaar-met-narcistische-rijke-gozer-elon-musk-we-komen-achter-je-aan~ae02f68b/",
            # urlToImage
            "https://images0.persgroep.net/rcs/uAun_D_gAfSfSrk53-hfMswOIPE/diocontent/203649608/_focus/0.51/0.38/_fill/1200/630/?appId=21791a8992982cd8da851550a453bd7f&quality=0.7",
            # publishedAt
            "2021-06-06T05:32:47Z",
        )
        self.news_sources = Sources(
            # id
            "abc-news",
            # name
            "ABC News",
            # description
            "Your trusted source for breaking news",
            # url
            "https://abcnews.go.com",
            # category
            "general",
        )

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news, News))

    # Correct instatanciation
    def test_initial(self):
        self.assertEqual(self.new_news.title, "Hackers")
        self.assertEqual(
            self.new_news.description,
            "In een video die zaterdag op Youtube werd geplaatst",
        )
        self.assertEqual(
            self.new_news.url,
            "https://www.ad.nl/tech/hackers-van-anonymous-klaar-met-narcistische-rijke-gozer-elon-musk-we-komen-achter-je-aan~ae02f68b/",
        )
        self.assertEqual(
            self.new_news.urlToImage,
            "https://images0.persgroep.net/rcs/uAun_D_gAfSfSrk53-hfMswOIPE/diocontent/203649608/_focus/0.51/0.38/_fill/1200/630/?appId=21791a8992982cd8da851550a453bd7f&quality=0.7",
        )
        self.assertEqual(self.new_news.publishedAt, "2021-06-06T05:32:47Z")
# ______________________________________________Source Class_______________________________________________

    def test_Source_initial(self):
        self.assertTrue(isinstance(self.news_sources, Sources))


    # Correct instatanciation
    def test_Sources_initial(self):
        self.assertEqual(self.news_sources.id,"abc-news")
        self.assertEqual(self.news_sources.name,"ABC News")
        self.assertEqual(self.news_sources.description, "Your trusted source for breaking news")
        self.assertEqual(self.news_sources.url, "https://abcnews.go.com")
        self.assertEqual(self.news_sources.category, "general")



if __name__ == "__main__":
    unittest.main()
