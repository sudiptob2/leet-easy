import requests

from app.constant import Constant


class RequestHandler:
    """Provides services for requesting leetcode API."""

    challenge_info = None

    @classmethod
    def get_challenge_info(cls):
        """Gets daily challenge info from leetcode API."""
        url = Constant.LEETCODE_API_ENDPOINT
        query = Constant.DAILY_CODING_CHALLENGE_QUERY
        try:
            response = requests.post(url, json={'query': query})
        except Exception:
            # TODO: log the exception
            return
        cls.challenge_info = response.json().get('data').get('activeDailyCodingChallengeQuestion')
