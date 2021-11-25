#include<iostream>
using namespace std;

int main(){
    int sum = 0;
    int l;
    cout<<"Enter limit: ";
    cin>>l;
    for(int i=3;i<l;i++){
        if(i%3==0 || i%5==0)
            sum+=i;
    }

    cout<<"Sum: "<<sum<<endl;
}
