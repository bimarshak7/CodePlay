#include<iostream>
#include <bits/stdc++.h>
#include <vector>
#include <string>
using namespace std;

class BigInt {
    private:
        vector<int> bigint;

    public:
        BigInt(){};
        BigInt (string num ){
            int size = num.size();
            for(auto i=0;i<=size-1;i++){
                bigint.push_back(num[i]- static_cast<int>('0'));
            }
        }

        friend ostream &operator<<( ostream &output, const BigInt &B ) {
            for(auto it=B.bigint.begin();it!=B.bigint.end();it++){
                output << *it;
            }
            output<<endl;
            return output;
        }
        BigInt reverse(BigInt N){
            BigInt tmp;
                for(int i = N.bigint.size()-1; i >= 0; i--){
                    tmp.bigint.push_back(N.bigint[i]);
                }
                return tmp;
        }
        BigInt operator + (BigInt & B){
            int carry;
            string result;
            B = reverse(B);
            *this = reverse(*this);
            int size = B.bigint.size()>this->bigint.size()? B.bigint.size(): this->bigint.size();
            return rev;
        }
};

int main(){
    BigInt a("122222");
    BigInt b("1234");
    cout << a;
    cout<<a+b;
    return 0;
}
