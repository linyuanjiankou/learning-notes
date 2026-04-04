#include<stdio.h>

void swap(int *pa,int *pb);

int main(void)
{
	int a,b;
	scanf("%d %d",&a,&b);
	swap(&a,&b);
	printf("a=%d,b=%d",a,b);
}

void swap(int *pa,int *pb)
{
	int t;
	t=*pa;
	*pa=*pb;
	*pb=t;
	
}
