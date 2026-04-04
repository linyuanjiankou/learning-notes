#include <stdio.h>
int main() 
{
	int a=2,i=2,n=0,b;
	
   	for(a=2 ;a<=100 ;a++){
	n=0;
		for(i=2 ;i<a ;i++){
		b=a%i;
		if(b==0){
			n+=1;
		}		
	}
	if(n==  0){
		printf("%d\n",a);
	}		
	}

	return 0;
}
	

