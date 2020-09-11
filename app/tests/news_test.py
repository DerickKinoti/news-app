import unittest
from app.models import news
News = news.News

class newsTest(unittest.TestCase):
    def setUp(self):
        self.newsArticle= News('business-insider','ddd','http://www.businessinsider.com','kkk')
        
     def test_instance(self):
        self.assertIsInstance(self.newsArticle,News)
