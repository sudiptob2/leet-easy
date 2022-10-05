from leeteasy.utils.validatiors import TimeValidator
import datetime
import pytest

class TestTimeValidator:
    def test_validator(self):
        assert TimeValidator.validate("23:59") == datetime.time(23, 59)
        assert TimeValidator.validate("11:59") == datetime.time(11, 59)
        assert TimeValidator.validate("0:0") == datetime.time(0, 0)

        with pytest.raises(SystemExit):
            TimeValidator.validate("2:60")
        with pytest.raises(SystemExit):
            TimeValidator.validate("24:00")
        with pytest.raises(SystemExit):
            TimeValidator.validate("5")