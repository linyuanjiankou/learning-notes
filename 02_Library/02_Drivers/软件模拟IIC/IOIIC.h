#ifndef __IOIIC_H__
#define __IOIIC_H__ 

#ifdef __cplusplus
extern "C" {
#endif 

#include "bitband.h"

//IO方向设置
#define SDA_IN()  { GPIOB->CRH &= 0XFFFFFF0F; GPIOB->CRH |= (8 << 4) ;} //输入模式
#define SDA_OUT() { GPIOB->CRH &= 0XFFFFFF0F; GPIOB->CRH |= (3 << 4);} // 推挽输出 50MHz

//IO操作函数
#define IIC_SCL PBout(8) //SCL
#define IIC_SDA PBout(9) //SDA
#define IIC_SDA_READ PBin(9) //输入SDA

void IIC_Start(void);
void IIC_Stop(void);
void IIC_SendBit(uint8_t bit);
uint8_t IIC_SendByte(uint8_t data);
uint8_t IIC_ReadBit(void);
uint8_t IIC_ReadByte(uint8_t send_ack);

#ifdef __cplusplus
}
#endif

#endif