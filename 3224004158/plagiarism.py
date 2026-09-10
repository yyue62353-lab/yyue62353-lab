import math
import re
from collections import Counter

import jieba


def clean_text(text):
    """保留中文、英文和数字，去除其他无意义字符。"""
    return re.findall(r"[\u4e00-\u9fffA-Za-z0-9]+", text)


def get_word_frequency(text):
    """对文本进行分词并统计词频。"""
    words = []
    for item in clean_text(text):
        if re.search(r"[\u4e00-\u9fff]", item):
            words.extend(jieba.cut(item))
        else:
            words.append(item.lower())

    words = [word.strip() for word in words if word.strip()]
    return Counter(words)


def cosine_similarity(text1, text2):
    """计算两段文本的余弦相似度。"""
    freq1 = get_word_frequency(text1)
    freq2 = get_word_frequency(text2)

    if not freq1 or not freq2:
        return 0.0

    all_words = set(freq1) | set(freq2)

    dot_product = sum(freq1[word] * freq2[word] for word in all_words)

    magnitude1 = math.sqrt(
        sum(count * count for count in freq1.values())
    )
    magnitude2 = math.sqrt(
        sum(count * count for count in freq2.values())
    )

    if magnitude1 == 0 or magnitude2 == 0:
        return 0.0

    return dot_product / (magnitude1 * magnitude2)
