"""Count English words in a text file and print them by frequency."""

import argparse
import re
from collections import Counter
from pathlib import Path


WORD_PATTERN = re.compile(r"[A-Za-z]+(?:'[A-Za-z]+)?")


def count_words(file_path: Path) -> Counter[str]:
    """Return case-insensitive English word counts from *file_path*."""
    text = file_path.read_text(encoding="utf-8-sig")
    return Counter(word.lower() for word in WORD_PATTERN.findall(text))


def main() -> None:
    parser = argparse.ArgumentParser(
        description="统计 txt 文件中每个英文单词出现的次数。"
    )
    parser.add_argument("file", type=Path, help="要统计的 txt 文件路径")
    args = parser.parse_args()

    try:
        counts = count_words(args.file)
    except (OSError, UnicodeError) as error:
        parser.error(f"无法读取文件：{error}")

    for word, count in sorted(counts.items(), key=lambda item: (-item[1], item[0])):
        print(f"{word}\t{count}")


if __name__ == "__main__":
    main()
