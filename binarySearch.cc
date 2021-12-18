#include<iostream>
using namespace std;

int main(){
    int arr[7]={100,100,50,40,40,20,10};
    int ranks[7]={1,1,2,3,3,4,5};
    int elem = 50;
    int lo=0, hi=6;
    int mid;
    while(hi-lo>1){
        mid = (hi+lo)/2;
        if(arr[mid]>elem){
            if(arr[mid+1]<elem){
                cout<<"New pos: "<<ranks[mid+1];
                break;
            }

            lo = mid+1;
        }
        else{
            hi = mid;
        }
        if(arr[mid-1]>elem){
                cout<<"New pos: "<<ranks[mid];
                break;
        }
    
    }
    if(arr[lo]==elem){
        cout<<ranks[lo]<<" "<<elem;
    }
    else if(arr[hi]==elem)
        cout<<ranks[hi]<<" "<<elem;
}
