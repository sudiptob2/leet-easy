from leeteasy.models.challenge import Challenge


class RequestParser:
    """Parse responses of leetcode API."""

    @classmethod
    def parse(cls, challenge_info: dict) -> Challenge:
        """Parse API data ans update challenge model."""
        return RequestParser._parse_challenge_info(challenge_info)

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
