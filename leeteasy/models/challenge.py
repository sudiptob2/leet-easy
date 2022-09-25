from typing import List


class Challenge:
    """Singleton Model class for daily challenge."""

    title: str = ''
    raw_tags: List[dict] = None
    ac_rate: float = 0
    difficulty: str = None
    question_id: int = None
    title_slug: str = ''
    date: str = None

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Challenge, cls).__new__(cls)
        return cls.instance

    @property
    def problem_link(self) -> str:
        """Returns the link of the problem."""
        return 'https://leetcode.com/problems/{0}/'.format(
            self.title_slug,
        )

    @property
    def tags(self) -> List[str]:
        """Returns the link of the problem."""
        tags = []
        for tag in self.raw_tags:
            tags.append(tag.get('name'))
        return tags

    def __str__(self):
        """Returns the string rep of the class."""
        return f"Title: {self.title}\nAcceptance Rate: {self.ac_rate}" \
               f"\nDifficulty: {self.difficulty}\n" + \
               f"id: {self.question_id}\nTags: {self.tags}"
