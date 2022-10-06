import time
from typing import Dict

import requests

from leeteasy.constant import Constant


class RequestHandler:
    """Provides services for requesting leetcode API."""

    url = Constant.LEETCODE_API_ENDPOINT
    query = Constant.DAILY_CODING_CHALLENGE_QUERY
    max_retries = Constant.HTTP_CALL_RETRIES

    @classmethod
    def get_challenge_info(cls) -> Dict:
        """Get daily challenge info from leetcode API."""
        for iteration in range(cls.max_retries):
            try:
                response = requests.post(cls.url, json={'query': cls.query})
                return response.json().get('data').get('activeDailyCodingChallengeQuestion')
            except Exception:
                time.sleep(((iteration + 1) * 10) * 60)
        raise SystemExit('Could not connect to the leetcode server.')
