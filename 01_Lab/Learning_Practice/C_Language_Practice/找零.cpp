#include <stdio.h>
int main()
{
	int amount=0;
	int price=0;

	printf("请输入金额（元）:");
	scanf("%d", &price);
	
	printf("请输入面值（元）:");
	scanf("%d", &amount);
	
	int change=amount-price;
	
		if(change<0){
		printf("余额不足，不能购买\n"); 
}else{
	printf("找您：%d元\n",change); 
} 
	
	return 0; 
 } 
