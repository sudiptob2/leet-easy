import pytest


@pytest.fixture
def fake_challenge_data():
    """Returns sample daily challenge data."""
    return {
        "date": "2022-09-22",
        "userStatus": "NotStart", "link": "/problems/reverse-words-in-a-string-iii/",
        "question": {
            "acRate": 80.7035733689484,
            "difficulty": "Easy",
            "freqBar": None,
            "frontendQuestionId": "557",
            "isFavor": False,
            "paidOnly": False,
            "status": None,
            "title": "Reverse Words in a String III",
            "titleSlug": "reverse-words-in-a-string-iii",
            "hasVideoSolution": False,
            "hasSolution": True,
            "topicTags": [
                {"name": "Two Pointers", "id": "VG9waWNUYWdOb2RlOjk=", "slug": "two-pointers"},
                {"name": "String", "id": "VG9waWNUYWdOb2RlOjEw", "slug": "string"},
            ]
        }
    }
