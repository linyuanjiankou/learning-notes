#include <stdio.h>
int main()
{
	int one=0,two=0,five=0,i; //设定一角、两角、五角个数 
	int x;//设定输入的目标金额
	scanf("%d",&x);
	
	for(five=0;five*5<=x*10;five++){
		for(two=0;two*2<=x*10;two++){
			for(one=0;one<=x*10;one++){
				if(5*five+2*two+one==x*10){
					printf("%d个一角、%d个两角、%d个五角可以组成%d元\n",one,two,five,x);
					i++;
				}
			}
		}
	}
	
	printf("%d",i);
	return 0;                                 
 } 
