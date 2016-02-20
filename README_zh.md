# delay_decorator

一个基于Python装饰器Decorators的延时执行系统，用于延缓Python方法的执行，保证只有函数在计时完成时只执行一次。[English README.md](README.md)



## 什么是 delay_decorator?

`delay_decorator` 一个代替Schedule模块的使用线程的decorator，函数调用后会顶替掉前面没有执行的函数，将计时器清零，保证函数最终只运行一次。


看了下面的一个示例，你就明白如何使用了：

### DEMO

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

### 配置项

```python
@Delayer.delay(delay_time = delay_time)
```

 - **`delay_time`**: 会延迟的秒数， 默认为`5`秒.


## 如何安装使用?

### 安装

三种方法安装 delay_decorator: 

#### 1. 使用PIP工具

 - `pip3/pip install delay_decorator`

#### 2. 下载安装

 - 从 [https://pypi.python.org/pypi/delay_decorator/](https://pypi.python.org/pypi/delay_decorator/)下载安装包解压, 并在目录中执行 `python setup.py install`即可。

#### 3. 手动安装使用

 - 将项目中的`delay` 复制到当前目录，或者 Python的`site-packages`目录, 然后 `import Delayer` 即可使用。


### 使用方法

#### 装饰器

```python

import Delayer
@Delayer.delay(delay_time = delay_time)
def need_to_be_delay_function():
	pass    # no returns

```

