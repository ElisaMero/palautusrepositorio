from matchers import All, And, PlaysIn, HasFewerThan, HasAtLeast, Or


class QueryBuilder:
    def __init__(self, query=All()):
        self.query = query

    def build(self):
        return self.query

    def playsIn(self, field):
        values = And(self.query, PlaysIn(field))
        return QueryBuilder(values)

    def hasAtLeast(self, value, attr):
        values = And(self.query, HasAtLeast(value, attr))
        return QueryBuilder(values)

    def hasFewerThan(self, value, attr):
        values = And(self.query, HasFewerThan(value, attr))
        return QueryBuilder(values)

    def oneOf(self, *matchers):
        values = Or(*matchers)
        return QueryBuilder(values)
