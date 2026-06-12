#include <stdio.h>
int main ()
{
	int hour1,minute1;
	int hour2,minute2;
	
	printf("请分别输入前后时间差（24小时制）：");
	scanf("%d %d",&hour1,&minute1); 
	scanf("%d %d",&hour2,&minute2); 
	
	int time1,time2,c;
	time1=hour1*60+minute1;
	time2=hour2*60+minute2;
	c=time2-time1;
	
	int h=c/60,m=c%60;
	printf("时间差为:%d小时 %d分钟",h,m);
	
	return 0;
}
