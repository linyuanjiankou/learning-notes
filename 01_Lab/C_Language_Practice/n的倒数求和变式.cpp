#include <stdio.h>
int main()
{
	int x,n=0;
	double i,sum=0;
	scanf("%d",&x);
	for (i=1;i<=x;i++){
		if(n==0){
			sum+=1/i;
			n++; 
			continue;
		}
		if(n==1){
			sum-=1/i;
			n--;
			continue;
		}
		
		
	}
	printf("%f",sum) ;
	
	return 0;
}
