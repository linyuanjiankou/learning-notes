#include <stdio.h>
int main()
{
	int x,a=0,i,b;
	scanf("%d",&x);
	
	do{
		i=x%10;
		a=a*10+i;
		x/=10;
	}while(x!=0);
	
	do{
		b=a%10;
		printf("%d",b);
		a/=10;
		if(a!=0){
			printf(" ");
		}
	}while(a!=0);
	
	return 0;
}
