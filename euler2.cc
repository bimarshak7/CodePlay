#include<iostream>
using namespace std;

int main(){
    int a = 1;
    unsigned long int sum = 0;
    int b=1;
    int c;
    for (int i=1;i<4000000;i++){
        //cout<<a<<" ";
        if (a%2==0)
            sum+=a;
        c=b;
        b=a;
        a+=c;
    }
    cout<<"sum: "<<sum<<endl;
}
