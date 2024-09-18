# EZPKL: lovely pickling🥒 for context manager hater👊

 [![PyPI version](https://badge.fury.io/py/ezpkl.svg)](https://badge.fury.io/py/ezpkl) [![Python Downloads](https://static.pepy.tech/badge/ezpkl)](https://pepy.tech/project/ezpkl)

<h4 align="center">
    <p>
        <a href="https://github.com/yesinkim/ezpkl/">English</a> |
        한국어
    </p>
</h4>

![EZPKL character](https://raw.githubusercontent.com/yesinkim/ezpkl/main/assets/banner.png)
컨텍스트 매니저 문법과 생김새를 좋아하지 않아서 만들었습니다.

## 설치

패키지 관리자 [pip](https://pip.pypa.io/en/stable/)를 사용하여 ezpkl를 설치합니다.

```bash
pip install ezpkl
```

## 사용법

### 객체 저장하기

```python
from ezpkl import save_pkl

a = [1, 2, 3, 4, 5]

# 현재 폴더에 'a.pkl'이 저장됩니다.
save_pkl(var=a)

# 현재 폴더에 'a_list_temp.pkl'이 저장됩니다.
save_pkl(var=a, file_name='a_list_temp')
```

### 객체 불러오기

```python
from ezpkl import load_pkl

a = load_pkl('a.pkl')
```

### 객체를 txt로 저장하기

```python
from ezpkl import save_txt

a = [1, 2, 3, 4, 5]

# 현재 폴더에 'a.txt'가 저장됩니다.
save_txt(data=a)

# 현재 폴더에 'a_list_temp.txt'가 저장됩니다.
save_txt(data=a, file_name='a_list_temp')
```

### 객체 불러오기

```python
from ezpkl import load_txt

a = load_txt('a.txt')
```

### 구분자를 사용하여 리스트 객체를 txt로 저장하기

```python
from ezpkl import save_txt

a = ["apple", "banana", "cherry"]

# 기본 구분자(줄바꿈)로 현재 폴더에 'a.txt'가 저장됩니다.
save_txt(data=a)
# a.txt 파일 내용:
# apple
# banana
# cherry

# 공백 구분자로 현재 폴더에 'a_list_temp.txt'가 저장됩니다.
save_txt(data=a, file_name='a_list_temp', separator=' ')
# a_list_temp.txt 파일 내용:
# apple banana cherry

# 구분자 없이 현재 폴더에 'a_list_temp.txt'가 저장됩니다.
save_txt(data=a, file_name='a_list_temp', separator=None)
# a_list_temp.txt 파일 내용:
# applebananacherry
```

## 라이선스

[MIT](https://choosealicense.com/licenses/mit/)
