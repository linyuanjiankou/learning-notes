#include <stdio.h>
int main()
{
	int n;
	scanf("%d",&n);
	int a=1,i=1;
	for (i=1;i<=n;i++){
		a*=i;
	}
	printf("%d",a);
	return 0;
	
 } 
