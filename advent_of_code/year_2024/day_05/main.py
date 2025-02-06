from advent_of_code.year_2024.day_05 import PageRules

def main():
    obj = PageRules()
    fom = 0
    with open('input_data.txt') as fid:
        obj.read_file(fid)

    for s in obj.sequences:
        if obj.check_sequence(s):
            fom += s[len(s) // 2]
    print(fom)


if __name__ == '__main__':
    main()