from io import StringIO
from advent_of_code.year_2025.day_08 import JunctionBoxes

# this is the published test case
test_case = """162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689
"""

def test_find_min_distance():
    f = StringIO(test_case)

    boxes = JunctionBoxes(f)

    i, j = boxes.find_minimum_distance()
    assert boxes.get_box(i) in ((425,690,689), (162,817,812))
    assert boxes.get_box(j) in ((425,690,689), (162,817,812))

    i, j = boxes.find_minimum_distance()
    assert boxes.get_box(i) in ((431,825,988), (162,817,812))
    assert boxes.get_box(j) in ((431,825,988), (162,817,812))

    i, j = boxes.find_minimum_distance()
    assert boxes.get_box(i) in ((906,360,560), (805,96,715))
    assert boxes.get_box(j) in ((906,360,560), (805,96,715))

    i, j = boxes.find_minimum_distance()
    print(boxes.get_box(i), boxes.get_box(j))
    assert boxes.get_box(i) in ((431,825,988), (425,690, 689))
    assert boxes.get_box(j) in ((431,825,988), (425,690, 689))

    i, j = boxes.find_minimum_distance()
    print(boxes.get_box(i), boxes.get_box(j))
    assert boxes.get_box(i) in ((862, 61, 35), (984, 92, 344))
    assert boxes.get_box(j) in ((862, 61, 35), (984, 92, 344))



def test_make_circuit():
    f = StringIO(test_case)

    boxes = JunctionBoxes(f)

    boxes.make_connection()
    assert boxes.get_circuit_lengths == [2]
    boxes.make_connection()
    assert boxes.get_circuit_lengths == [3]
    boxes.make_connection()
    assert boxes.get_circuit_lengths == [3, 2]
    boxes.make_connection()
    assert boxes.get_circuit_lengths == [3, 2]
    
    boxes.make_connection()
    boxes.make_connection()
    boxes.make_connection()
    boxes.make_connection()
    boxes.make_connection()
    boxes.make_connection()
    # boxes.make_connection()
    assert boxes.get_circuit_lengths == [5, 4, 2, 2]
