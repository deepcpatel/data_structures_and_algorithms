// Link: https://practice.geeksforgeeks.org/problems/kadanes-algorithm/0

#include<iostream>

using namespace std;

int max_sum(int* array, int n)
{
    int max_sum, sum;
    
    max_sum = array[0];
    sum = array[0];
    
    for(int i=1;i<n;i++)
    {
        sum += array[i];
        
        if(array[i]>sum)
        {
            sum = array[i];
        }
        
        if(sum>max_sum)
        {
            max_sum = sum;
        }
    }
    return max_sum;
}

int main()
{
    int t, n, *array, ans;
    cin>>t;
    
    for(int i=0;i<t;i++)
    {
        cin>>n;
        array = new int[n];
        
        for(int j=0;j<n;j++)
        {
            cin>>array[j];
        }
        
        ans = max_sum(array, n);
        cout<<ans<<"\n";
        free(array);
    }
    return 0;
}