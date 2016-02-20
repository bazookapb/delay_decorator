# delay_decorator
A decorator for delayed function executing.  [中文README.md](README_zh.md)

## What's delay_decorator?

`delay_decorator` is a decorator that is a substitute of Scheduler model of python standard lib.

Auto delay the Function execution for a certain period time.
The new function will replace the older one and reset the countdown of the delay time. `Support python 2.7 ~ python3.5`.

Here's an example of how you might use delay_decorator:

```python

import time
from delay import Delayer

if __name__ == "__main__":

    @Delayer.delay(4)
    def test(key):
        print("The thread: {key} run at {time}".format(key=key, time=str(time.time())))

    print("Now:" + str(time.time()))
    test("First")  # will run after 4 seconds

    time.sleep(5)
    print("Now:" + str(time.time()))
    test("Second")  # Won't run
    time.sleep(2)
    test("Third")   # will run after 6 seconds

```

Some config:

```python
@Delayer.delay(delay_time = delay_time)
```

 - **`delay_time`**: how many seconds to delay. Default is `5`.

 

## How to Install and Use?

### Install

### Install

Three ways to install delay_decorator: 

#### 1. Use tool install

 - `pip install delay_decorator`

#### 2. Download to install

 - Download from [https://pypi.python.org/pypi/delay_decorator/](https://pypi.python.org/pypi/delay_decorator/), and run `python setup.py install`.

#### 3. Manual installation

 - Manual installation: Put `delay` folder into current directory or `site-packages`, then `import delay` to use.


### Usage

#### Decorators

```python

import Delayer
@Delayer.delay(delay_time = delay_time)
def need_to_be_delay_function():
	pass    # no returns

```
