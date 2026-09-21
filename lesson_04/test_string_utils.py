import pytest
from string_utils import StringUtils

utils = StringUtils()

@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),           
    ("Skypro", "Skypro"),            
    ("", ""),                        
    ("123", "123")                  
])
def test_capitalize(input_str, expected):
    assert utils.capitalize(input_str) == expected

@pytest.mark.parametrize("input_str, expected", [
    ("   skypro", "skypro"),         
    ("   skypro", "skypro"),          
    ("  hello world", "hello world"), 
     ("", ""),                        
     ("", ""),                         
    ("   ", "")                      
])
def test_trim(input_str, expected):
    assert utils.trim(input_str) == expected

@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "S", True),          
    ("SkyPro", "P", True),           
    ("SkyPro", "U", False),          
    ("", "S", False)                 
])
def test_contains(string, symbol, expected):
    assert utils.contains(string, symbol) == expected


@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "k", "SyPro"),        
    ("SkyPro", "Pro", "Sky"),        
    ("SkyPro", "x", "SkyPro"),       
    ("", "a", "")                    
])
def test_delete_symbol(string, symbol, expected):
    assert utils.delete_symbol(string, symbol) == expected