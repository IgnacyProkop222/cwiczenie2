import os
import sys

# Ensure the project's `src` directory is on sys.path so imports like
# `from app import logic` work when running tests from the repository root.
sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src"))
)

from app import logic


def test_count_words_empty():
    assert logic.count_words("") == {}


def test_count_words_basic():
    text = "Hello hello world"
    counts = logic.count_words(text)
    assert counts.get("hello") == 2
    assert counts.get("world") == 1


def test_most_common():
    counts = {"a": 5, "b": 2, "c": 3}
    top1 = logic.most_common(counts, 1)
    assert top1 == [("a", 5)]
