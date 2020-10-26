// Link: https://practice.geeksforgeeks.org/problems/trapping-rain-water/0

#include <iostream>

using namespace std;

int min(int a, int b)
{
    if(a<b)
        return a;
    else
        return b;
}

int trapped_water(int* array, int n)
{
    int left_max[n], right_max[n], l_temp = -1, r_temp = -1, trapped_water = 0;

    for(int i=0;i<n;i++)
    {
        if(array[i]>l_temp)
        {
            l_temp = array[i];
        }

        if(array[(n-1)-i]>r_temp)
        {
            r_temp = array[(n-1)-i];
        }

        left_max[i] = l_temp;           // Filling max numbers from left side
        right_max[(n-1)-i] = r_temp;    // Filling max numbers from right side
    }

    for(int i=0;i<n;i++)
    {
        trapped_water += (min(left_max[i], right_max[i]) - array[i]);
    }

    return trapped_water;
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
	    
	    ans = trapped_water(array, n);
	    free(array);
	    cout<<ans<<"\n";
	}
	return 0;
}