#include<iostream>
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

        BigInt operator + (BigInt & B){
            int carry;

        }
};

int main(){
    BigInt a("122222");
    cout << a;
    return 0;
}
