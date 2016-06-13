#include<iostream>
#include<string>

using std::endl;
using std::cin;
using std::cout;

using std::string;

void print(int * totals);
void print(char * totals);

int main() {

    int totals [50] = {}; // sets all 50 to 0

    char array [50];
    for (unsigned int i = 0; i < 100 ; i++) {
        cin >> array;
        print(totals);
        for (unsigned int j = 0; j < 50; j++) {
            //cout << array[j] << endl;
            //cout << (int)array[j] << endl;
            totals[j] += array[j] - '0';
        }
    }

    for (unsigned int i = 49; i > 0; i--) {
        totals[i - 1] += totals[i] / 10;
    }
    //cout << totals[0];

    print(totals);
    
}

void print(int * totals) {
    for (int i = 0; i < 50; i++) {
        cout << totals[i] << " ";
    }
    cout << endl;
}

void print(char * totals) {
    for (int i = 0; i < 50; i++) {
        cout << totals[i] << " ";
    }
    cout << endl;
}
