from datetime import datetime


class TimeValidator:
    """Provides method for validating time."""

    time_format = '%H:%M'

    @classmethod
    def validate(cls, time: str):
        """Validates the given string is in valid time format."""
        try:
            return datetime.strptime(time, cls.time_format).time()
        except ValueError:
            raise SystemExit('Invalid date format given.')
