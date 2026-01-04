import unittest
from pattern import Singleton, RoadLogistics, WindowsFactory, CarBuilder


class TestPatterns(unittest.TestCase):

    def test_singleton(self):
        s1 = Singleton()
        s2 = Singleton()
        self.assertIs(s1, s2)
        self.assertEqual(s1.get_data(), "Singleton Data")

    def test_factory_method(self):
        logistics = RoadLogistics()
        result = logistics.plan_delivery()
        self.assertIn("грузовиком", result)

    def test_abstract_factory(self):
        factory = WindowsFactory()
        button = factory.create_button()
        self.assertIn("Windows", button.render())

    def test_builder(self):
        car = CarBuilder().build_engine().build_wheels().get_result()
        self.assertIn("Engine", car.list_parts())
        self.assertIn("Wheels", car.list_parts())


if __name__ == "__main__":
    unittest.main()
