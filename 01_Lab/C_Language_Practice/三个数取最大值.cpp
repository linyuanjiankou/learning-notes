#include<stdio.h>
int main()
{
	int a,b,c;
	
	printf("请分别输入三个整数：");
	scanf("%d %d %d",&a,&b,&c);
	
	int max=a;
	if(max<=b){
		max=b ;
}
	if(max<=c){
		max=c ;
}
    printf("最大的数为：%d\n",max);
}
