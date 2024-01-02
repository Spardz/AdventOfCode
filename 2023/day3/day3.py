import json
import re


def execute_sum(data):
    i = 0
    nums = {}
    tot = 0
    for l in data:
        entry = l.strip()
        print(entry)
        match_num = re.finditer(r'\d+', entry)

        for match in match_num:
            start_match = match.start()
            end_match = match.end()
            len_match = end_match - start_match
            print('%s - %s - %s' % (entry[start_match:end_match], start_match, len_match))

            start_col = 0
            end_col = len(entry) - 1

            if start_match != 0:
                start_col = start_match - 1

            if start_match + len_match < end_col:
                end_col = start_match + len_match

            print(start_col)
            print(end_col)

            if i > 0:
                start_row = i - 1
            else:
                start_row = 0

            if i == len(data) - 1:
                end_row = i
            else:
                end_row = i + 1

            broke = False
            for j in range(start_row, end_row + 1):
                if broke:
                    break
                for k in range(start_col, end_col + 1):
                    if j != i or (j == i and not (start_col < k < end_col)):
                        print('J: %s - K: %s - %s - %s' % (j, k, data[j][k], data[j][k] != '.' and not data[j][k].isnumeric()))
                        if not(data[j][k] == '.' or data[j][k].isnumeric()):
                            print('Adding: %s to %s' % (entry[start_match:end_match], tot))
                            nums[entry[start_match:end_match]] = True
                            tot = tot + int(entry[start_match:end_match])
                            print(tot)
                            broke = True
                            break
        i = i + 1

    print(json.dumps(nums, sort_keys=False, indent=4))
    print(tot)


def execute_mul_error(data):
    i = 0
    nums = {}
    tot = 0
    for l in data:
        entry = l.strip()
        print(entry)
        match_num = re.finditer(r'\d+', entry)

        for match in match_num:
            start_match = match.start()
            end_match = match.end()
            len_match = end_match - start_match
            print('%s - %s - %s' % (entry[start_match:end_match], start_match, len_match))

            start_col = 0
            end_col = len(entry) - 1

            if start_match != 0:
                start_col = start_match - 1

            if start_match + len_match < end_col:
                end_col = start_match + len_match

            print(start_col)
            print(end_col)

            if i > 0:
                start_row = i - 1
            else:
                start_row = 0

            if i == len(data) - 1:
                end_row = i
            else:
                end_row = i + 1

            broke = False
            gear_row = -1
            gear_col = -1
            for j in range(start_row, end_row + 1):
                if broke:
                    break
                for k in range(start_col, end_col + 1):
                    if j != i or (j == i and not (start_col < k < end_col)):
                        print('J: %s - K: %s - %s - %s' % (j, k, data[j][k], data[j][k] == '*'))
                        if data[j][k] == '*':
                            print('Found Gear at J: %s - K: %s' % (j, k))
                            gear_row = j
                            gear_col = k
                            broke = True
                            break

            if broke:
                start_col = gear_col
                end_col = len(entry) - 1

                '''if gear_col != 0:
                    start_col = gear_col - 1'''

                if gear_col + 1 < end_col:
                    end_col = gear_col + 1

                print(start_col)
                print(end_col)

                if gear_row > 0:
                    start_row = gear_row - 1
                else:
                    start_row = 0

                if gear_row == len(data) - 1:
                    end_row = gear_row
                else:
                    end_row = gear_row + 1

                for j in range(start_row, end_row + 1):
                    match_sec_num = re.finditer(r'\d+', data[j])
                    for sec_num_match in match_sec_num:
                        if sec_num_match.start() <= start_col <= sec_num_match.end() or sec_num_match.start() <= end_col <= sec_num_match.end():
                            if not(j == i and sec_num_match.start() == start_match and sec_num_match.end() == end_match):
                                check = int(entry[start_match:end_match]) * int(data[j][sec_num_match.start():sec_num_match.end()])
                                if check not in nums.keys():
                                    print('Found second part - %s' % data[j][sec_num_match.start():sec_num_match.end()])
                                    nums[check] = '%s * %s' % (entry[start_match:end_match], data[j][sec_num_match.start():sec_num_match.end()])
                                    print('\tAdding %s * %s = %s to total %s' % (entry[start_match:end_match], data[j][sec_num_match.start():sec_num_match.end()], check, tot))
                                    tot = tot + check

        i = i + 1

    print(json.dumps(nums, sort_keys=False, indent=4))
    print(tot)


def execute_mul_working(data):
    i = 0
    nums = {}
    tot = 0
    for l in data:
        entry = l.strip()
        print(entry)
        match_num = re.finditer(r'\*', entry)

        for match in match_num:
            start_match = match.start()
            end_match = match.end()
            len_match = end_match - start_match
            print('%s - %s - %s' % (entry[start_match:end_match], start_match, len_match))

            start_col = start_match - 1
            end_col = len(entry) - 1

            if start_match + len_match < end_col:
                end_col = start_match + len_match

            print(start_col)
            print(end_col)

            if i > 0:
                start_row = i - 1
            else:
                start_row = 0

            if i == len(data) - 1:
                end_row = i
            else:
                end_row = i + 1

            num1 = -1
            num2 = -1
            for j in range(start_row, end_row + 1):
                match_sec_num = re.finditer(r'\d+', data[j])
                for sec_num_match in match_sec_num:
                    if sec_num_match.start() <= start_col + 1 <= sec_num_match.end() or sec_num_match.start() <= end_col <= sec_num_match.end():
                        if num1 == -1:
                            print('Found part1 - %s' % data[j][sec_num_match.start():sec_num_match.end()])
                            num1 = data[j][sec_num_match.start():sec_num_match.end()]
                        elif num2 == -1:
                            print('Found part2 - %s' % data[j][sec_num_match.start():sec_num_match.end()])
                            num2 = data[j][sec_num_match.start():sec_num_match.end()]
                            check = int(num1) * int(num2)
                            nums[check] = '%s * %s' % (num1, num2)
                            print('\tAdding %s * %s = %s to total %s' % (num1, num2, check, tot))
                            tot = tot + check
        i = i + 1

    print(json.dumps(nums, sort_keys=False, indent=4))
    print(tot)


if __name__ == '__main__':
    data = []
    with open('day3.txt') as fh:
        for line in fh:
            data.append(line.strip())

    execute_mul_working(data)
