#include<iostream>
using namespace std;

int factorial(int n){
    int fact =1;
    for (int i=1;i<=n;i++)
        fact*=i;
    return fact;
}
int fsum(int n){
    int sum = 0;
    while(n!=0){
        sum+=factorial(n%10);
        n/=10;
    }
    return sum;
}
int sf(int n){
    int sum = n%10;
    while(n/10!=0){
        n/=10;
    }
    sum += n;
    return sum;
}
int main(){
    cout<<fsum(324)<<endl;
    cout<<sf(342)<<endl;
}
