#include<iostream>
#include<vector>
using namespace std;

int main(){
    vector<int> x;
    for (int i =0; i<10;i++){
        x.push_back(i);
    }

    vector<int> y;

    for(int i=x.size()-1;i>=0;i--){
        y.push_back(x[i]);
    }
    for (auto &elem:y){
        cout<<elem<<" ";
    }
    cout<<endl;
}
