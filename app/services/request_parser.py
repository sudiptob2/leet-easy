from app.models.challenge import Challenge
from app.services.request_handler import RequestHandler


class RequestParser:
    """Parse responses of leetcode API."""

    @classmethod
    def parse(cls):
        """Parse API data ans update challenge model."""
        RequestHandler.get_challenge_info()
        RequestParser._parse_challenge_info(RequestHandler.challenge_info)

    @classmethod
    def _parse_challenge_info(cls, challenge_info):
        """Parse and update challenge model."""
        challenge = Challenge()
        challenge.title = challenge_info.get('question').get('title')
        challenge.ac_rate = challenge_info.get('question').get('acRate')
        challenge.difficulty = challenge_info.get('question').get('difficulty')
        challenge.question_id = challenge_info.get('question').get('frontendQuestionId')
        challenge.date = challenge_info.get('date')
        challenge.title_slug = challenge_info.get('question').get('titleSlug')
        challenge.raw_tags = challenge_info.get('question').get('topicTags')


if __name__ == '__main__':
    RequestParser.parse()
    test_challenge = Challenge()
    print(test_challenge)
