import pytest

from plagiarism import clean_text, get_word_frequency, cosine_similarity


def test_identical_text():
    assert cosine_similarity("软件工程", "软件工程") == pytest.approx(1.0)


def test_completely_different_text():
    assert cosine_similarity("苹果", "电脑") == pytest.approx(0.0)


def test_partially_similar_text():
    result = cosine_similarity("软件工程 软件开发", "软件工程 数据库")
    assert 0 < result < 1


def test_both_empty():
    assert cosine_similarity("", "") == 0.0


def test_original_empty():
    assert cosine_similarity("", "软件工程") == 0.0


def test_plagiarism_empty():
    assert cosine_similarity("软件工程", "") == 0.0


def test_single_word():
    assert cosine_similarity("计算机", "计算机") == pytest.approx(1.0)


def test_punctuation():
    assert clean_text("你好，世界！") == ["你好", "世界"]


def test_numbers():
    assert clean_text("Python2026") == ["Python2026"]


def test_chinese_english_mix():
    result = cosine_similarity("Python 编程", "Python 编程")
    assert result == pytest.approx(1.0)


def test_repeated_words():
    frequency = get_word_frequency("软件 软件 软件")
    assert frequency["软件"] == 3


def test_long_text():
    text1 = "软件工程 " * 100
    text2 = "软件工程 " * 100
    assert cosine_similarity(text1, text2) == pytest.approx(1.0)
