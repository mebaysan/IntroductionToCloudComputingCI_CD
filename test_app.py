from app import index, greeting

def test_index():
    assert index() == "Introduction to CI & CD | Baysan"


def test_greeting():
    assert greeting('Baysan') == "Hello, Baysan!"