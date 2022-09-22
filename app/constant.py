class Constant:
    """Class for organizing constants."""

    # website names
    LEETCODE = 'LEETCODE'
    LEETCODE_API_ENDPOINT = 'https://leetcode.com/graphql'
    DAILY_CODING_CHALLENGE_QUERY = """
    query questionOfToday {
        activeDailyCodingChallengeQuestion {
            date
            userStatus
            link
            question {
                acRate
                difficulty
                freqBar
                frontendQuestionId: questionFrontendId
                isFavor
                paidOnly: isPaidOnly
                status
                title
                titleSlug
                hasVideoSolution
                hasSolution
                topicTags {
                    name
                    id
                    slug
                }
            }
        }
    }
    """
