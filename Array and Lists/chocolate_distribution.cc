// Link: https://practice.geeksforgeeks.org/problems/chocolate-distribution-problem/0

#include <iostream>

using namespace std;

int get_diff(int* array, int n, int m)
{
	int min = INT_MAX;
    sort(array, array+n, greater<int>());

	for(int i=0;i<(n-m+1);i++)
	{
		if((array[i]-array[m+i-1])<min)
		{
			min = (array[i]-array[m+i-1]);
		}
	}
	return min;
}

int main() 
{
	int t, n, m, ans, *array;
	cin>>t;
	
	for(int i=0;i<t;i++)
	{
	    cin>>n;
	    array = new int[n];
	    
	    for(int j=0;j<n;j++)
	    {
	        cin>>array[j];
	    }
	    cin>>m;
	    ans = get_diff(array, n, m);
	    free(array);
	    cout<<ans<<"\n";
	}
	return 0;
}