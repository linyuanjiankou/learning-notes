#include <stdio.h>
int check(int x); 
int main(void)
{
	int max=25;
	int a[max];
	
	int i,x,c;
	for (i=0;i<=max;i++){
		a[i]=1;
	}
	
	for (x=2;x<=max;x++){
		if(a[x]==1&&check(x)==0){
			i=2;
			while(x*i<=max){
				a[i*x]=0;
				i++;
			}
		}else{
			a[x]=0;
		}
	}
	
	for(i=2;i<=max;i++){
		if(a[i]==1){
			printf("%d\t",i);
		}
	}
	printf("\n");
	
	return 0;
}

int check(int x)
{
	int b=2,cnt=0;
	for(b=2;b<x;b++){
		if(x%b==0){
			cnt++;
			break;
		}
	}
	if(cnt==0){
		return cnt;
	}
}
