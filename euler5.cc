#include <iostream>
using namespace std;

int main(){
    int a = 1000;
    int i;
    while(1){
        for(i=2;i<=10;i++){
            if(a%i!=0){
                a++;
                break;
            }
        }
        //cout<<i;
        if (i==20)
            break;
    }
    cout<<a<<endl;
    return 0;
}
