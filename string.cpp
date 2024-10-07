#include<iostream>
#include<math.h>
using namespace std;

void replaceSpaces(string s){
    int count = 0;
    // for(int i=0; i<s.length(); i++){
    //     if(s[i] == ' '){
    //         count++;
    //     }
    // }
    // int newLength = s.length() + count*2;
    // char newString[newLength];
    // for(int i=s.length()-1; i>=0; i--){
    //     if(s[i] == ' '){
    //         newString[newLength-1] = '0';
    //         newString[newLength-2] = '2';
    //         newString[newLength-3] = '%';
    //         newLength = newLength - 3;
    //     }else{
    //         newString[newLength-1] = s[i];
    //         newLength = newLength - 1;
    //     }
    // }
    // cout<<newString;

    string newString;
    for(int i=0; i < s.length();i++)
    {
        if(s[i]==' ')
        {
            newString.push_back('@');
            newString.push_back('4');
            newString.push_back('0');
        }
        else
        {
            newString.push_back(s[i]);
        }
    }
    cout<<newString;
}
int main(){
    string s;
    cin.getline(s);
    // find spaces
    // replace spaces
}
