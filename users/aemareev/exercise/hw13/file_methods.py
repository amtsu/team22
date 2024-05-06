import pickle


class FileMethods:
    def __init__(self, file_name: str = 'default.pickle'):
        self.file_name = file_name

    def dump_obj(self):
        with open(self.file_name, 'wb') as file:
            pickle.dump(self, file)

    @staticmethod
    def load_obj(file_path):
        with open(file_path, 'rb') as file:
            obj = pickle.load(file)
        return obj
