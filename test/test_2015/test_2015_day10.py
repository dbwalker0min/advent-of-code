from io import StringIO

from advent_of_code.year_2015.day_10.day_10 import *

def len_elements(elements: list[str] | str) -> int:
    if isinstance(elements, list):
        return sum(len(element_table[e].sequence) for e in elements)
    else:
        return len_elements(elements.split('.'))

def test_from_element_simple():
    assert look_and_say_element('Fr', 1) == len_elements('Rn')
    assert look_and_say_element('Fr', 2) == len_elements('Ho.At')
    assert look_and_say_element('Fr', 3) == len_elements('Dy.Po')
    assert look_and_say_element('Fr', 4) == len_elements('Tb.Bi')
    assert look_and_say_element('Fr', 5) == len_elements('Ho.Gd.Pm.Pb')
    assert look_and_say_element('Fr', 6) == len_elements('Dy.Eu.Ca.Co.Nd.Tl')
    assert look_and_say_element('Fr', 7) == len_elements('Tb.Sm.K.Fe.Pr.Hg')
    
def test_repeated():
    # Be and Re both decay to Ge. This allows me to test two elements producing the same byproduct
    assert look_and_say_element('Be.Re', 1) == len_elements('Ge.Ca.Li.Ge.Ca.W')
