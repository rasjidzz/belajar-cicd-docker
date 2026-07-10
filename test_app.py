from app import greet, add

def test_greet():
    assert greet("Alice") == "Hello, Alice!"
    assert greet("Bob") == "Hello, Bob!"

def test_add():
    assert add(1, 2) == 3
    assert add(2, 3) == 5
    assert add(0, 0) == 0
    assert add(-1, 4) == 3
    assert add(2, 100) == 102