import json


def run(data):
    contents = {"red": 12, "green": 13, "blue": 14}
    games = {}
    results = {}
    ans = 0
    for entry in data:
        game = entry.split(':')[0].strip()
        draws = entry.split(':')[1].split(';')
        games[game] = {}
        results[game] = {}
        results[game]['result'] = True
        results[game]['issues'] = {}
        results[game]['min'] = {}
        i = 0
        for draw in draws:
            games[game][i] = {}
            balls = draw.split(',')
            for ball in balls:
                ball = ball.strip()
                color = ball.split(' ')[1].strip()
                count = int(ball.split(' ')[0].strip())
                games[game][i][color] = count

                if contents[color] < count:
                    results[game]['result'] = False
                    results[game]['issue'] = '%s - %s - %s' % (i, color, count)

                if color not in results[game]['min'].keys():
                    results[game]['min'][color] = count
                elif results[game]['min'][color] < count:
                    results[game]['min'][color] = count

            i = i + 1

    power_sum = 0
    for game, val in results.items():
        if val['result']:
            ans = ans + int(game.split(" ")[1].strip())
        mul = 1
        for color, count in val['min'].items():
            mul = mul * count

        power_sum = power_sum + mul

    print(json.dumps(results, sort_keys=False, indent=4))
    print(ans)
    print(power_sum)


if __name__ == '__main__':
    data = []
    with open('day2.txt') as fh:
        for line in fh:
            data.append(line.strip())

    run(data)
