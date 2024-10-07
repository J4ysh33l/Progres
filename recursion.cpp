#include<iostream>
using namespace std;
// int sumOfArr(int arr[],int n){
//     if(n==1||n==0){
//         return arr[0];
//     }else{
//         // return arr[n-1]+sumOfArr(arr,n-1);
//         return arr[0]+sumOfArr(arr+1,n-1); // this is the recursive call
//     }
    
// }

// bool linearSearch(int arr[],int n,int key,int start,int end){
    
//     if(start>end){
//         return false;
//     }
//         int mid=start + (end-start)/2;
//         if(arr[mid]==key){
//             return true;
//         }else if(arr[mid]<key){
//             return linearSearch(arr,n,key,mid+1,end);
//         }else if(arr[mid]>key){
//             return linearSearch(arr,n,key,start,mid-1);
//         }
//     return false;
// }

bool checkPalindrome(string arr, int i,int j){
    if(i>j){
        return true;
    }
    if(arr[i]!=arr[j] ){
        return false;
    }else{
        return checkPalindrome(arr,i+1,j-1);
    }
}
int main(){
    string name="madam";
    // cout<<sumOfArr(arr,4);
    // cout<<linearSearch(arr,4,26,0,4);
    cout<<checkPalindrome(name,0,4);
    return 0;
}