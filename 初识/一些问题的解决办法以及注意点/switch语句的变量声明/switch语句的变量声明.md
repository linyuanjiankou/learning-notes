**错误：**
![](Pasted%20image%2020260306191435.png)
**正确：**
![](Pasted%20image%2020260306191604.png)

在switch-case语句中，case后面只能跟语句，而诸如`uint16_t current_freq……`之类的变量定义属于声明而非语句，声明不能成为case的“标签”对象，因此需要套上花括号形成代码块。