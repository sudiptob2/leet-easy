from pathlib import Path

from notifypy import Notify

from leeteasy.models.challenge import Challenge
from leeteasy.services.request_handler import RequestHandler
from leeteasy.services.request_parser import RequestParser


class Notifier:
    """Handles notification related functionalities."""

    target_difficulty = ['Easy']
    app_name = 'LeetEasy'
    challenge: Challenge

    @classmethod
    def prepare_notification(cls):
        """Prepare notification msg and triggers notification."""
        challenge_info = RequestHandler.get_challenge_info()
        cls.challenge = RequestParser.parse(challenge_info)
        if cls.challenge.difficulty in cls.target_difficulty:
            return '{0}\nLink: {1}'.format(
                cls.challenge.title,
                cls.challenge.problem_link,
            )

    @classmethod
    def notify(cls):
        """Send desktop notification."""
        app_name_with_subtitle = '{0} - Easy Problem Notification'.format(cls.app_name)
        icon_path = Path(__file__).parent.parent / 'assets/leetcoin.png'
        notification = Notify(
            default_notification_application_name=app_name_with_subtitle,
            default_notification_icon=icon_path,
        )
        notification.message = cls.prepare_notification()
        notification.title = '{0} - {1} Problem Alert \U0001F514'.format(
            cls.app_name,
            cls.challenge.difficulty,
        )
        if notification.message:
            notification.send()
