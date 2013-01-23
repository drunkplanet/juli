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

which is usually considered easier to read by somebody including me.


### Installation and usage

To install, just run `python setup.py install` from terminal.

The usage is very straight forward:

```
import juli

input = '我在github上关注了123个repo。'
output = juli.filter(input)
```

### Rules

There are exceptions.

### Troubleshooting
