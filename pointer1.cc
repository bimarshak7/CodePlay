#include<iostream>

using namespace std;

int main(){
    long int a[3]={12,121,7};
    long int *ptr;
    ptr=a;
    
    cout<<a<<endl;
    cout<<*(ptr)<<endl;
    cout<<a+1<<endl;
    cout<<*(ptr+1)<<endl;
}
