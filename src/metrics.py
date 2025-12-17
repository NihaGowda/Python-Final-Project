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
        return SortMetrics(
            comparisons=self.comparisons + other.comparisons,
            swaps=self.swaps + other.swaps,
            time_ms=self.time_ms + other.time_ms,
        )

    def __str__(self) -> str:
        return f"SortMetrics(comparisons={self.comparisons}, swaps={self.swaps}, time_ms={self.time_ms:.3f})"


def score_run(metrics: SortMetrics, difficulty: int) -> int:
    """
    Simple scoring function:
    - Higher difficulty increases base score
    - More operations reduce score slightly
    """
    base = 100 * int(difficulty)
    penalty = metrics.comparisons + (2 * metrics.swaps)
    score = max(0, base - penalty)
    return int(score)
