from article_model import Article
from article_controller import ArticleController
from article_view import ArticleView

if __name__ == "__main__":
    controller = ArticleController()
    view = ArticleView()

    # Добавление статей
    article1 = Article("Как программировать на Python", "Иван Иванов", 1500, "Программирование", "Краткое руководство по Python.")
    article2 = Article("Изучение машинного обучения", "Петр Петров", 2000, "Наука", "Основы машинного обучения.")

    controller.add_article(article1)
    controller.add_article(article2)

    # Отображение всех статей
    view.display_message("Список статей:")
    view.display_articles(controller.get_all_articles())

    # Поиск статей по автору
    view.display_message("Поиск статей автора 'Иван Иванов':")
    ivan_articles = controller.find_article_by_author("Иван Иванов")
    view.display_articles(ivan_articles)