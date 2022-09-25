from notifypy import Notify

from leeteasy.services.request_handler import RequestHandler
from leeteasy.services.request_parser import RequestParser


class Notifier:
    """Handles notification related functionalities."""

    target_difficulty = ['Easy']
    app_name = 'LeetEasy - Easy Problem Alert \U0001F514'

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
        notification = Notify()
        notification.title = cls.app_name
        notification.message = cls.prepare_notification()
        notification.icon = 'assests/leetcoin.png'
        notification.send()
