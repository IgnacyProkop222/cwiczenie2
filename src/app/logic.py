"""Core logic for a tiny word-counter app."""

from typing import Dict


def count_words(text: str) -> Dict[str, int]:
    """Return a dict with word counts for the given text.

    Words are split on whitespace and normalized to lower-case. Empty input
    returns an empty dict.
    """
    if not text:
        return {}

    counts: Dict[str, int] = {}
    for token in text.split():
        word = token.strip().lower()
        if not word:
            continue
        counts[word] = counts.get(word, 0) + 1
    return counts


def most_common(counts: Dict[str, int], n: int = 1):
    """Return the n most common words as a list of (word, count).

    If n <= 0, returns an empty list.
    """
    if n <= 0:
        return []
    return sorted(counts.items(), key=lambda kv: kv[1], reverse=True)[:n]
