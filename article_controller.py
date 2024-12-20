from article_model import Article

class ArticleController:
    def __init__(self):
        self.articles = []

    def add_article(self, article):
        self.articles.append(article)

    def remove_article(self, article):
        self.articles.remove(article)

    def get_all_articles(self):
        return self.articles

    def find_article_by_author(self, author):
        return [article for article in self.articles if article.author == author]