import subprocess

from leeteasy.services.request_handler import RequestHandler
from leeteasy.services.request_parser import RequestParser


class Notifier:
    """Handles notification related functionalities."""

    target_difficulty = ['Easy']
    app_name = '\U0001F514 LeeEasy - Easy Problem Alert'

    @classmethod
    def prepare_notification(cls):
        """Prepares notification msg and triggers notification."""
        challenge_info = RequestHandler.get_challenge_info()
        challenge = RequestParser.parse(challenge_info)
        if challenge.difficulty in cls.target_difficulty:
            return '{0}\nLink: {1}'.format(
                challenge.title,
                challenge.problem_link,
            )

    @classmethod
    def notify(cls):
        msg = cls.prepare_notification()
        if msg:
            subprocess.run(['notify-send', cls.app_name, msg])
