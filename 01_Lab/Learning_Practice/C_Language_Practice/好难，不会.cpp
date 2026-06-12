#include <stdio.h>
int main(void)
{
	int a,n;//输入的整数为a，位位置为n。 
	scanf("%d %d",&a,&n);
	
	int b;
	b=(a>>(n))&1;
	printf("%d\n",b);// 输出第n位。
	
	int c;
	c= a| (1<<n);
	printf("%d\n",c/n);//将第n位改为1后输出。
	
	int d;
	d= a-(1<<n);
	printf("%d\n",d/n);
	
	return 0;
}
