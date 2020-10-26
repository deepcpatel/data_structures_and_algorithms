// Link : https://practice.geeksforgeeks.org/problems/equilibrium-point/0
#include <iostream>

using namespace std;

int equilibrium_ar(int *array, int n)
{
    int start = -1, end = n;
    int sum_start = 0, sum_end = 0;

    if(n==1)
    {
        return 1;
    }

    while(start != end)
    {
        if(sum_start>sum_end)
        {
            end--;
            sum_end += array[end];
        }
        else if(sum_end>sum_start)
        {
            start++;
            sum_start += array[start];
        }
        else
        {
            if(start+2 == end)
            {
                return start+2;
            }
            else
            {
                start++;
                sum_start += array[start];
            }
        }
    }
    return -1;
}

int main()
{
    int *ar, t, n;

    cin>>t;

    for(int i=0;i<t;i++)
    {
        cin>>n;
        ar = new int[n];

        for(int j=0;j<n;j++)
        {
            cin>>ar[j];
        }
        cout<<equilibrium_ar(ar, n)<<"\n";
        free(ar);
    }
    return 0;
}