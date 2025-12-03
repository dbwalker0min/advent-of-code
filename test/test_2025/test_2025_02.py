from io import StringIO
from advent_of_code.year_2025.day_02.day_02 import (
    validate_code,
    validate_range,
    parse_ranges,
    validate_ranges,
    validate_code2,
    find_all_factors,
)


test_file_contents = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"


def test_invalid_codes():
    invalid_codes = [55, 6464, 123123, 123456123456]

    for code in invalid_codes:
        assert not validate_code(code), f"Code {code} should be invalid"


def test_valid_codes():
    valid_codes = [
        101,
        1234,
        7830,
    ]

    for code in valid_codes:
        assert validate_code(code), f"Code {code} should be valid"


def test_range():
    ranges = [
        dict(range_=(11, 22), invalid_sum=33),
        dict(range_=(95, 115), invalid_sum=99),
        dict(range_=(998, 1012), invalid_sum=1010),
        dict(range_=(1188511880, 1188511890), invalid_sum=1188511885),
        dict(range_=(222220, 222224), invalid_sum=222222),
        dict(range_=(1698522, 1698528), invalid_sum=0),
        dict(range_=(446443, 446449), invalid_sum=446446),
        dict(range_=(38593856, 38593862), invalid_sum=38593859),
    ]

    for r in ranges:
        sum_invalid = validate_range(r["range_"])
        assert sum_invalid == r["invalid_sum"], (
            f"Sum error in range {r['range_']}. Got {sum_invalid}, should be {r['invalid_sum']}"
        )


def test_parse_ranges():
    expected_ranges = [
        (11, 22),
        (95, 115),
        (998, 1012),
        (1188511880, 1188511890),
        (222220, 222224),
        (1698522, 1698528),
        (446443, 446449),
        (38593856, 38593862),
        (565653, 565659),
        (824824821, 824824827),
        (2121212118, 2121212124),
    ]
    ranges = parse_ranges(StringIO(test_file_contents))

    for r, e in zip(ranges, expected_ranges):
        assert r == e, f"Expected {e}, received {r}"


def test_test_case():
    ranges = parse_ranges(StringIO(test_file_contents))

    assert validate_ranges(ranges) == 1227775554


def test_invalid_codes2():
    invalid_codes = [
        12341234,
        123123123,
        12121212,
        1111111,
    ]

    for c in invalid_codes:
        assert not validate_code2(c), f"Code {c} should be invalid"


def test_range2():
    ranges = [
        dict(range_=(11, 22), invalid_sum=33),
        dict(range_=(95, 115), invalid_sum=210),
        dict(range_=(998, 1012), invalid_sum=999 + 1010),
        dict(range_=(1188511880, 1188511890), invalid_sum=1188511885),
        dict(range_=(222220, 222224), invalid_sum=222222),
        dict(range_=(1698522, 1698528), invalid_sum=0),
        dict(range_=(446443, 446449), invalid_sum=446446),
        dict(range_=(38593856, 38593862), invalid_sum=38593859),
        dict(range_=(565653, 565659), invalid_sum=565656),
        dict(range_=(824824821, 824824827), invalid_sum=824824824),
        dict(range_=(2121212118, 2121212124), invalid_sum=2121212121),
    ]

    for r in ranges:
        sum_invalid = validate_range(r["range_"], version=2)
        assert sum_invalid == r["invalid_sum"], (
            f"Sum error in range {r['range_']}. Got {sum_invalid}, should be {r['invalid_sum']}"
        )


def test_test_case2():
    ranges = parse_ranges(StringIO(test_file_contents))

    assert validate_ranges(ranges, version=2) == 4174379265


def test_all_multiples():
    mult = find_all_factors(100)
    assert mult == [1, 2, 4, 5, 10, 20, 25, 50]
