#include <stdio.h>
#include <stdlib.h>
#include <time.h>
int main()
{
	srand(time(0));
	int c=rand();
	int a,b,n=0;
	a=c%100+1;
	printf("我已经想好一个数了，这个数是一个小于100的正整数，来猜猜看吧!\n");
	
	do{
		scanf("%d",&b);
		n++;
		if(b>a)
			printf("你猜大了，再猜猜看吧！\n");
		else if(b<a)
			printf("你猜小了，再猜猜看吧！\n");
		    
	}while(b!=a);
	
	printf("太棒了，你猜对了！\n你一共猜了%d次。\n",n);
	
	return 0;
	 
 } 
