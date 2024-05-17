#include<stdio.h>
int main()
{
int n;
int n1,n2,n3,n4,n5;
int a1,a2,a3,a4,a5;
printf("Enter a five digit number:-\n");
scanf("%d",&n);

n1=n/10000;
a1=n%10000;
n2=a1/1000;
a2=a1%1000;
n3=a2/100;
a3=a2%100;
n4=a3/10;
a4=a3%10;
n5=a4/1;
a5=a4/1;

int x=(10000*n5)+(1000*n4)+(100*n3)+(10*n2)+(1*n1);
printf("Reverse is:- %d \n",x);

if (n==x)
printf("Given number is equal of its reverse");
else
printf("Given number is not equal of its reverse");
return 0;
}
