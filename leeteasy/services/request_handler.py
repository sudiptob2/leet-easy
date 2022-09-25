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
        try:
            response = requests.post(url, json={'query': query})
        except Exception:
            # TODO: some retry logic will be better
            return
        return response.json().get('data').get('activeDailyCodingChallengeQuestion')
