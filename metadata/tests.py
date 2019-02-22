import types
import pytest
import random
import sys
import os
import string 

"""

This module include the testing for Metadata
"""

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from models import Metadata, User, Filter

@pytest.fixture
def setup():
    print("\nSetting up!")

def test_test():
    assert True

def test_create_metadata():
    m = Metadata(random.randint(1,10), 'Some title')
    assert isinstance(m, Metadata) 

def test_create_empty_metadata():
    with pytest.raises(TypeError):
        m = Metadata()

def test_create_no_title_metadata():
    with pytest.raises(TypeError):
        m = Metadata(10)

def test_create_no_primary_key_metadata():
    with pytest.raises(TypeError):
        m = Metadata(title='Some title')

def test_create_non_int_primary_key_metadata():
    assert True

def test_create_metadata_and_verify_filters():
    def pk():
        n = 0
        step = 1
        while True:
            yield n
            n = n + step

    meta_data = [] # contains metadata 

    n = 1000 
    primary_key = pk()
    for _ in range(n):
        random_title = ''.join(random.choices(string.ascii_uppercase, k=10))
        meta_data.append(Metadata(next(primary_key), title=random_title))

    f = Filter(meta_data,['kind'],['book'])
    assert len(meta_data) > len(f.tofilter)

    g = Filter(meta_data,['kind','category'],['book','textbook'])

    assert len(meta_data) > len(g.tofilter)
    assert len(f.tofilter) > len(g.tofilter)

@pytest.fixture
def admin_user():
    user = User()
    return user

def test_db(admin_user):
    assert admin_user.pk

