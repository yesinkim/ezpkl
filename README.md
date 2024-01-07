# EZPKL: lovely pickling🥒 for context manager hater👊

![EZPKL character](https://raw.githubusercontent.com/yesinkim/ezpkl/main/assets/banner.png)
컨텍스트 매니저를 열고 닫는 것이 귀찮아서 만들었습니다.

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

## 라이선스

[MIT](https://choosealicense.com/licenses/mit/)
