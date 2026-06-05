from cython_template_uv import add

# very dirty, yet simple and effective test
def test_add() -> None:
    assert add(1, 2) == 3
