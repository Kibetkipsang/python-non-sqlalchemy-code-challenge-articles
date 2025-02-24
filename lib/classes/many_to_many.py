class Article:

    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self._title = title

        #here we will add the article to the authors list and also magazine list
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
        #here we are preventing changing of the title after initialization
    @title.setter
    def title(self, value):
        pass
        # here we can raise AttributeError("Title cannot be changed after initialization.")

        
class Author:
    def __init__(self, name):
        self._name = name
        #below is the list to store articles written by the author
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
        

       #here we return articles written by the author
    def articles(self):
        return self._articles 

        #here we return list of magazines the aothor has contributed to
    def magazines(self):
        return list({article.magazine for article in self.articles()})
    #here we can add new articles
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
        self._articles = [] #this will store articles in this magazine
        print(f"Magazine name: {self._name}")
        print(f"Category: {self._category}")
        
    #gets the magazine name
    @property
    def name(self):
        return self._name
    #sets the magazine name
    @name.setter
    def name(self, value):
        if isinstance(value, str) and 2 <= len(value) <= 16:
            self._name = value
    #gets the magazine category
    @property
    def category(self):
        return self._category
    #sets the magazine category and validates it 
    @category.setter
    def category(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._category = value
    #returns the list for articles in the magazine
    def articles(self):
        return self._articles
    #here we return the list of contributors to the magazine
    def contributors(self):
        contributors = list({article.author for article in self.articles()})
        if contributors:
            return contributors
        else:
            return None
    #we return the titles of the articles
    def article_titles(self):
        titles = [article.title for article in self.articles()]
        if titles:
            return titles
        else:
            return None
     #here we return the authors who have written more than two articles
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
