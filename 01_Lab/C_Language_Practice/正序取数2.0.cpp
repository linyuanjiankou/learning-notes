#include <stdio.h>
int main()
{
	int x,i=1;
	scanf("%d",&x);
	
	int a=x;
	while(a>=10){
		a/=10;
		i*=10;
	}
	
	int b;
	do{
		b=x/i;
		printf("%d",b);
		if (i>1){
			printf(" ");
		}
		x%=i;
		i/=10;
		
	}while(i>=1);
	
	return 0;
}
