from python_bootcamp_cloudorbit.chapter3.floating_point_number import FloatingPointNumber


def test_chapter3():
    obj = FloatingPointNumber("-0.5")
    obj2 = FloatingPointNumber("-10.92")
    assert (obj + obj2) == FloatingPointNumber("-11.42")
    assert (obj - obj2) == FloatingPointNumber("10.42")
    assert (obj + 0.5) == FloatingPointNumber("0")
    assert obj != obj2