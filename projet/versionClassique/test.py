def test(test):
    res=False
    if isinstance(test, int):
        res=True
    return res
print(test('r'))
