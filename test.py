from payment import calculate as cal

def test(a, b):
    c = cal(a, b)

    test_a = a + b

    assert c == test_a

test(11, 22)
test(2, 16)
test(50, 1632)