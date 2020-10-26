// Link : https://practice.geeksforgeeks.org/problems/missing-number-in-array/0
#include <iostream>

using namespace std;

int main()
{
    int t, n, sum_n, sum_ar, temp;
    cin>>t;

    for(int i=0;i<t;i++)
    {
        cin>>n;
        sum_n = 0;
        sum_ar = 0;

        for(int j=1;j<=n;j++)
        {
            sum_n = sum_n + j;
        }

        for(int j=0;j<n-1;j++)
        {   
            cin>>temp;
            sum_ar = sum_ar + temp;
        }
        cout<<sum_n-sum_ar<<"\n";
    }
    return 0;
}