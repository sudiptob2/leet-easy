from notifypy import Notify

from leeteasy.services.request_handler import RequestHandler
from leeteasy.services.request_parser import RequestParser


class Notifier:
    """Handles notification related functionalities."""

    target_difficulty = ['Easy']
    app_name = 'LeetEasy'
    challenge = None

    @classmethod
    def prepare_notification(cls):
        """Prepares notification msg and triggers notification."""
        challenge_info = RequestHandler.get_challenge_info()
        cls.challenge = RequestParser.parse(challenge_info)
        if cls.challenge.difficulty in cls.target_difficulty:
            return '{0}\nLink: {1}'.format(
                cls.challenge.title,
                cls.challenge.problem_link,
            )

    @classmethod
    def notify(cls):
        notification = Notify()
        notification.message = cls.prepare_notification()
        notification.title = f'{cls.app_name} - {cls.challenge.difficulty} ' \
                             f'Problem Alert \U0001F514'
        notification.icon = 'leeteasy/assets/leetcoin.png'
        notification.send()
