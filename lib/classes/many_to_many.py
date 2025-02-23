class Article:

    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self._title = title
        author._articles.append(self)
        magazine._articles.append(self)
        Article.all.append(self)
        print(f"Articles: {self._title}")


        if not isinstance(author, Author):
            raise TypeError("Author must be of type Author.")
        if not isinstance(magazine, Magazine):
            raise TypeError("Magazine should be of type Magazine.")
        if len(title) < 5 or len(title) > 50:
            raise ValueError("Title must be between 5 and 50 characters.")
        if not isinstance(title, str):
            raise TypeError("Title must be a string.")

    
    @property    
    def title(self):
        return self._title
    @title.setter
    def title(self, value):
        pass
        # here we can raise AttributeError("Title cannot be changed after initialization.")

        
class Author:
    def __init__(self, name):
        self._name = name
        self._articles = []
        print(f"Author: {self._name}")

        if not isinstance(name, str):
            raise TypeError("Name must be a string.")
        if len(name.strip()) == 0:
            raise ValueError("Name must be longer than 0 characters.")

        # if hasattr(self, '_name'):
        #     raise AttributeError("Cannot change name after initialisation.")
    
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        pass
        # here we can raise AttributeError("Cannot change name after initialisation.")
        


    def articles(self):
        return self._articles 


    def magazines(self):
        return list({article.magazine for article in self.articles()})

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        if not self._articles:
            return None
        else:
            return list({article.magazine.category for article in self.articles()})

class Magazine:
    def __init__(self, name, category):
        self._name = name
        self.category = category
        self._articles = []
        print(f"Magazine name: {self._name}")
        print(f"Category: {self._category}")
        

    @property
    def name(self):
        return self._name
        
    @name.setter
    def name(self, value):
        if isinstance(value, str) and 2 <= len(value) <= 16:
            self._name = value
    
    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._category = value

    def articles(self):
        return self._articles

    def contributors(self):
        contributors = list({article.author for article in self.articles()})
        if contributors:
            return contributors
        else:
            return None

    def article_titles(self):
        titles = [article.title for article in self.articles()]
        if titles:
            return titles
        else:
            return None

    def contributing_authors(self):
        authors_count = {}
        for article in self.articles():
            author = article.author
            authors_count[author] = authors_count.get(author, 0) + 1

        result = [author for author, count in authors_count.items() if count > 2]

        if result:
            return result
        else:
            return None



author = Author("Carry Bradshaw")
magazine = Magazine("Vogue", "Fashion")
article_1 = Article(author, magazine, "How to wear a tutu with style")
article_2 = Article(author, magazine, "Dating life in NYC")

print(author)
