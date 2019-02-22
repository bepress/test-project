import json
import string
import time
import datetime
import random
import copy

def pk(start = 0, step = 1):
    # this ia a generator for the primary key generation
    # it can be more complex and it should inicialized from a 
    # given start, eg. from a database of preexistent records
    n = start
    while True:
        yield n
        n = n + step

class User(object):
    # class to pass one pre-defined fixture
    def __init__(self):
        self.pk = True

class Metadata(object):
    """

    Class Metadata - contains metadata information of kinds and category objects.
    """

    kinds_categories = {'journal': ['Read', 'Travel', 'Food', 'Art', 'Auto'], 'book': ['textbook','anthology','cookbook','scientific','literature']}
 
    def __init__(self, pk,  title = '', url = None, kind = '', category = ''):
        self.pk = pk # this should be an integer is only included in the testing, but it can be validated here to like title
        self.title = title
        if url:
            self.url = 'https://'
        else: 
            self.url = 'http://www.google.com/search?keywords=' + self.title
        self.kind = self.initialize_kind()
        self.category = self.initialize_category(self.kind)
        self.datetime_create = datetime.datetime.now()
        self.datetime_update = str(time.time())
         
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, newtitle):
        if not isinstance(newtitle, str):
            raise TypeError('Expected str for title')
        if newtitle == '':
            raise TypeError('Expected a str not null')
        self._title = newtitle

    @property
    def datetime_create(self):
        return self._datetime_create.strftime("%m-%d-%y %H:%M:%S")

    @datetime_create.setter
    def datetime_create(self, newdate):

        # here includes validation for datetime and str 
        if isinstance(newdate, type(datetime.datetime.now())):
            self._datetime_create = newdate
        if isinstance(newdate, str):
            self._datetime_create = datetime.datetime.strptime(newdate.split()[0],'%m-%d-%y')

    @property
    def datetime_update(self):
        return self._datetime_update

    @datetime_update.setter
    def datetime_update(self, newdate):
        if not isinstance(newdate, str):
            raise TypeError('Expected other value for newdate')
        # here can go additional validation for dates properly
        self._datetime_update = newdate

    def __str__(self):
        return '{} - {} - {} - {}'.format(self.title, self.url, self.kind, self.category)

    def toJSON(self):
        attributes = ['pk', 'title', 'url', 'kind', 'category', 'datetime_create', 'datetime_update']
        r = {}
        for attr in attributes:
            r.update({k: v for k,v in (zip([attr],[getattr(meta_data[0],attr)]))})
        print(json.dumps(r,sort_keys = False, indent = 4))

    @classmethod
    def initialize_kind(cls):
        kinds = list(cls.kinds_categories.keys())
        return kinds[random.randint(0,len(kinds)-1)]

    @classmethod
    def initialize_category(cls, kind):
        categories = list(cls.kinds_categories[kind])
        return categories[random.randint(0,len(categories)-1)]

def bulk(toBulk, n = 200):
    for i in range(len(toBulk)):
        if i < n:
            print(toBulk[i])
            
class Filter(object):
    """
    
    Class to apply filters for criteria and values.
    """
    def __init__(self, toFilter, criteria, values):
        self.tofilter = toFilter
        self.criteria = criteria
        self.values = values
        self.filter_metadata()

    def filter_metadata(self):
        if len(self.tofilter) == 0:
            pass 
        else: 
            for i in range(len(self.criteria)):
                toFilter = copy.deepcopy([x for x in self.tofilter if getattr(x, self.criteria[i]) == self.values[i]])
        self.tofilter = toFilter

def filterfunction(tofilter, criteria, values):
    """
    
    Filters the list of metadata according to criteria and their values.
    """
    if len(tofilter) == 0:
        return []
    else: 
        for i in range(len(criteria)):
            toFilter = copy.deepcopy([x for x in tofilter if getattr(x, criteria[i]) == values[i]])
    return toFilter

def paginate(toPaginate, n):
    """
    
    Paginates the list of metadata in pages of size n. 
    """
    return [toPaginate[i:i+n] for i in range(0,len(toPaginate),n)]

if __name__ == "__main__":
    
    primary_key = pk()
    # let's create metadata
    m = Metadata(next(primary_key), 'Some title') #  Cretes a Metadata with validators included      
    n_metadata = 10000
    meta_data = []
    # generate metadata and send to a simple list
    for i in range(n_metadata):
        random_title = ''.join(random.choices(string.ascii_uppercase, k=10))
        meta_data.append(Metadata(next(primary_key), title=random_title))

    print(len(meta_data))
    # Filtering the metadata
    # First filtering general 1 criteria
    f = filterfunction(meta_data, ['kind'], ['book'])
    print(len(f))
    # Second filter more specific 2 criteria
    h = filterfunction(meta_data, ['kind','category'], ['book','textbook'])
    print(len(h))
    # Pagination of the metadata
    n = 200
    g = paginate(f, n)
    print('Number of pages: {} of length: {} '.format(len(g), n))
    bulk(meta_data, 10)
    bulk(list(g[-1]))

