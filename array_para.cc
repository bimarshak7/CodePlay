// C++ Program to display marks of 5 students

#include <iostream>
using namespace std;

// declare function to display marks
// take a 1d array as parameter
void display(int m[]) {
    cout << "Displaying marks: " << endl;
    m[3]++;
    // display array elements    
    for (int i = 0; i < 5; ++i) {
        cout << "Student " << i + 1 << ": " << m[i] << endl;
    }
}

int main() {
    // declare and initialize an array
    int marks[5] = {88, 76, 90, 61, 69};
    
    // call display function
    // pass array as argument
    display(marks);

    cout<<marks[3]<<endl;

    return 0;
}
