# 1. Singleton
class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.data = "Singleton Data"
        return cls._instance

    def get_data(self):
        return self.data


# 2. Factory Method
from abc import ABC, abstractmethod


class Transport(ABC):
    @abstractmethod
    def deliver(self):
        pass


class Truck(Transport):
    def deliver(self):
        return "Доставка грузовиком"


class Logistics(ABC):
    @abstractmethod
    def create_transport(self):
        pass

    def plan_delivery(self):
        transport = self.create_transport()
        return transport.deliver()


class RoadLogistics(Logistics):
    def create_transport(self):
        return Truck()


# 3. Abstract Factory
class Button(ABC):
    @abstractmethod
    def render(self):
        pass


class WindowsButton(Button):
    def render(self):
        return "Windows Button"


class MacButton(Button):
    def render(self):
        return "Mac Button"


class GUIFactory(ABC):
    @abstractmethod
    def create_button(self):
        pass


class WindowsFactory(GUIFactory):
    def create_button(self):
        return WindowsButton()


# 4. Builder
class Car:
    def __init__(self):
        self.parts = []

    def add(self, part):
        self.parts.append(part)

    def list_parts(self):
        return f"Car parts: {', '.join(self.parts)}"


class CarBuilder:
    def __init__(self):
        self.car = Car()

    def build_engine(self):
        self.car.add("Engine")
        return self

    def build_wheels(self):
        self.car.add("Wheels")
        return self

    def get_result(self):
        return self.car


# Демонстрация
def main():
    print("=== Лабораторная работа 3 ===")

    # Singleton
    s1 = Singleton()
    s2 = Singleton()
    print(f"1. Singleton: {s1 is s2}, data: {s1.get_data()}")

    # Factory Method
    logistics = RoadLogistics()
    print(f"2. Factory Method: {logistics.plan_delivery()}")

    # Abstract Factory
    factory = WindowsFactory()
    button = factory.create_button()
    print(f"3. Abstract Factory: {button.render()}")

    # Builder
    car = CarBuilder().build_engine().build_wheels().get_result()
    print(f"4. Builder: {car.list_parts()}")


def main():
    print("=" * 50)
    print("Лабораторная работа 3: Порождающие паттерны")
    print("=" * 50)

    # Singleton
    print("\n1. SINGLETON (Одиночка)")
    print("-" * 30)
    s1 = Singleton()
    s2 = Singleton()
    print(f"   Создаем первый объект: id={id(s1)}")
    print(f"   Создаем второй объект: id={id(s2)}")
    print(f"   Это один и тот же объект? {s1 is s2}")
    print(f"   Данные: {s1.get_data()}")

    # Factory Method
    print("\n2. FACTORY METHOD (Фабричный метод)")
    print("-" * 30)
    logistics = RoadLogistics()
    print(f"   Создаем логистику: {logistics.__class__.__name__}")
    print(f"   Результат: {logistics.plan_delivery()}")

    # Abstract Factory
    print("\n3. ABSTRACT FACTORY (Абстрактная фабрика)")
    print("-" * 30)
    factory = WindowsFactory()
    print(f"   Создаем фабрику: {factory.__class__.__name__}")
    button = factory.create_button()
    print(f"   Создаем кнопку: {button.render()}")

    # Builder
    print("\n4. BUILDER (Строитель)")
    print("-" * 30)
    builder = CarBuilder()
    print("   Строим машину по шагам:")
    builder.build_engine()
    print("   - Добавили двигатель")
    builder.build_wheels()
    print("   - Добавили колеса")
    car = builder.get_result()
    print(f"   Результат: {car.list_parts()}")

    print("\n" + "=" * 50)
    print("Все паттерны работают корректно!")
    print("=" * 50)


if __name__ == "__main__":
    main()