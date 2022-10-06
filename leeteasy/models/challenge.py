from typing import Dict, List, Optional


class Challenge:
    """Singleton Model class for daily challenge."""

    title: str = ''
    raw_tags: List[Dict[str, str]] = []
    ac_rate: float = 0
    difficulty: str = ''
    question_id: int = 0
    title_slug: str = ''
    date: str = ''

    def __new__(cls):
        """Override default class creation logic."""
        if not hasattr(cls, 'instance'):  # NOQA : WPS421
            cls.instance = super(Challenge, cls).__new__(cls)  # NOQA: WPS608
        return cls.instance

    @property
    def problem_link(self) -> str:
        """Return the link of the problem."""
        return 'https://leetcode.com/problems/{0}/'.format(
            self.title_slug,
        )

    @property
    def tags(self) -> List[Optional[str]]:
        """Return the link of the problem."""
        tags = []
        for tag in self.raw_tags:
            tags.append(tag.get('name'))
        return tags

    def __str__(self):
        """Return the string rep of the class."""
        return 'Title: {0}\nAcceptance: {1}\nDifficulty: {2}\nID: {3}\nTags: {4}\n'.format(
            self.title,
            self.ac_rate,
            self.difficulty,
            self.question_id,
            self.tags,
        )
