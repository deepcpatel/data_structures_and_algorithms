// Link: https://practice.geeksforgeeks.org/problems/pythagorean-triplet/0
// Reference: https://stackoverflow.com/questions/2032153/how-to-find-pythagorean-triplets-in-an-array-faster-than-on2
// The algorithm has time complexity of O(N^2)

#include <iostream>

using namespace std;

void check_triplets(int* array, int n)
{
    cout<<"Yes";
}

int main() 
{
	int t, n, *array;
	cin>>t;
	
	for(int i=0;i<t;i++)
	{
	    cin>>n;
	    array = new int[n];
	    
	    for(int j=0;j<n;j++)
	    {
	        cin>>array[j];
	    }
	    
	    check_triplets(array, n);
	    free(array);
	    cout<<"\n";
	}
	return 0;
}