class Articles:
  '''
  Articles class to define Article objects
  '''
  all_articles = []
  def __init__(self, author, title, imageurl, publishedAt, url):
    self.author = author
    self.title = title
    self.imageurl =imageurl
    self.publishedAt = publishedAt
    self.url = url


    @classmethod
    def get_articles(cls,id):

        response = []

        for review in cls.all_articles:
            if review.news_id == id:
                response.append(Articles)

        return response