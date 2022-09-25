import subprocess

from leeteasy.services.request_handler import RequestHandler
from leeteasy.services.request_parser import RequestParser


class Notifier:
    """Handles notification related functionalities."""

    @classmethod
    def prepare_notification(cls):
        """Prepares notification msg and triggers notification."""
        challenge_info = RequestHandler.get_challenge_info()
        test_challenge = RequestParser.parse(challenge_info)
        return test_challenge.problem_link

    @classmethod
    def notify(cls):
        msg = cls.prepare_notification()
        subprocess.run(['notify-send', 'leeteasy', msg])
