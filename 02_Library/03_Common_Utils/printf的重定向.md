在C语言中，printf()函数常被应用于在显示器上输出某些指定内容。
而在嵌入式开发的环境下，单片机并不具备显示屏来显示输出内容，那么，我们可以使用串口将单片机需要发送的内容显示在电脑显示屏上进行读取，变相的实现了printf()函数的输出功能。
在这种方法中，我们不仅实现了上述功能，还变相解决了使用HAL库发送函数时无法确定发送数组大小而随机设定造成的内存浪费，某种程度上提高了程序的严谨性。

printf重定向代码（举例）：
~~~c
#include<stdio.h>
int fputc(int ch, FILE *f)
	{
		HAL_UART_Transmit(&huart2, (uint8_t *)&ch, 1, HAL_MAX_DELAY);
		
		return ch;
		
	}
~~~