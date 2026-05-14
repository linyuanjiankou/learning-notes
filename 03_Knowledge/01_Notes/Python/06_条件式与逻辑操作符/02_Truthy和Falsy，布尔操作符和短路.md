当遇到需要同时比较多个值的情况，可能会导致嵌套条件式语句，例如：
```python
is_citizen = True
age = 25

if is_citizen:
    if age >= 18:
        print('You are eligible to vote') # You are eligible to vote
else:
    print('You are not eligible to vote')
```

当然，你也可以使用Python的`and`、`or`和`not`操作符来简化条件书写。

# 真值和假值（Truthy & Flasy）

但在深入了解这些操作符之前，先来看看什么是真值和假值。

在Python中，每个值都有固定的布尔值，或者说在逻辑上下文中应该被视为`True`或`False`的内置含义。许多值被认为是真值，即他们在逻辑上下文中计算为`True`，其他则是假值，意味着它们计算为`False`。

下面是一些假值：
- `None`
- `False`
- 整数 `0`
- 浮点数 `0.0`
- 空字串 `""`
其他值如非零数字和非空字符串都是真值。

如果你想查看一个值是真值或者是假值，可以使用内置函数`bool()`函数。它显示地将一个值转换为其布尔等价物，返回`True/False`。

# 布尔操作符
Python中有三个布尔操作符：`and`、`or`和`not`

1. `and`: `and`操作符接受两个操作对象，如果第一个操作对象为假，则返回第一个操作对象，否则返回第二个操作对象。两个操作对象都为真时，返回真。
```python
is_citizen = True
age = 25

print(is_citizen and age) # 25
```
上述示例中，数字 25 被打印到终端，因为 `and` 操作符如果第一个操作对象为 `True`，则会计算第二个操作对象。`and` 操作符被称为短路操作符。短路意味着 Python 从左到右检查值，并在确定最终结果后立即停止。

你经常会在 `if` 语句中使用 `and` 来查看是否满足多个条件。下面是如何重构之前的示例，使用 `and` 操作符代替嵌套的 `if` 语句：
```python
is_citizen = True
age = 25

if is_citizen and age >= 18:
    print('You are eligible to vote') # You are eligible to vote
else:
    print('You are not eligible to vote')
```

在上面的例子中，`is_citizen` 是 `True`，且 `age >= 18` 计算结果为 `True`。由于 `and` 操作符的两个操作对象都为真，该条件 `is_citizen and age >= 18` 计算结果为 `True`，并且执行 `if` 块中的 `print` 调用。

2. `or`：如果第一个操作对象为真，则返回第一个操作对象，否则返回第二个操作对象。如果至少一个操作对象为真，`or`表达式将返回真。`or`操作符也被称为短路操作符。
```python
age = 19
is_employed = False

print(age or is_employed) # 19
```

如果你需要查看一个或多个表达式是否为 `True`，那么你可以在条件式中使用 `or` 操作符：
```python
age = 19
is_student = True

if age < 18 or is_student:
    print('You are eligible for a student discount') # You are eligible for a student discount
else:
    print('You are not eligible for a student discount')
```
在这个分支中，`age < 18` 是 `False`，但 `is_student` 是 `True`。由于至少有一个条件为真，整个 `or` 表达式的值为 `True`，并且 `if` 块中的折扣消息被打印。

3. `not`：接受一个操作对象并反转其布尔值。~~（感觉类似于C中的`!`）~~
在条件式中使用 `not` 操作符来检查某事是否不是 `True` 或 `False` 是很常见的：
```python
is_admin = False

if not is_admin:
    print('Access denied for non-administrators.') # Access denied for non-administrators.
else:
    print('Welcome, Administrator!')
```

由于 `is_admin` 是 `False`，所以 `not is_admin` 表示非 `False`，即 `True`。因此将打印消息 `Access denied for non-administrators.`。

当在 `if` 语句中使用多个逻辑操作符时，使用 `and` 连接的条件会在使用 `or` 连接的条件之前被计算。Python 中使用括号 `()` 来分组条件并控制它们的计算顺序。