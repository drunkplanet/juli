# juli

距离产生美。

This little module does only one little thing:

Adding a half-width whitespace between full-width characters and half-width characters.

For example, the following sentence

```
我在github上关注了123个repo。
```

becomes

```
我在 github 上关注了 123 个 repo。
```

which is usually considered to be easier to read.


### Installation and usage

To install, just run `python setup.py install` from terminal.

The usage is pretty straight forward:

```
import juli

input = '我在github上关注了123个repo。'
output = juli.process(input)
```

### Rules

There are exceptions.

中文及日文字符，与半角字符间应留有空格。

全角符号，应视情况而定。原则不加空格。

半角符号与全角字符混用时，位于句首时加空格，位于句尾时不加空格。

对于 markdown 及 reST 格式，其中需要原样输出的部分，不予处理。


### Troubleshooting
