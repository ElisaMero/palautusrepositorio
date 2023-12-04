class QueryBuilder:
    def __init__(self, *matchers):
        self._matchers = matchers

    def test(self, player):
        for matcher in self._matchers:
            if not matcher.test(player):
                return False
        return True

    def build(self):
        return

    def playsIn(self, field):
        pass

    def hasAtLeast(self, value, goal):
        pass

    def hasFewerThan(self):
        pass
