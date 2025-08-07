import numpy as np


def analyse_rainfall(data):
    np_data = np.array(data)
    print(f'\nRainfall as NumPy array: {np_data}')
    print(f'\nTotal: {np_data.sum():.2f} mm')
    print(f'Average: {np_data.mean():.2f} mm')
    print(f'No rain: {len(np.where(np_data == 0)[0])} days')
    day_indices = np.where(np_data > 5)[0]
    print('More than 5 mm:')
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 
            'Friday', 'Saturday', 'Sunday']
    for index in day_indices:
        print(f'\t{index} {days[index]}')
    print()


if __name__ == '__main__':
    sample = [0.0, 5.2, 3.1, 0.0, 12.4, 0.0, 7.5]
    analyse_rainfall(sample)