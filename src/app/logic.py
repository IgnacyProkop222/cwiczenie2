"""Core logic for a tiny word-counter app.

Notes:
 - Keep annotations simple to avoid AST parsing issues in older astroid
   versions used by some CI images.
"""


def count_words(text: str):
    """Return a plain dict with word counts for the given text.

    Words are split on whitespace and normalized to lower-case. Empty input
    returns an empty dict.
    """
    if not text:
        return {}

    counts = {}
    for token in text.split():
        word = token.strip().lower()
        if not word:
            continue
        counts[word] = counts.get(word, 0) + 1
    return counts


def most_common(counts, top_n: int = 1):  # pylint: disable=invalid-name
    """Return the top_n most common words as a list of (word, count).

    If top_n <= 0, returns an empty list.
    """
    if top_n <= 0:
        return []
    return sorted(counts.items(), key=lambda kv: kv[1], reverse=True)[:top_n]
