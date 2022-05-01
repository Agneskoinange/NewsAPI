import unittest
from models import news
News = news.News

class NewsTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the News class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source= News( "abc-news","ABC News","Your trusted source for breaking news, analysis, exclusive interviews, headlines, and videos at ABCNews.com.","http://abcnews.go.com","general")
    
    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,News))

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_contact.first_name,"James")
        self.assertEqual(self.new_contact.last_name,"Muriuki")
        self.assertEqual(self.new_contact.phone_number,"0712345678")
        self.assertEqual(self.new_contact.email,"james@ms.com")

if __name__ == '__main__':
    unittest.main()