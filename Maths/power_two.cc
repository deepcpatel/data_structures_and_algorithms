// Link : https://practice.geeksforgeeks.org/problems/power-of-2/0
#include <iostream>

using namespace std;

int main()
{
    int t;
    long n;
    cin>>t;

    for(int i=0;i<t;i++)
    {
        cin>>n;


        if(n == 0)
        {
            cout<<"NO";
        }
        else if((n&(n-1)) == 0)
        {
            cout<<"YES\n";
        }
        else
        {
            cout<<"NO\n";
        }
    }
    return 0;
}