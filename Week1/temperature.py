import numpy as np


days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

def average(data):
    print('\nThe temperature for the week:')
    for index,temperature in enumerate(data):
        print(f'   {days[index]:10s} {temperature}°C')
    print()
    average = np.round(np.mean(data))
    print(f'The average temperature is: {average}°C')
    print()


def find_max_min(data):
    print(f'\nThe highest temperature is {np.max(data)}°C')
    print(f'The lowest  temperature is {np.min(data)}°C\n')


def convert(data):
    print('\nThe temperatures in Fahrenheit:')
    for temperature in data:
        value = np.round(temperature * 9 / 5 + 32)
        print(f'    {value}°F')
    print()


def filter_days(data):
    print('The days where temperature > 20°C:')
    for index,temperature in enumerate(data):
        if temperature > 20:
            print(f'   {days[index]}')
    print()


if __name__ == '__main__':
    data = [18.5, 19, 20, 25.0, 2, 30, 13.9]
    average(data)
    find_max_min(data)
    convert(data)
    filter_days(data)
