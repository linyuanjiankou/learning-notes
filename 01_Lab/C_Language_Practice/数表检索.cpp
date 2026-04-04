#include<stdio.h>
int search(int a[],int x,int length);
int main(void)
{
	int a[]= {1,4,6,3,7,45,7,8,12,14,16};
	int length=sizeof(a)/sizeof(a[0]);
	int x,b;
	scanf("%d",&x);
	
	b=search(a,x,length);
	if(b==-1){
		printf("这个数不存在\n");
	}else{
		printf("这个数在%d这个位置上\n",b);
	}
	
	return 0;
}
	int search(int a[],int x,int length)
	{
		int location=-1;
		int i=0;
		for(i=0;i<length;i++){
			if(a[i]==x){
				location=i;
				break;
			}
		}
	return location;
	}

