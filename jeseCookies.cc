#include <bits/stdc++.h>

using namespace std;



int main() {
    int n,k,el;
    priority_queue<int, vector<int>, greater<int> > q;
    cin >> n >> k;
    int a;
    int s=0;
    for(int i=0;i<n;i++){
        cin>>el;
        q.push(el);
    }
    while(q.top()<k){
            if (q.size() < 2) {
                cout<<-1;    
                return 0;
        }
            a = q.top();
            q.pop();
            a+=2*q.top();
            q.pop();
            q.push(a);
            s++;
    }
    cout<<s;
    return 0; 
}
