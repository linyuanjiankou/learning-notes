#include <stdio.h>
int main()
{
	double foot=0;
	double inch=0;
	
	printf("请输入英尺数和英寸数：");

	scanf("%lf %lf",&foot,&inch);
	
	double m=((foot+inch/12)*0.3048);
	printf("即%f米\n",m);
}
