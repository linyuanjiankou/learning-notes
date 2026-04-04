#include <stdio.h>
int main()
{
	int n=0;
	double sum=0,b=0,average=0;
	
	printf("请输入第%d个数。\n",n+1);
	scanf("%lf",&b);
	while(b!=-1){	
		sum+=b;
		n++;
		printf("请输入第%d个数。\n",n+1);
		scanf("%lf",&b);
	    
	}
	average=sum/n;
	printf("这些数的平均数为：%f",average);
	return 0;
}
