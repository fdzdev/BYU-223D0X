from src.dynarray import DynArray


def test_append_and_index():
    a = DynArray()
    for i in range(50):
        a.append(i)
    assert len(a) == 50
    assert a[49] == 49
