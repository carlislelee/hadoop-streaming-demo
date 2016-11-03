#include <stdio.h>
#include <iostream>
#include <string>

using namespace std;

int main(){
  string key;
  string val = "1";
  while(cin >> key){
    cout << key << "\t" << val << endl;
  }
  return 0;
}
