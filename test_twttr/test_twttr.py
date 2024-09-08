import twttr

def test_shorten():
    assert twttr.shorten("hello") == "hll"
    assert twttr.shorten("world") == "wrld"
    assert twttr.shorten("tweet") == "twt"
    assert twttr.shorten("ana.") == "n."
    assert twttr.shorten("life1") == "lf1"
    assert twttr.shorten("Apple") == "ppl"
