#include<iostream>
#include<vector>
#include<math.h>
using namespace std;

void reverseArr(int arr[], int n)
{
    int mid=n/2,i=0;
    while(i<mid)
    {
        int temp=arr[i];
        swap(arr[i], arr[n-i-1]);
        i++;
    }
}

void printArr(vector<int> arr)
{
    for(int i=0; i<arr.size()-1; i++)
    {
        cout<<arr[i]<<" ";
    }
    cout<<endl; 
}

void binarySearch(int arr[], int n, int key)
{
    int low=0,mid;
    int high= n-1;
    while(low<=high)
    {
        mid= low + (high-low)/2;
        if(arr[mid]==key)
        {
            cout<<"Element found at index: "<<mid<<endl;
            return;
        }else if(arr[mid]<key)
        {
            low=mid+1;
        }else
        {
            high=mid-1;
        }
    }
}

void delIndex(vector<int>& arr, int n, int index)
{
    for(int i=index; i<n-1; i++)
    {
        arr[i]=arr[i+1];
    }
}

void indexCount(vector<int>& arr,int n, int key)
{
    int count=0;
    for(int i=0; i<arr.size()-1; i++)
    {
        if(arr[i]==key)
        {
            count++;
            delIndex(arr, n, i);
        }
    }
    for(int i=n-count-1; i<n; i++)
    {
        arr[i]=key;
    }
}

int main()
{
    vector<int> arr= {1,2,3,4,5,6,7,8,9};
    // reverseArr(arr, 10);
    // printArr(arr, 10);
    // binarySearch(arr, 10, 5);
    // indexCount(arr,10, 5);
    // printArr(arr);
    

    
}