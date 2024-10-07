#include<iostream>
using namespace std;

int main(){
    int arr[10]= {23,122,24,67};

    cout<<" address of first memory block is "<<arr<<endl;
    cout<<" address of first memory block is "<<&arr[0]<<endl;
    cout<<" value of zero index /first memory block is "<<*arr<<endl;
    cout<<" value of first index/ memory block is "<<*(arr+1)<<endl;
    cout<<" value of second index/ memory block is "<<*(arr+2)<<endl;

    cout<<"size of arr " <<sizeof(arr[0])<<endl;
    cout<<"size of arr " <<sizeof(&arr)<<endl;


    // arr[i]= *(arr+i)
    // or i[arr]= *(i+ arr)


}