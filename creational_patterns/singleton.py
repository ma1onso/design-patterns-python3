class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance

        return cls._instances[cls]


class DBConnection(metaclass=SingletonMeta):
    def insert_record_to_table(self):
        print(f'Inserting data to DB with object: {id(self)}')


if __name__ == '__main__':
    first_db_connection = DBConnection()
    second_db_connection = DBConnection()

    print('*' * 10)

    if id(first_db_connection) == id(second_db_connection):
        print("Singleton works, both variables contain the same instance.")
    else:
        print("Singleton failed, variables contain different instances.")

    first_db_connection.insert_record_to_table()
    second_db_connection.insert_record_to_table()
