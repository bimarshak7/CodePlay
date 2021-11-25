#include<iostream>
using namespace std;

bool checkPrime(int n){
    for(int i=2;i<n;i++){
        if(n%i==0)
            return false;
    }
    return true;
}
int main(){
   long long int x=600851475143;
    long long int y = x;
    int max=1;
    while(y%2==0){
        max=2;
        cout<<2<<" ";
        y/=2;
    }
    for(long long int i=3;i<y;i++){
        if(checkPrime(i)){
            if(y%i==0){
                cout<<i<<" ";
                y/=i;
                if (i>max)
                    max=i;
            }
        }
    }
    if (y>max)
        max=y;
    cout<<y<<endl;
    cout<<"Max: "<<max<<endl;
}
