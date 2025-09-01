import requests

session = '' # get session id from cookie
url = 'https://adventofcode.com/2024/day/2/input'

res = requests.get(url, cookies={'session': session})
res.raise_for_status()
reports = res.text.strip().splitlines()

def diff(x, y):
    return (x > y) - (x < y)

def valid_level(direction, levels):
    anchor = levels[0]
    for level in levels[1:]:
        if diff(level, anchor) != direction:
            return False
        if not 3 >= abs(level - anchor) >= 1:
            return False
        anchor = level
    return True

def is_safe_report(report, new_report, i=0):
    direction = diff(new_report[1], new_report[0])
    if direction != 0 and valid_level(direction, new_report):
        return True
    if i > len(report) - 1:
        return False
    new_report = report.copy()
    new_report.pop(i)
    if is_safe_report(report, new_report, i+1):
        return True
    else:
        return False

safe_count = 0
for report in reports:
    report = list(map(int, report.split(' ')))
    if is_safe_report(report, report):
        safe_count += 1

print(safe_count)
