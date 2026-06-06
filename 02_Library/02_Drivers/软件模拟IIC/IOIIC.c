#include "IOIIC.h"
#include "delay.h"

// IIC起始函数
void IIC_Start(void){
    SDA_OUT();
    IIC_SCL = 1;
    IIC_SDA = 1;
    delay_us(5);
    IIC_SDA = 0;
    delay_us(5);
    IIC_SCL = 0;
}

// IIC结束函数
void IIC_Stop(void){
    SDA_OUT();
    IIC_SDA = 0;
    IIC_SCL = 1;
    delay_us(5);
    IIC_SDA = 1;
    delay_us(5);
}

//发送一个字节并等待从机应答
void IIC_SendBit(uint8_t bit){
    if(bit) IIC_SDA = 1;
    else IIC_SDA = 0;
    delay_us(5);
    IIC_SCL = 1;
    delay_us(5);
    IIC_SCL = 0;
    delay_us(2); //保持数据的稳定
}
uint8_t IIC_SendByte(uint8_t data){
    //发送一个字节
    SDA_OUT();
    for (int i = 0; i < 8; i++){
        IIC_SendBit(data & 0x80); //发送最高位
        data <<= 1;
    }
    SDA_IN();

    //等待从机应答
    IIC_SCL = 1;
    delay_us(5);
    uint8_t ack = !IIC_SDA_READ; //IIC_SDA_READ为0时表示应答
    IIC_SCL = 0;
    delay_us(2);

    return ack;    
}

//读取一个字节
//参数send_ack: 1为发送应答，0为发送非应答
uint8_t IIC_ReadBit(void){
    IIC_SCL = 1;
    delay_us(5);
    uint8_t bit = IIC_SDA_READ;
    IIC_SCL = 0;
    delay_us(2);
    return bit;
}
uint8_t IIC_ReadByte(uint8_t send_ack){
    uint8_t data = 0;
    SDA_IN();

    for (int i = 0; i < 8; i++){
        data <<= 1;
        data |= IIC_ReadBit();
    }

    //主机做出应答
    SDA_OUT();
    if (send_ack) IIC_SDA = 0;
    else IIC_SDA = 1;
    delay_us(2);
    IIC_SCL = 1;
    delay_us(5);
    IIC_SCL = 0;
    delay_us(2);

    //释放总线
    SDA_IN();
    return data;
}


