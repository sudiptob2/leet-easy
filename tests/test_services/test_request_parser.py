from leeteasy.services.request_handler import RequestHandler
from leeteasy.services.request_parser import RequestParser


class TestRequestParser:
    """Class for testing request parser."""

    def test_parse(self, mocker, fake_challenge_data):
        """Tests parse method."""

        def fake_get_challenge_info():
            RequestHandler.challenge_info = fake_challenge_data

        mocker.patch.object(
            RequestHandler,
            'get_challenge_info',
            fake_get_challenge_info,
        )
        challenge = RequestParser.parse()

        assert challenge.title == fake_challenge_data.get('question').get('title')
        assert challenge.difficulty == fake_challenge_data.get('question').get('difficulty')
        assert challenge.title_slug == fake_challenge_data.get('question').get('titleSlug')
        assert challenge.title == fake_challenge_data.get('question').get('title')
        assert len(challenge.tags) == len(fake_challenge_data.get('question').get('topicTags'))
        assert challenge.date == fake_challenge_data.get('date')
