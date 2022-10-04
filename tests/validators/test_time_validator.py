from leeteasy.utils.validatiors import TimeValidator
import datetime
import unittest

class TestTimeValidator(unittest.TestCase):
    def test_validator(self):
        self.assertEqual(TimeValidator.validate("23:59"), datetime.time(23, 59))
        self.assertEqual(TimeValidator.validate("11:59"), datetime.time(11, 59))
        self.assertEqual(TimeValidator.validate("0:0"), datetime.time(0, 0))
        with self.assertRaises(SystemExit):
            TimeValidator.validate("2:60")
        with self.assertRaises(SystemExit):
            TimeValidator.validate("24:00")
        with self.assertRaises(SystemExit):
            TimeValidator.validate("5")

if __name__ == "__main__":
    unittest.main()