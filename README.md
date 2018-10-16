# dprofiler


[![PyPI](https://img.shields.io/pypi/v/dprofiler.svg)](https://pypi.org/project/dprofiler/)
[![Build Status](https://travis-ci.org/disktnk/dprofiler.svg?branch=master)](https://travis-ci.org/disktnk/dprofiler)
[![Build status](https://ci.appveyor.com/api/projects/status/d304h5xmycq4t3ls/branch/master?svg=true)](https://ci.appveyor.com/project/disktnk/dprofiler/branch/master)
[![codecov](https://codecov.io/gh/disktnk/dprofiler/branch/master/graph/badge.svg)](https://codecov.io/gh/disktnk/dprofiler)

wrap `cProfile` and `profile` modules, use as decorator.

## Support

- Python 2.7.15+ / 3.5+ / 3.6+

## Install

**Required**

- six 1.11.0+

```
$ pip install dprofiler
```

from source

```bash
$ git clone https://github.com/disktnk/dprofiler
$ cd dprofiler
$ pip install -e .
```

## Usage

Add `@profile` decorator on the target function.

```python
from dprofiler import profile

@profile
def target_function():
    # some process
```

with own logger.

```python
import logging
from dprofiler import profile

own_logger = logging.getLogger(__name__)
# dprofiler output as DEBUG, enable DEBUG level
own_logger.setLevel(logging.DEBUG)

@profile(logger=own_logger)
def target_function():
    # some process
```

output example.

```
path/to/target.py          10 function calls in 0.000 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 pstats.py:65(__init__)
        1    0.000    0.000    0.000    0.000 pstats.py:75(init)
        1    0.000    0.000    0.000    0.000 pstats.py:94(load_stats)
        1    0.000    0.000    0.000    0.000 cProfile.py:50(create_stats)
        ...
```

**Support option**

- `logger`: set own logger, stdout is used on default.
- `sort_key`: `cumtime` on default, other keys are [here](https://docs.python.org/3.6/library/profile.html#pstats.Stats.sort_stats).
- `n`: max count to output, `20` on default.
- `prefix`: output string when start, empty on default.
- `suffix`: output string when end, empty on default.

## License

MIT License (see [LICENSE](/LICENSE) file).
