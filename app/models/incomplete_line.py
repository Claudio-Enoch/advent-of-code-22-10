CHUNK_SCORE_MAP = {")": 1, "]": 2, "}": 3, ">": 4}
CHUNK_RELATION_MAP = {"(": ")", "[": "]", "<": ">", "{": "}"}


class IncompleteLine:
    def __init__(self, line: str):
        self.line = line
        self.incomplete_chars: list[str] = self._find_incomplete_closers()
        self.score = self._calculate_autocomplete_points(chars=self.incomplete_chars)

    def _find_incomplete_closers(self) -> list[str]:
        """Get the closing chunk for an incomplete line
        :return: list of closing chars
        """
        expected_closers = []
        for char in self.line:
            if char in CHUNK_RELATION_MAP:
                expected_closers.append(CHUNK_RELATION_MAP[char])
            else:
                expected_closers.pop()
        return expected_closers[::-1]

    @staticmethod
    def _calculate_autocomplete_points(chars: list[str], points=0) -> int:
        if chars:
            points *= 5
            points += CHUNK_SCORE_MAP[chars.pop(0)]
            return IncompleteLine._calculate_autocomplete_points(
                chars=chars, points=points
            )
        return points

    def __repr__(self):
        return f"{self.__class__}(line='{self.line}')"

    def __bool__(self):
        return bool(self.score)
