import pytest

from functions import *

def test_select_genre_pop():
    assert select_genre('pop') == 'pop'

def test_select_genre_rock():
    assert select_genre('rock') == 'rock'

def test_select_genre_invalid():
    with pytest.raises(ValueError) as e:        
        select_genre('rap')	
	
def test_remove_punctuation():
	assert remove_punctuation('test!^') == 'test'

def test_string_concatenator():
    assert string_concatenator("test", "train", " o ") == 'test o train'


	



