# 整合后的代码：
# 学习经过：
# 一、SCL&SDA
* SCL：主机控制，节拍器（usually 100kHz or 400kHz）；SDA：主从机轮流使用
* 谁想说话谁拉低
* 主机每个时钟周期传输一位数据，8个时钟周期完成1字节传输，等待从机应答（ACK 0 / NACK 1），反之，主机可以不应答或直接STOP，其他相同
* SCL低电平时，发送方写SDA；SCL高电平时，SDA被锁，接收方读数据，发送方不能写
* Start：拉高SCL和SDA，在SCL高电平的情况下拉低SDA
* Stop：拉高SCL，在SCL高电平的情况下拉高SDA
# 二、发送1bit
* 发送数据位时，在SCL拉高之前，先确定SDA的状态不变（拉低0，放手1）
	发送1：SDA=1；SCL=  0  ->  1  ->  0 
	发送0：SDA=0；SCL=  0  ->  1  ->  0 
* 基本实现写法（只发一次，未优化）：
```c
void IIC_SendBit(uint8_t bit)
{
    if (bit)
        SDA = 1;    // 放手，表示 1
    else
        SDA = 0;    // 拉低，表示 0

    delay_us(5);

    SCL = 1;       // 时钟上升沿
    delay_us(5);
    SCL = 0;       // 时钟下降沿
}

```
# 三、Start -> 1Byte -> Stop
```c
  void IIC_Start(void)
{
    SDA = 1;     // 确保释放
    SCL = 1;
    delay_us(5);

    SDA = 0;     // 在 SCL 高时拉低 → Start
    delay_us(5);

    SCL = 0;     // 准备发送数据
}

void IIC_SendByte(uint8_t data)
{
    for (int i = 0; i < 8; i++)
    {
        IIC_SendBit(data & 0x80); // 发送最高位
        data <<= 1;
    }
}

void IIC_Stop(void)
{
    SDA = 0;
    SCL = 1;
    delay_us(5);

    SDA = 1;     // 在 SCL 高时释放 → Stop
    delay_us(5);
}
```
# 四、ACK
* what is ACK：在第9个时钟周期，从机拉低SDA
* 等待ACK时，SDA不是输出，而是输入
```c
uint8_t IIC_WaitAck(void)
{
	SDA = 1;            //主机放手SDA
	delay_us(5);
	
	SCL = 1;            //第九个时钟
	delay_us(5);
	
	if(SDA == 0)
	{
		SCL = 0;
		return 1;
	}
	else
	{
		SCL = 0;
		return 0;
	}
}
```
# 五、主机读&回应

完整流程：
1. 主机放手SDA
2. 从机在SDA上放数据1bit
3. 主机打8个SCL
4. 主机读完8bit
5. 主机决定：
   * 继续读（ACK，拉低SDA）
   * 不继续读（NACK，SDA = 1）

```c
uint8_t IIC_ReadBit(void)
{
    SDA = 1;        // 主机放手 SDA
    delay_us(5);

    SCL = 1;
    delay_us(5);

    uint8_t bit = SDA;  // 读数据

    SCL = 0;
    return bit;
}

uint8_t IIC_ReadByte(uint8_t ack)
{
    uint8_t data = 0;

    for (int i = 0; i < 8; i++)
    {
        data <<= 1;
        data |= IIC_ReadBit();
    }

    // 主机回应 ACK 或 NACK
    if (ack)
        SDA = 0;    // ACK：我还要
    else
        SDA = 1;    // NACK：不要了

    delay_us(5);
    SCL = 1;
    delay_us(5);
    SCL = 0;

    SDA = 1;        // 释放 SDA
    return data;
}
```
# 六、读MPU6050的只读寄存器



