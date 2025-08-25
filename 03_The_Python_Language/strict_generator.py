# create a generator and list out its items and their sum
squares = (x*x for x in range(10))
print(list(squares))  # prints [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(sum(squares))   # Bug! prints 0


class AccessingConsumedGeneratorError(Exception):
    """Raised if a generator is accessed after already consumed."""


class StrictGenerator:
    """Wrapper for generator which will only permit it to be consumed once.
    Additional accesses will raise AccessingConsumedGeneratorError."""
    def __init__(self, gen):
        self._gen = gen
        self._gen_consumed = False

    def __iter__(self):
        return self

    def __next__(self):
        try:
            return next(self._gen)
        except StopIteration:
            if self._gen_consumed:
                raise AccessingConsumedGeneratorError() from None
            self._gen_consumed = True
            raise


squares = StrictGenerator(x*x for x in range(10))
print(list(squares))  # prints [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(sum(squares))   # raises AccessingConsumedGeneratorError
