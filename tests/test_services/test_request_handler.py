from app.services.request_handler import RequestHandler


class TestRequestHandler:
    """Class for testing request handlers."""

    def test_get_challenge_info(self, mocker, fake_challenge_data):
        """Tests get_challenge_info method."""

        def fake_get_challenge_info():
            RequestHandler.challenge_info = fake_challenge_data

        mocker.patch.object(RequestHandler, 'get_challenge_info', fake_get_challenge_info)
        RequestHandler.get_challenge_info()
        assert type(RequestHandler.challenge_info) == dict
