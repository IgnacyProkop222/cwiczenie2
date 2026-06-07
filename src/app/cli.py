"""Simple CLI for the word-counter app."""

import argparse
from .logic import count_words, most_common


def build_parser():
    """Build and return the CLI argument parser.

    This parser accepts a positional text argument (one or more tokens) and
    an optional --top integer.
    """
    parser = argparse.ArgumentParser(description="Count words in a string")
    parser.add_argument("text", help="Text to analyze", nargs="+")
    parser.add_argument("--top", type=int, default=3, help="Show top N words")
    return parser


def main(argv=None):
    """Parse argv and run the word counting logic, printing top results."""
    parser = build_parser()
    args = parser.parse_args(argv)
    text = " ".join(args.text)
    counts = count_words(text)
    # pass the value positionally to avoid relying on the old keyword name
    top = most_common(counts, args.top)
    for word, cnt in top:
        print(f"{word}: {cnt}")


if __name__ == "__main__":
    main()
