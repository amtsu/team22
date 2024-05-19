import pickle

class PickleHandler:
    @staticmethod
    def save_to_file(obj, filename):
        """Сохраняет объект в файл с помощью pickle."""
        with open(filename, 'wb') as file:
            pickle.dump(obj, file)
    
    @staticmethod
    def load_from_file(filename):
        """Загружает объект из файла с помощью pickle."""
        with open(filename, 'rb') as file:
            return pickle.load(file)