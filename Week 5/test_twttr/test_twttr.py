from twttr import shorten

def test_words():
    assert shorten("twitter") == "twttr"
    assert shorten("TWITTER") == "TWTTR"

def test_sentences():
    assert shorten("What's your name") == "Wht's yr nm"
    assert shorten("This is CS50") == "Ths s CS50"