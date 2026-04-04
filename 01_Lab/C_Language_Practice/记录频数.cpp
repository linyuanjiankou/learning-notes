#include <stdio.h>
int main(void)
{
	const int number=10;
	int i=0,x=0;
	int cnt[number];
	
	for(i=0;i<number;i++){
		cnt[i]=0;
	}
	
	scanf("%d",&x);
	while(x!=-1){
		if(x<=9&&x>=0){
			cnt[x]++;
		}
		scanf("%d",&x);	
	}
	
	for(i=0;i<number;i++){
		printf("%d出现了%d次\n",i,cnt[i]);
	}
	
	return 0;
}
