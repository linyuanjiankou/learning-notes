#include <stdio.h>
int main() 
{
	int a=2,i=2,n=0,b,c=1;
	
   	while(c<=50){
	n=0;
		for(i=2 ;i<a ;i++){
		b=a%i;
		if(b==0){
			n+=1;
		}		
	}
	if(n==  0){
		printf("%d\n",a);
		c++;
	}
	a++;
			
	}

	return 0;
}
	
