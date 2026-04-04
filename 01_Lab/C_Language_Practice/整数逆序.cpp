#include <stdio.h>
int main ()
{
	int a=0,b=0,c=0;
	printf("请输入一个数字：\n");
	scanf("%d",&a);
	while(a!=0){
		b=a%10;
		a/=10;
		printf("%d",b);
}

	
	return 0; 
}
//以上为700输出为007

//以下为700输出为7 

//#include <stdio.h>
//int main ()
//{
	//int a=0,b=0,c=0;
	//printf("请输入一个数字：\n");
//	scanf("%d",&a);
//	while(a!=0){
//		b=a%10;
//      c=c*10+b;
//		a/=10;
//}

//	printf("这个数的逆序数为：",c);
//	return 0; 
//}
 
