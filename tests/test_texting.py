import pytest

from ezpkl import load_txt, save_txt


def test_save_txt_string():
    data = "안뇽 세상!"
    save_txt(data, file_name="test_string")
    assert load_txt("test_string.txt") == data


def test_save_txt_list():
    data = ["apple", "banana", "cherry"]
    save_txt(data, file_name="test_list")
    assert load_txt("test_list.txt") == "\n".join(data)


def test_save_txt_invalid_filename():
    data = "춘의 쾌유를 빕니다"
    save_txt(data, file_name="test.txt")
    assert load_txt("test.txt") == data


def test_load_txt_nonexistent_file():
    filename = "nonexistent_file.txt"
    assert load_txt(filename) is None


def test_save_txt_no_filename_with_variable():
    data = "This is a test."
    save_txt(data)
    assert load_txt("data.txt") == data


def test_save_txt_with_separator():
    data = ["치유", "치유", "빔", "!", "✨"]
    save_txt(data, separator=None)
    assert load_txt("data.txt") == "치유치유빔!✨"
