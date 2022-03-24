import statistics
from dataclasses import dataclass

from app.models import CorruptLine, IncompleteLine


@dataclass
class NavCalculator:
    navigations: list[str]

    @property
    def corrupt_line_score(self) -> int:
        corrupt_lines = self._get_corrupt_lines()
        return sum(line.score for line in corrupt_lines)

    @property
    def incomplete_line_score(self) -> int:
        incomplete_lines = self._get_incomplete_lines()
        return statistics.median(line.score for line in incomplete_lines)

    def _get_corrupt_lines(self) -> list[CorruptLine]:
        """Return a list of corrupted lines, that is one where a chunk hits an invalid closing character"""
        return [
            line
            for navigation in self.navigations
            if (line := CorruptLine(line=navigation))
        ]

    def _get_incomplete_lines(self) -> list[IncompleteLine]:
        """Return a list of incomplete lines, that is one where a chunk is valid but missing closing characters"""
        uncorrupted_navigations = [
            navigation
            for navigation in self.navigations
            if not CorruptLine(line=navigation)
        ]
        return [
            line
            for navigation in uncorrupted_navigations
            if (line := IncompleteLine(line=navigation))
        ]
