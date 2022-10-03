import time
from typing import Union

import requests

from leeteasy.constant import Constant


class RequestHandler:
    """Provides services for requesting leetcode API."""

    @classmethod
    def get_challenge_info(cls) -> Union[dict, None]:
        """Gets daily challenge info from leetcode API."""
        url = Constant.LEETCODE_API_ENDPOINT
        query = Constant.DAILY_CODING_CHALLENGE_QUERY
        max_retries = Constant.HTTP_CALL_RETRIES

        for i in range(max_retries):
            try:
                response = requests.post(url, json={'query': query})
                return response.json().get('data').get('activeDailyCodingChallengeQuestion')
            except Exception:
                """
                    On first hit sleep 10 minutes.
                    On second hit sleep 20 minutes.
                    On third hit sleep 30 minutes.
                """
                time.sleep(((i+1)*10)*60) # sleep takes seconds
        return None
