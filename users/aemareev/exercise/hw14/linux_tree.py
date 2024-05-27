class File:
    def __init__(self, name: str, size: int | float, directory):
        self.name = name
        self.directory: Directory = directory
        self.size = size

    def __str__(self):
        return self.name


class Directory:
    def __init__(self, name: str, directory=None):
        self.name = name
        self.directory: Directory | None = directory
        self.attachments: list[Directory | File] = []
        self.size = 4

    def __str__(self):
        return f'\033[1;34m{self.name}\033[0m'


class LinuxTree:
    def __init__(self):
        self.root = Directory('root')
        self.current_directory = self.root

    def mkdir(self, name: str):
        self.current_directory.attachments.append(Directory(name.lower(), self.current_directory))

    def mkfile(self, name: str, size: int | float):
        self.current_directory.attachments.append(File(name.lower(), size, self.current_directory))

    def pwd(self) -> str:
        path = '/' + self.current_directory.name + '/'
        buf = self.current_directory
        while buf.directory:
            path = '/' + buf.directory.name + path
            buf = buf.directory
        return path

    def cd(self, target: str):
        if target == '..' and self.current_directory.name != 'root':
            self.current_directory = self.current_directory.directory
        elif target == '/':
            self.current_directory = self.root
        else:
            for node in self.current_directory.attachments:
                if isinstance(node, Directory) and node.name == target:
                    self.current_directory = node
                    break
            else:
                raise ValueError(f'Каталога или команды "{target}" не существует!')

    def rm(self, name):
        for node in self.current_directory.attachments:
            if node.name == name:  # сделать валидацию уникального имени при создании узлов
                self.current_directory.attachments.remove(node)
                break
        else:
            raise ValueError(f'Каталога или файла "{name}" не существует!')

    def ls(self) -> list[Directory | File] | None:
        if self.current_directory.attachments:
            return [node for node in self.current_directory.attachments]
        else:
            return None

    def search(self, part_of_filename: str) -> list[str]:
        def search_func(filename: str, directory: Directory, lst: list[str], filepath: str) -> list[str]:
            if directory.attachments:
                for node in directory.attachments:
                    if isinstance(node, File):
                        if filename in node.name:
                            lst.append(filepath + '/' + node.name)
                    else:
                        filepath += '/' + node.name
                        search_func(filename, node, lst, filepath)
            return lst

        result = []
        path = 'root'
        search_func(part_of_filename, self.root, result, path)
        return result

    def du(self) -> list[tuple]:
        def get_dir_size(directory: Directory):
            dir_sum = 0
            if directory.attachments:
                for node in directory.attachments:
                    if isinstance(node, File):
                        dir_sum += node.size
                    else:
                        dir_sum += node.size + get_dir_size(node)
            return dir_sum

        result_list = [('.', get_dir_size(self.current_directory))]

        if self.current_directory.attachments:
            for attach in self.current_directory.attachments:
                if isinstance(attach, File):
                    result_list.append((attach.name, attach.size))
                else:
                    node_sum = get_dir_size(attach) + attach.size
                    result_list.append((attach.name, node_sum))

        return result_list


if __name__ == '__main__':
    separator = '=' * 100
    my_os = LinuxTree()

    # проверка создания папок и файлов в текущей директории
    my_os.mkfile('root_lvl_file', 128)
    my_os.mkdir('root_lvl_dir_1')
    my_os.mkdir('root_lvl_dir_1')
    assert len(my_os.current_directory.attachments) == 3
    assert len(my_os.ls()) == 3

    # проверка вывода списка папок и файлов в текущей директории
    print(f'Директория {my_os.current_directory}:')
    print(*my_os.ls(), sep='\n')
    print(separator)

    # проверка смены текущей директории на уровень ниже
    # проверка вывода полного пути к текущей директории
    my_os.cd('root_lvl_dir_1')
    assert my_os.pwd() == '/root/root_lvl_dir_1/'

    # проверка создания папок и файлов в подкаталоге (текущем)
    my_os.mkdir('2nd_lvl_dir_1')
    my_os.mkfile('2nd_lvl_file', 128)
    assert len(my_os.ls()) == 2

    # переход в созданную ранее директорию, проверка создания папки и удаление папки
    my_os.cd('2nd_lvl_dir_1')
    my_os.mkdir('123')
    assert len(my_os.ls()) == 1
    my_os.rm('123')
    assert my_os.ls() is None

    # проверка функции поиска файлов по части имени
    assert len(my_os.search('fi')) == 2
    assert len(my_os.search('nd')) == 1
    print('Поиск файлов с "fi":')
    print(*my_os.search('fi'), sep='\n')
    print(separator)
    print('Поиск файлов с "nd":')
    print(*my_os.search('nd'), sep='\n')
    print(separator)

    # проверка перехода в каталог выше и в корень
    my_os.cd('..')
    assert my_os.pwd() == '/root/root_lvl_dir_1/'
    my_os.cd('/')
    assert my_os.pwd() == '/root/'

    # проверка размера папок и файлов
    assert len(my_os.du()) == 4
    assert my_os.du()[0][1] == 268
    print('Занимаемое дисковое пространство:')
    print(*my_os.du(), sep='\n')
