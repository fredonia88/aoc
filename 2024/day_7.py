import requests

url = 'https://adventofcode.com/2024/day/7/input'
session = ''
resp = requests.get(url=url, cookies={'session':session})

calibrations = resp.text.splitlines()

#print(calibrations[0])
calibrations = [
    '190: 10 19',
    '3267: 81 40 27',
    '83: 17 5',
    '156: 15 6',
    '7290: 6 8 6 15',
    '161011: 16 10 13',
    '192: 17 8 14',
    '21037: 9 7 18 13',
    '292: 11 6 16 20'
]

def is_valid_equation(test, remainders, symbols):
    base = len(symbols)
    n = len(remainders)

    for combination in range(base**n):
        remainder_total = 0
        temp = combination
        for i in range(n):
            digit = temp % base
            symbol = symbols[digit]
            remainder = remainders[i]
            if i == 0:
                remainder_total += remainder
            elif symbol == '||':
                remainder_total = int(str(remainder_total) + str(remainders[i]))
            elif symbol == '*':
                remainder_total *= remainder
            else:
                remainder_total += remainder
            if remainder_total > test:
                break
            temp //= base
        if remainder_total == test:
            return True
            
    return False

calibration_total = 0
for calibration in calibrations:
    symbols = ['*', '+']
    calibration = calibration.split(':')
    test, remainders = int(calibration[0]), calibration[1].strip().split(' ')
    remainders = [int(remainder) for remainder in remainders]

    if is_valid_equation(test, remainders, symbols):
        calibration_total += test
    else:
        symbols += ['||']
        if is_valid_equation(test, remainders, symbols):
            calibration_total += test

print(calibration_total)