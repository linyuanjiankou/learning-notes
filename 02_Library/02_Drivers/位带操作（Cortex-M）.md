先给最终成品（STM32C8T6 · GPIO）：
```
//位带操作
//IO口操作宏定义
#define BITBAND(addr, bitnum) ((addr & 0xF0000000)+0x2000000+((addr &0xFFFFF)<<5)+(bitnum<<2)) 
#define MEM_ADDR(addr)  *((volatile unsigned long  *)(addr)) 
#define BIT_ADDR(addr, bitnum)   MEM_ADDR(BITBAND(addr, bitnum)) 
//IO口地址映射
#define GPIOA_ODR_Addr    (GPIOA_BASE+12) //0x4001080C 
#define GPIOB_ODR_Addr    (GPIOB_BASE+12) //0x40010C0C 
#define GPIOC_ODR_Addr    (GPIOC_BASE+12) //0x4001100C 
#define GPIOD_ODR_Addr    (GPIOD_BASE+12) //0x4001140C 
#define GPIOE_ODR_Addr    (GPIOE_BASE+12) //0x4001180C 
#define GPIOF_ODR_Addr    (GPIOF_BASE+12) //0x40011A0C    
#define GPIOG_ODR_Addr    (GPIOG_BASE+12) //0x40011E0C    

#define GPIOA_IDR_Addr    (GPIOA_BASE+8) //0x40010808 
#define GPIOB_IDR_Addr    (GPIOB_BASE+8) //0x40010C08 
#define GPIOC_IDR_Addr    (GPIOC_BASE+8) //0x40011008 
#define GPIOD_IDR_Addr    (GPIOD_BASE+8) //0x40011408 
#define GPIOE_IDR_Addr    (GPIOE_BASE+8) //0x40011808 
#define GPIOF_IDR_Addr    (GPIOF_BASE+8) //0x40011A08 
#define GPIOG_IDR_Addr    (GPIOG_BASE+8) //0x40011E08 
 
//IO口操作,只对单一的IO口!
//确保n的值小于16!
#define PAout(n)   BIT_ADDR(GPIOA_ODR_Addr,n)  //输出 
#define PAin(n)    BIT_ADDR(GPIOA_IDR_Addr,n)  //输入 

#define PBout(n)   BIT_ADDR(GPIOB_ODR_Addr,n)  //输出 
#define PBin(n)    BIT_ADDR(GPIOB_IDR_Addr,n)  //输入 

#define PCout(n)   BIT_ADDR(GPIOC_ODR_Addr,n)  //输出 
#define PCin(n)    BIT_ADDR(GPIOC_IDR_Addr,n)  //输入 

#define PDout(n)   BIT_ADDR(GPIOD_ODR_Addr,n)  //输出 
#define PDin(n)    BIT_ADDR(GPIOD_IDR_Addr,n)  //输入 

#define PEout(n)   BIT_ADDR(GPIOE_ODR_Addr,n)  //输出 
#define PEin(n)    BIT_ADDR(GPIOE_IDR_Addr,n)  //输入

#define PFout(n)   BIT_ADDR(GPIOF_ODR_Addr,n)  //输出 
#define PFin(n)    BIT_ADDR(GPIOF_IDR_Addr,n)  //输入

#define PGout(n)   BIT_ADDR(GPIOG_ODR_Addr,n)  //输出 
#define PGin(n)    BIT_ADDR(GPIOG_IDR_Addr,n)  //输入

```

# 解释如下（如果有人想看的话）

**背景知识：**

位带是一种硬件特性，允许你通过访问一个“别名地址”来原子地操作另一个地址中的某一位，而不需要“读-改-写”。

在 Cortex-M 中，有两个区域支持位带：

* **SRAM 区**：从 `0x2000_0000` 开始的 1MB（即 `0x2000_0000 ~ 0x200F_FFFF`）
* **外设区**：从 `0x4000_0000` 开始的 1MB（即 `0x4000_0000 ~ 0x400F_FFFF`）

这两个区域中的每一个**比特（bit）**，都在一个叫 **“位带别名区（Bit-Band Alias Region）”** 的地方有一个对应的 32 位地址。

- **SRAM 位带别名区**：`0x2200_0000 ~ 0x23FF_FFFF`
- **外设位带别名区**：`0x4200_0000 ~ 0x43FF_FFFF`

根据 ARM 手册，位带别名地址计算公式为：
```alias_addr = alias_region_base + (byte_offset * 32) + (bit_number * 4)```

其中：
- `alias_region_base = (addr & 0xF0000000) + 0x02000000`
- `byte_offset = addr & 0x000FFFFF`

代入后可得：```alias_addr = (addr & 0xF0000000) + 0x02000000 + ((addr & 0xFFFFF) << 5) + (bitnum << 2)```

**三个常数的由来：**
1. 0xF0000000：
	Cortex-M 使用地址的**最高 4 位**来判断该地址属于哪个内存区域，`0xF0000000` 的二进制是 `1111 0000 ... 0000`（32 位），用它和地址做 `&` 运算，就是**保留高 4 位，清零低 28 位**。
	所以：
	- 如果 `addr = 0x4001080C`（GPIOA_ODR），那么 `addr & 0xF0000000 = 0x40000000`
	- 如果 `addr = 0x20000010`（SRAM 变量），那么 `addr & 0xF0000000 = 0x20000000`
	这个值决定了我们要映射到 **外设别名区（0x42000000）** 还是 **SRAM 别名区（0x22000000）**。

2. 0x02000000：
	ARM 官方规定：
	- 外设区 `0x40000000` → 别名区 `0x42000000`，**偏移 = 0x02000000**
	- SRAM 区 `0x20000000` → 别名区 `0x22000000`，**偏移 = 0x02000000**
	所以无论你是外设还是 SRAM，**别名区基地址 = 原区域基地址 + 0x02000000**
	因此，`+ 0x2000000` 就是加上这个固定的偏移量。

3. 0xFFFFF：
	位带只对每个区域的**前 1MB（= 2^20 字节）** 有效。
	`0xFFFFF` = `2^20 - 1` = `1,048,575`，二进制是 **20 个 1**。
	所以 `addr & 0xFFFFF` 就是提取地址的**低 20 位**，也就是该地址在所属区域（SRAM 或外设）中的**字节偏移**（必须 < 1MB）。


