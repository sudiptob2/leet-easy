from typing import Dict

from leeteasy.models.challenge import Challenge


class RequestParser:
    """Parse responses of leetcode API."""

    @classmethod
    def parse(cls, challenge_info: Dict) -> Challenge:
        """Parse API data ans update challenge model."""
        return cls._parse_challenge_info(challenge_info)

    @classmethod
    def _parse_challenge_info(cls, challenge_info) -> Challenge:
        """Parse and update challenge model."""
        question = challenge_info.get('question')
        challenge = Challenge()
        challenge.title = question.get('title')
        challenge.ac_rate = question.get('acRate')
        challenge.difficulty = question.get('difficulty')
        challenge.question_id = question.get('frontendQuestionId')
        challenge.date = challenge_info.get('date')
        challenge.title_slug = question.get('titleSlug')
        challenge.raw_tags = question.get('topicTags')
        return challenge
