from abc import ABC, abstractmethod
from dataclasses import dataclass


class DataSource(ABC):
    @abstractmethod
    def write_data(self):
        raise NotImplementedError
    
    @abstractmethod
    def read_data(self):
        raise NotImplementedError
    
    

@dataclass
class FileDataSource(DataSource):
    filename: str

    def write_data(self, data):
        print(f'👩‍💻 Writing {self.filename} to disk')

    def read_data(self):
        print(f'🙌 Open the content file of {self.filename}')

        return '🗃️'


@dataclass
class DataSourceDecorator(DataSource):
    _wrappee: DataSource

    def write_data(self, data):
        self._wrappee.write_data(data)

    def read_data(self):
        return self._wrappee.read_data()


class EncryptionDecorator(DataSourceDecorator):
    def write_data(self, data):
        print(f'Encrypted data and passing it to write method')
        super().write_data(data)
    
    def read_data(self):
        data = super().read_data()
        print(f'Decrypted data')

        return data
    
class CompressionDecorator(DataSourceDecorator):
    def write_data(self, data):
        print(f'Compressed data and passing it to write method')
        super().write_data(data)
    
    def read_data(self):
        data = super().read_data()
        print(f'Decompressed data')

        return data


# Option 2. Client code that uses an external data source.
# SalaryManager objects neither know nor care about data
# storage specifics. They work with a pre-configured data
# source received from the app configurator.
@dataclass
class RecipeManager:
    source: DataSource

    def load(self):
        return self.source.read_data()

    def save(self, data):
        self.source.write_data(data)


@dataclass
class ApplicationConfigurator:
    enabled_encryption: bool = True
    enabled_compression: bool = True

    def recipes_configuration(self):
        bread_recipes = {'recipe 1': 'steps'}

        source_file = FileDataSource('recipes.txt')

        if (self.enabled_encryption):
            source_file = EncryptionDecorator(source_file)
        if (self.enabled_compression):
            source_file = CompressionDecorator(source_file)

        recipe_manager = RecipeManager(source_file)
        recipe_manager.save(bread_recipes)
        recipes_data = recipe_manager.load()

        print(recipes_data)


if __name__ == '__main__':
    # Option 1. A simple example of a decorator assembly.
    print('*' * 30)
    print ('Example 1')
    print('*' * 30)
    bread_recipes = {'recipe 1': 'steps'}

    source_file = FileDataSource('bread_recipes.txt')
    source_file.write_data(bread_recipes)

    compressed_file = CompressionDecorator(source_file)
    compressed_file.write_data(bread_recipes)

    encrypted_file = EncryptionDecorator(compressed_file)
    encrypted_file.write_data(bread_recipes)

    print(f'Real data: {encrypted_file.read_data()}')

    print('*' * 30)
    print ('Example 2')
    print('*' * 30)
    # Option 2.
    app_configurator = ApplicationConfigurator()
    app_configurator.recipes_configuration()