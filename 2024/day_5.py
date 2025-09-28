import requests

url = 'https://adventofcode.com/2024/day/5/input'
#session = '' # get from cookie
session = '53616c7465645f5f56206da822b1dc5378b576457012dc580f82a7780ed3c46b8e1d7004abca6f15d97290ea0df401b2f0ab2cbdbfa38901ffbc2dbf2e50354d'
res = requests.get(url=url, cookies={'session': session})
res = res.text.splitlines()

# Part 1
res.index('') # 1176
page_rules = set(res[:1176])
page_updates = res[1177:]

updates = [update.split(',') for update in page_updates]

total = 0
for update in updates:
    in_order = True
    update_copy = update.copy()
    while len(update_copy) > 1:
        order = str(update_copy[0]) + '|' + str(update_copy[1])
        if order not in page_rules:
            in_order = False
            break
        update_copy.pop(0)
    if in_order:
        i = len(update) // 2
        total += int(update[i])

print(total)