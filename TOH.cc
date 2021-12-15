#include<iostream>
#include<math.h>
using namespace std;

void TOH(int n, char L, char A, char R){
    if (n){
        TOH(n-1,L,R,A);
        cout<<L<<" -> "<< R<<endl;
        TOH(n-1,A,L,R);
    }
}

int main(){
    int n;
    cout<<"Enter no of disks ";
    cin>>n;
    TOH(n,'L','A','R');
    cout<<"Done!"<<endl;
    cout<<"No. of Steps: "<<pow(2,n)-1<<endl; 
    return 0;
}
