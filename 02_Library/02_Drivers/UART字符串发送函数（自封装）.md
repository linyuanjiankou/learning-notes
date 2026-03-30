使用阻塞式单字节发送字符串：
```c
void USART_SendString(UART_HandleTypeDef huart ,char *str){
	
	while(*str)//当当前字符非字符串结束符‘\0’时
	{
		HAL_UART_Transmit(huart, (uint8_t *)str, 1, HAL_MAX_DELAY); //发送字符
		str++; //移到下一位
	}
}
```

也可以计算字符串长度一次性发送整条字符串：
~~~c
void USART_SendString(UART_HandleTypeDef *huart, char *str) {
    
    uint16_t len = 0;
    char *temp = str;
    
    while(*temp++) len++; // 计算字符串长度
    
    HAL_UART_Transmit(huart, (uint8_t *)str, len, HAL_MAX_DELAY);// 一次发送整个字符串
}
~~~
或者使用非阻塞式发送：
~~~c
void USART_SendString_IT(UART_HandleTypeDef *huart, char *str) {
    
    // 使用中断方式发送，不阻塞主程序
    while(*str) {
        HAL_UART_Transmit_IT(huart, (uint8_t *)str, 1);
        str++;
        // 注意：这里可能需要添加延时或等待发送完成的机制
        // 避免发送过快导致数据覆盖
    }
}
~~~