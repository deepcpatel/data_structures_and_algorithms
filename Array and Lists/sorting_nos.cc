// Link : https://practice.geeksforgeeks.org/problems/sort-an-array-of-0s-1s-and-2s/0
#include <iostream>

using namespace std;

int main()
{
    int ar[3], t, n, temp;

    cin>>t;

    for(int i=0;i<t;i++)
    {
        cin>>n;

        ar[0] = 0;
        ar[1] = 0;
        ar[2] = 0;

        for(int j=0;j<n;j++)
        {
            cin>>temp;
            ar[temp] += 1;
        }

        for(int k=0;k<3;k++)
        {
            for(int l=0;l<ar[k];l++)
            {
                cout<<k<<" ";
            }
        }
        cout<<"\n";
    }

    return 0;
}
