//Find the largest palindrome made from the product of two 3-digit numbers.

#include<iostream>
using namespace std;
bool checkPalindrome(int num){
    int tmp=num;
    int p=0;
    int r;
    while(tmp!=0){
        r = tmp%10;
        tmp = tmp/10;
        p=p*10+r;
    }
    if(p==num)
        return true;
    return false;
}
int main(){
    int max = 1;
    for (int i=999;i>99;i--){
        for(int j=999;j>99;j--){
            if(checkPalindrome(i*j)){
                //cout<<i*j;
                if ((i*j)>max)
                    max = i*j;
            }        
        }
    }
    cout<<max<<endl;
}
