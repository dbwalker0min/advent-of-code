from io import StringIO

from advent_of_code.year_2015.day_09.day_09 import *

input_test = '''
London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141
'''

def test_get_distance():
    f = StringIO(input_test.strip('\n'))
    loc = Locations(f)
    assert loc.distance('London', 'Dublin') == 464
    assert loc.distance('London', 'Belfast') == 518
    assert loc.distance('Dublin', 'Belfast') == 141
    assert loc.distance('Dublin', 'London') == 464
    assert loc.distance('Belfast', 'London') == 518
    assert loc.distance('Belfast', 'Dublin') == 141

    assert 'London' in loc.cities
    assert 'Dublin' in loc.cities
    assert 'Belfast' in loc.cities

def test_shortest_distance():
    f = StringIO(input_test.strip('\n'))
    loc = Locations(f)

    min_dist, order = loc.min_distance_all()
    assert order == ("London", "Dublin", "Belfast")
    assert min_dist == 605

def test_max_distance():
    f = StringIO(input_test.strip('\n'))
    loc = Locations(f)

    max_dist, order = loc.max_distance_all()
    assert order == ("Dublin", "London", "Belfast") or order == ("Belfast", "London", "Dublin")
    assert max_dist == 982
