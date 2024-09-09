class Article:

    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, new_title):
        if isinstance(new_title, str) and (50 >= len(new_title) >= 5) and not hasattr(self, '_title'):
            self._title = new_title
    
    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, new_author):
        if isinstance(new_author, Author):
            self._author = new_author
    
    @property
    def magazine(self):
        return self._magazine
    
    @magazine.setter
    def magazine(self, new_magazine):
        if isinstance(new_magazine, Magazine):
            self._magazine = new_magazine

class Author:
    def __init__(self, name):
        self.name = name
    
    @property
    def name(self):
        return self._name
    
    @name.setter 
    def name(self, new_name):
        if isinstance(new_name, str) and len(new_name) > 0 and not hasattr(self, '_name'):
            self._name = new_name
        # else:
        #     raise ValueError()   


    def articles(self):
        return [a for a in Article.all if a.author is self]

    def magazines(self):
        return list(set([a.magazine for a in self.articles()]))

    def add_article(self, magazine, title):
        if isinstance(magazine, Magazine):
            new_article = Article(self, magazine, title)
        return new_article

    def topic_areas(self):
        if not self.magazines():
            return None
        return list(set([magazine.category for magazine in self.magazines()]))

class Magazine:
    all = []

    def __init__(self, name, category):
        self.name = name
        self.category = category
        Magazine.all.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and (16 >= len(new_name) >= 2):
            self._name = new_name

    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, new_category):
        if isinstance(new_category, str) and len(new_category) > 0:
            self._category = new_category
    

    def articles(self):
        return [a for a in Article.all if a.magazine is self]

    def contributors(self):
        return list(set([m.author for m in self.articles()]))

    def article_titles(self):
        if not self.articles():
            return None
        return [article.title for article in self.articles()]

    def contributing_authors(self):

        counts = {}

        for article in self.articles():
            if article.author not in counts:
                counts[article.author] = 1  # new key/value pair --> key = Author object, value = count
            else:
                counts[article.author] += 1 # increment existing count

        filtered_authors = []

        for author in counts:
            if counts[author] > 2:                   # if the counter for author key is more than 2
                filtered_authors.append(author)      # then append the object to filtered list

        if len(filtered_authors) == 0:
            return None
        return filtered_authors
 