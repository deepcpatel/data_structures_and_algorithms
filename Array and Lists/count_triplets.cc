// Link: https://practice.geeksforgeeks.org/problems/count-the-triplets/0
#include <iostream>

using namespace std;

int count_triplets(int *array, int n)
{
    
    return 0;
}

int main()
{
    int t, n, *array, temp;

    cin>>t;

    for(int i=0;i<t;i++)
    {
        cin>>n;
        array = new int[n];
        for(int j=0;j<n;j++)
        {
            cin>>array[j];
        }
        temp = count_triplets(array, n);
        cout<<temp<<"\n";
        free(array);
    }
    return 0;
}
