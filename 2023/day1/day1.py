import re


def find_and_sum(val):
    rep_dict = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }
    regex = '(?=(%s))' % '|'.join(rep_dict.keys())

    match_num = re.findall(r'\d', val)
    match_text = re.findall(regex, val)

    if len(match_num) == 0:
        start = rep_dict[match_text[0]]
        end = rep_dict[match_text[-1]]
    elif len(match_text) == 0:
        start = match_num[0]
        end = match_num[-1]
    else:
        if val.find(match_num[0]) < val.find(match_text[0]):
            start = match_num[0]
        else:
            start = rep_dict[match_text[0]]

        if val.rfind(match_num[-1]) < val.rfind(match_text[-1]):
            end = rep_dict[match_text[-1]]
        else:
            end = match_num[-1]

    return int(start) * 10 + int(end)


def run(cal_in):
    total = 0
    for entry in cal_in:
        print(entry)
        out = find_and_sum(entry)
        print(out)
        total = total + out

    print(total)


if __name__ == '__main__':
    cal_in = []
    with open('day1.txt') as fh:
        for line in fh:
            cal_in.append(line.strip())

    run(cal_in)
