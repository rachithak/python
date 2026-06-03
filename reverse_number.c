#include<stdio.h>
 int main()
{
    long long int num,rev,digit;
    rev=0;
    printf("enter a number:");
    scanf("%lld",&num);
    while(num>0)
    {
        digit = num % 10;
        rev = rev * 10 + digit;
        num = num / 10;
    }
    printf("the reversed number is = %lld",rev);
}