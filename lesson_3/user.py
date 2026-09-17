class User:
    def __init__(self, first_name, last_name):     
        self.first_name = first_name
        self.last_name = last_name

    # Метод, который печатает только имя
    def print_first_name(self):
        print(self.first_name)

    # Метод, который печатает только фамилию
    def print_last_name(self):
        print(self.last_name)

    # Метод, который печатает имя и фамилию вместе
    def print_full_name(self):
        print(f"{self.first_name} {self.last_name}")


    