"""
metrics.py

Holds metric tracking for sorting and scoring.
Includes operator overloading (__add__) and __str__.
"""

from __future__ import annotations
from dataclasses import dataclass


@dataclass
class SortMetrics:
    """Tracks performance and operations during sorting."""
    comparisons: int = 0
    swaps: int = 0
    time_ms: float = 0.0

    def __add__(self, other: "SortMetrics") -> "SortMetrics":
        """Operator overloading: combine two metric objects."""
        if not isinstance(other, SortMetrics):
            return NotImplemented
        return SortMetrics(
            comparisons=self.comparisons + other.comparisons,
            swaps=self.swaps + other.swaps,
            time_ms=self.time_ms + other.time_ms,
        )

    def __str__(self) -> str:
        return f"SortMetrics(comparisons={self.comparisons}, swaps={self.swaps}, time_ms={self.time_ms:.3f})"
        return (
            f"SortMetrics(comparisons={self.comparisons}, "
            f"swaps={self.swaps}, time_ms={self.time_ms:.3f})"
        )


def score_run(metrics: SortMetrics, difficulty: int | str) -> int:
    """
    Simple scoring function:
    - Higher difficulty increases base score
    - More operations reduce score slightly

    difficulty can be an int (1/2/3) or a string ("easy"/"medium"/"hard").
    """
    if isinstance(difficulty, str):
        d = difficulty.strip().lower()
        difficulty = {"easy": 1, "medium": 2, "hard": 3}.get(d, 1)

    base = 100 * int(difficulty)
    penalty = metrics.comparisons + (2 * metrics.swaps)
    score = max(0, base - penalty)
    return int(score)
