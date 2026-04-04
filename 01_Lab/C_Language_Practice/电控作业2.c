#include <stdio.h>
#include <stdbool.h>

struct Work1Variables{
	int a;
	float b;
	long c;
};

struct Work2Variables{
	int x,y;
	
	bool LogicalAnd;
	bool LogicalOr;
	bool LogicalNot;
};

int work3(int d,int e);
struct Work3Variables{
	int a;
};

struct Work4Variables{
	int a;
	int *p;
	int t;
};

struct Work5Variables{
	int i,result5; 
};

int main(){
	//作业1
	struct Work1Variables work1;
	work1.a=10;
	work1.b=3.14f;
	work1.c=100000L;
	
	//作业2
  	struct Work2Variables work2;
	work2.x=5;
	work2.y=10;
	
	work2.LogicalAnd=(work2.x>1)&&(work2.y<10);
	work2.LogicalOr=(work2.x>1)||(work2.y<10);
	work2.LogicalNot=!(work2.x>0);

	//作业3
	struct Work3Variables work;
	work.a=work3(1,2); 
	
	//作业4
	struct Work4Variables work4;
	work4.a=10;
	work4.p=&work4.a;
	work4.t=5;
	work4.p=&work4.t;
	work4.a=*work4.p;
	
	//作业5
	struct Work5Variables work5;
	work5.result5=0;
	for(work5.i=1;work5.i<101;work5.i++){
		if(work5.i%2==0){
			work5.result5+=work5.i;
		}
	}
	printf("%d",work5.result5);
	
	return 0;
} 

int work3(int d,int e){
	int result=0;
	result=d+e;
	return result;
	
}
