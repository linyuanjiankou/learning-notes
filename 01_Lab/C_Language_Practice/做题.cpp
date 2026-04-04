#include <stdio.h>
int main(void){
	int a,b,c,n;
	scanf("%d %d %d",&a,&b,&c);
	n=a;
	if(n<b){
		n=b;
	}
	if(n<c){
		n=c;
	}
	return n;
	
	
}
