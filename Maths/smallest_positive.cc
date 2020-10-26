// Link: https://practice.geeksforgeeks.org/problems/smallest-positive-missing-number/0
// Reference: https://www.geeksforgeeks.org/find-the-smallest-positive-number-missing-from-an-unsorted-array-set-2/

// Explanation: This code is based on two obvious principles: 
// (1). The smallest missing number will be between (1, N).
// (2). If the number is present, it will claim its place in the corresponding index in the array.
// Therefore, missing number will be the "index", whose value(array[index]) is not equal to "index".

#include <iostream>

using namespace std;

int missing_no(int* array, int n)
{
    int ind, tmp;

    for(int i=0;i<n;i++)
    {
        ind = array[i];

        if(ind<=0 || ind>n)
            continue;

        while(!(ind<=0 || ind>n))
        {
            if(array[ind-1] != ind)
            {
                tmp = array[ind-1];
                array[ind-1] = ind;
                ind = tmp;
            }
            else
            {
                break;
            }
        }
    }

    for(int i=0;i<n;i++)
    {
        if(array[i]!= i+1)
            return i+1;
    }
    return n+1;
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
	    
	    ans = missing_no(array, n);
	    free(array);
	    cout<<ans<<"\n";
	}
	return 0;
}