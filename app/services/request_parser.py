from app.models.challenge import Challenge
from app.services.request_handler import RequestHandler


class RequestParser:
    """Parse responses of leetcode API."""

    @classmethod
    def parse(cls) -> Challenge:
        """Parse API data ans update challenge model."""
        RequestHandler.get_challenge_info()
        return RequestParser._parse_challenge_info(RequestHandler.challenge_info)

    @classmethod
    def _parse_challenge_info(cls, challenge_info) -> Challenge:
        """Parse and update challenge model."""
        challenge = Challenge()
        challenge.title = challenge_info.get('question').get('title')
        challenge.ac_rate = challenge_info.get('question').get('acRate')
        challenge.difficulty = challenge_info.get('question').get('difficulty')
        challenge.question_id = challenge_info.get('question').get('frontendQuestionId')
        challenge.date = challenge_info.get('date')
        challenge.title_slug = challenge_info.get('question').get('titleSlug')
        challenge.raw_tags = challenge_info.get('question').get('topicTags')
        return challenge


if __name__ == '__main__':
    test_challenge = RequestParser.parse()
    print(test_challenge)
