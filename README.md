# EZPKL: lovely pickling🥒 for context manager hater👊

 [![PyPI version](https://badge.fury.io/py/ezpkl.svg)](https://badge.fury.io/py/ezpkl) [![Python Downloads](https://static.pepy.tech/badge/ezpkl)](https://pepy.tech/project/ezpkl)

<h4 align="center">
    <p>
        English |
        <a href="https://github.com/yesinkim/ezpkl/blob/main/README_ko.md">한국어</a>
    </p>
</h4>

![EZPKL character](https://raw.githubusercontent.com/yesinkim/ezpkl/main/assets/banner.png)
I hate `with open(file_path) as file...` and I don't want to google `how to save pickle in python` anymore. 
then, i made it.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install ezpkl.

```bash
pip install ezpkl
```

## Usage

### Save Object to pkl

```python
from ezpkl import save_pkl

a = [1, 2, 3, 4, 5]

# 'a.pkl' will be saved in the current directory.
save_pkl(var=a)

# 'a_list_temp.pkl' will be saved in the current directory.
save_pkl(var=a, file_name='a_list_temp')
```

### Load Object

```python
from ezpkl import load_pkl

a = load_pkl('a.pkl')
```

### Save Object to txt

```python
from ezpkl import save_txt

a = [1, 2, 3, 4, 5]

# 'a.txt' will be saved in the current directory.
save_txt(data=a)

# 'a_list_temp.txt' will be saved in the current directory.
save_txt(data=a, file_name='a_list_temp')
```

### Load Object

```python
from ezpkl import load_txt

a = load_txt('a.txt')
```

### Save List Object to txt with separator

```python
from ezpkl import save_txt

a = ["apple", "banana", "cherry"]

# 'a.txt' will be saved in the current directory with newline separator (default).
save_txt(data=a)
# a.txt file content:
# apple
# banana
# cherry

# 'a_list_temp.txt' will be saved in the current directory with space separator.
save_txt(data=a, file_name='a_list_temp', separator=' ')
# a_list_temp.txt file content:
# apple banana cherry

# 'a_list_temp.txt' will be saved in the current directory without separator.
save_txt(data=a, file_name='a_list_temp', separator=None)
# a_list_temp.txt file content:
# applebananacherry
```

## License

[MIT](https://choosealicense.com/licenses/mit/)
