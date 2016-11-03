#include <string>
#include <map>
#include <iostream>
#include <iterator>
using namespace std;
int main(){
  string key;
  string value;
  map<string, int> count;
  map<string, int>::iterator it;

  while(cin>>key){
    cin>>value;
    it = count.find(key);
    if(it != count.end()){
      (it->second)++;
    }else{
      count.insert(make_pair(key, 1));
    }
  }
  for(it = count.begin(); it != count.end(); ++it){
    cout<<it->first<<"\t"<<it->second<<endl;
  }
  return 0;
}
