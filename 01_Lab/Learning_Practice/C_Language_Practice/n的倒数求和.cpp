#include <stdio.h>
int main()
{
	int x;
	double i,sum=0;
	scanf("%d",&x);
	for (i=1;i<=x;i++){
		sum+=1/i;
	}
	printf("%f",sum) ;
	
	return 0;
}
