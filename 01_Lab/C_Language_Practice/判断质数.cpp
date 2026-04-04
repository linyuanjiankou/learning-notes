#include <stdio.h>
int main()
{
	int x,a,i=1,n=0;
	scanf("%d",&x);
	
	for(i=1 ;i<=x ;i++){
		a=x%i;
		if(a==0){
			n+=1;
		}
	}

	if(n==2)
	printf("%d是质数",x);
	else
	printf("%d不是质数",x);
	
	return 0;
}
