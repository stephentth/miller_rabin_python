# Miller Rabin primality test

An implementation of Miller Rabin primality test written in Python.

## Install

From PyPI (not live yet)

```bash
pip install miller_rabin
```

From Git

```bash
pip install git+https://github.com/stephentt-me/miller_rabin_python.git
```

## Usage

```python
from miller_rabin import miller_rabin

# using defaut k
miller_rabin(15485867)  # 1000001st prime number

# choose your our k=5
miller_rabin(15485867, 5)
```

## Test

```
python -m unittest
```

## Build

```
python setup.py sdist bdist_wheel
```