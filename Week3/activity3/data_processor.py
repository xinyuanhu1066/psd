import io
import numpy as np
import pandas as pd
import pyarrow.parquet as pq


class DataProcessor:
    def __init__(self, file_path, column_names):
        self.file_path = file_path
        self.column_names = column_names
        self.columns = []

    def csv_to_parquet(self):
        """Convert CSV format to Parquet format."""
        # Read CSV file and convert the data into pandas DataFrame format
        csv_data = pd.read_csv(self.file_path)
        # Create bytes buffer which is a file-like object, needed by read_table()
        parquet_buf = io.BytesIO()
        # Convert DataFrame format to Parquet format, store the result in file-like buffer
        csv_data.to_parquet(parquet_buf)
        # Read column data for user specified column names
        table = pq.read_table(parquet_buf, columns=self.column_names)
        for chunkarray in table.columns:
            # Use to_pylist() to convert ChunkedArray to normal list
            # Then create numpy array from this normal list
            column_data = np.array(chunkarray.to_pylist())
            self.columns.append(column_data)

    def find_maximum(self):
        """Find the maximum value of each column."""
        print('\nMaximum value of columns\n{}'.format('-' * 100))
        for index, name in enumerate(self.column_names):
            print('{:10s}{}'.format(name + ':', self.columns[index].max()))

    def find_minimum(self):
        """Find the minimum value of each column."""
        print('\nMinimum value of columns\n{}'.format('-' * 100))
        for index, name in enumerate(self.column_names):
            print('{:10s}{}'.format(name + ':', self.columns[index].min()))

    def find_average(self):
        """Compute the average value of each column."""
        print('\nAverage value of columns\n{}'.format('-' * 100))
        for index, name in enumerate(self.column_names):
            print('{:10s}{}'.format(name + ':', self.columns[index].mean()))

    def get_abs_value(self):
        """Compute the absolute values for each column."""
        print('\nAbsolute values for columns\n{}'.format('-' * 100))
        for index, name in enumerate(self.column_names):
            print('{:10s}\n\n{}\n'.format(name + ':', np.abs(self.columns[index])))


if __name__ == '__main__':
    processor = DataProcessor(
        'forestfires.csv', 
        ['X', 'Y', 'FFMC', 'DMC', 'DC', 'ISI', 
         'temp', 'RH', 'wind', 'rain', 'area'])
    processor.csv_to_parquet()
    processor.find_maximum()
    processor.find_minimum()
    processor.find_average()
    processor.get_abs_value()
