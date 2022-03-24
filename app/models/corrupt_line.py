from typing import Optional

CHUNK_SCORE_MAP = {")": 3, "]": 57, "}": 1_197, ">": 25_137}
CHUNK_RELATION_MAP = {"(": ")", "[": "]", "<": ">", "{": "}"}


class CorruptLine:
    def __init__(self, line: str):
        self.line = line
        self.corrupt_char: Optional[str] = self._find_corrupt_closer()
        self.score = CHUNK_SCORE_MAP.get(self.corrupt_char, 0)

    def _find_corrupt_closer(self) -> Optional[str]:
        """Iterate over each character and check for an unexpected closer
        :return: corrupt closer
        """
        expected_closer = []
        for char in self.line:
            if char in CHUNK_RELATION_MAP:
                expected_closer.append(CHUNK_RELATION_MAP[char])
            elif not expected_closer:
                return char
            elif char != expected_closer.pop():
                return char

    def __repr__(self):
        return f"{self.__class__}(line='{self.line}')"

    def __bool__(self):
        return bool(self.score)
