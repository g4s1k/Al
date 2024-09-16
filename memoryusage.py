# 1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
# Для анализа возьмите любые 1-3 ваших программы. Результаты анализа вставьте в виде комментариев к коду.
# P.S. Напишите в комментариях версию Python и разрядность ОС.


import sys


class Obj_Info_Getter():

    __slots__ = ['module_name']

    def __init__(self, module_name = ''):
        self.module_name = module_name

    def get_obj_info(self, obj_name, wronglist = tuple()):
        try:
            if (obj_name not in sys.modules) and (obj_name not in wronglist):
                obj_type = type(getattr(sys.modules[self.module_name], obj_name))
                obj_counter = sys.getrefcount(getattr(sys.modules[self.module_name], obj_name)) - 1
                obj_size = sys.getsizeof(getattr(sys.modules[self.module_name], obj_name))
                obj_total_size = self.get_obj_total_size(obj_name, wronglist)
                return (obj_name, obj_type, obj_counter, obj_size, obj_total_size)
        except KeyError:
            print(f'No module with name {self.module_name}. Please, set correct Obj_Info_Getter.module name')

    def get_script_objects_info(self, wronglist = tuple()):
        try:
            info_list = []
            for item in dir(sys.modules[self.module_name]):
                if not item.startswith('__'):
                    info = self.get_obj_info(item, wronglist)
                    info_list.append(info)
            return info_list
        except KeyError:
            print(f'No module with name {self.module_name}. Please, set correct Obj_Info_Getter.module name')

    def get_obj_total_size(self, obj_name, wronglist = tuple()):
        try:
            if (obj_name not in sys.modules) and (obj_name not in wronglist):
                obj = getattr(sys.modules[self.module_name], obj_name)
                obj_size = sys.getsizeof(obj)
                if hasattr(obj, '__iter__'):
                    if hasattr(obj, 'items'):
                        for item in obj.items():
                            obj_size += sys.getsizeof(item[0])
                            obj_size += sys.getsizeof(item[1])
                    else:
                        for item in obj:
                            obj_size += sys.getsizeof(item)
                return obj_size
        except KeyError:
            print(f'No module with name {self.module_name}. Please, set correct Obj_Info_Getter.module name')

    def get_script_objects_size(self, wronglist = tuple()):
        try:
            total_size = 0
            for item in dir(sys.modules[self.module_name]):
                if not item.startswith('__'):
                    total_size += self.get_obj_total_size(item, wronglist)
            return total_size
        except KeyError:
            print(f'No module with name {self.module_name}. Please, set correct Obj_Info_Getter.module name')

    def print_objects_info(self, wronglist = tuple(), sep = '-'*100):
        info_list = self.get_script_objects_info(wronglist)
        print(f'{sep}\n\n', f'Objects info for script "{self.module_name}":\n\n')
        for obj_info in info_list:
            if obj_info: #почему-то в тесте вылез объект None, видимо в какой-то переменной содержится
                print(f'{sep}\n')
                for index in range(0, len(obj_info)):
                    tab = '    '
                    if index == 0:
                        description = 'Obj_name: '
                        tab = ''
                    elif index == 1:
                        description = 'Obj_type: '
                    elif index == 2:
                        description = 'Obj_counter: '
                    elif index == 3:
                        description = 'Obj_size: '
                    elif index == 4:
                        description = 'Obj_total_size: '
                    else:
                        description = 'Uncnown_property: '
                    print(tab, description, obj_info[index])

        print(f'{sep}\n')


if __name__ == '__main__':
    import sample_script # не по ГОСТУ для теста
    wronglist = tuple('randint')
    info_getter = Obj_Info_Getter('sample_script')
    info_getter.print_objects_info(wronglist)
    print('TOTAL SCRIPT MEMORY USAGE: ', info_getter.get_script_objects_size(wronglist))

# python3.6.2
# MS Windows10 64bit
# TOTAL SCRIPT MEMORY USAGE:  502
