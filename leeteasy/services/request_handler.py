import time
from typing import Union

import requests

from leeteasy.constant import Constant


class RequestHandler:
    """Provides services for requesting leetcode API."""

    @classmethod
    def get_challenge_info(cls) -> Union[dict, None]:
        """Get daily challenge info from leetcode API."""
        url = Constant.LEETCODE_API_ENDPOINT
        query = Constant.DAILY_CODING_CHALLENGE_QUERY
        max_retries = Constant.HTTP_CALL_RETRIES  # Change HTTP_CALL_RETRIES for more retries

        for iteration in range(max_retries):
            try:
                response = requests.post(url, json={'query': query})
                return response.json().get('data').get('activeDailyCodingChallengeQuestion')
            except Exception:
                time.sleep(((iteration + 1) * 10) * 60)
        raise SystemExit('Could not connect to the leetcode server.')
