import unittest

from student import Student


class TestStudent(unittest.TestCase):
    def test_80_100(self):
        s1 = Student('s1', 80)
        self.assertEqual(s1.get_grade(), 'A')
        s2 = Student('s2', 100)
        self.assertEqual(s2.get_grade(), 'A')

    def test_60_80(self):
        s1 = Student('s1', 60)
        self.assertEqual(s1.get_grade(), 'B')
        s2 = Student('s2', 79)
        self.assertEqual(s2.get_grade(), 'B')

    def test_0_60(self):
        s1 = Student('s1', 0)
        self.assertEqual(s1.get_grade(), 'C')
        s2 = Student('s2', 59)
        self.assertEqual(s2.get_grade(), 'C')

    def test_invalid_value(self):
        s1 = Student('s1', 101)
        with self.assertRaises(ValueError):
            s1.get_grade()
        s2 = Student('s2', -1)
        with self.assertRaises(ValueError):
            s2.get_grade()
