import pytest

from ezpkl import save_pkl, load_pkl

def test_save_pkl():
    data = [1, 2, 3, (4), 5]
    save_pkl(data)
    assert load_pkl("data.pkl") == data

def test_save_pkl_with_filename():
    data = [1, 2, 3, 4, 5]
    save_pkl(data, file_name="test_data")
    assert load_pkl("test_data.pkl") == data
