from services import *
import time


tables_init_data = {
    'users': {
        'columns': ['name'],
        'rows': [['Mike'], ['Andy'], ['Tom'], ['Alex']]
    },
    'orders': {
        'columns': ['user_id', 'product'],
        'rows': [
            [1, 'Apple'],
            [1, 'Banana'],
            [1, 'iPhone'],
            [2, 'Book']
        ]
    },
}


def is_table_empty(cursor, name):
        cursor.execute(f'SELECT COUNT(*) FROM {name}')
        result = cursor.fetchone()
        return result[0] == 0


def create_tables():
    conn = sqlite3.connect('app.db')
    cursor = conn.cursor()
    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
        ''')
    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER REFERENCES users(id),
            product TEXT NOT NULL
        )
        ''')
    conn.commit()
    for table_name, rows_columns in tables_init_data.items():
        if is_table_empty(cursor, table_name):
            for row in rows_columns['rows']:    
                cursor.execute(
                    'INSERT INTO {} ({}) VALUES ({})'.format(
                        table_name,
                        ','.join(rows_columns['columns']),
                        ','.join(['?'] * len(row))
                    ),
                    tuple(row))
    conn.commit()
    conn.close()


def main():
    create_tables()
    begin_time = time.time()
    users = UserService().get_user(1)
    orders = OrderService().get_orders(1)
    end_time = time.time()
    print(users)
    print(orders)
    print('time costed:', end_time - begin_time)


if __name__ == '__main__':
    main()