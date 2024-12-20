class Article:
    def __init__(self, title, author, character_count, publication, description):
        self.title = title
        self.author = author
        self.character_count = character_count
        self.publication = publication
        self.description = description

    def __str__(self):
        return f"Статья: {self.title} | Автор: {self.author} | Знаков: {self.character_count} | Издание: {self.publication} | Описание: {self.description}"