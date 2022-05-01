class Articles:


        response = []

        for review in cls.all_articles:
            if review.news_id == id:
                response.append(Articles)

        return response