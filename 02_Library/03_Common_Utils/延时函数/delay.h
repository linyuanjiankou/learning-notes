#ifndef __DELAY_H__
#define __DELAY_H__

#ifdef __cplusplus
extern "C" {
#endif 

void Delay_Init (void);
void Delay_us (uint32_t nus);
void Delay_ms(uint32_t nms);

#ifdef __cplusplus
}
#endif

#endif
