#include <iostream>

using namespace std;

void printArray(int *arr, int beg, int size)
{
    for (int i=beg; i<size; i++)
    {
        cout<<arr[i]<<" ";
    }
    cout<<"\n";
}

int partition(int* array, int p, int r)
{
    int start = p, end = r-1, temp = -1;
    int part_val = array[end];
    
    while(start<end)
    {
        if(array[start]>part_val)
        {
            if(array[end]<=part_val)
            {
                temp = array[start];
                array[start] = array[end];
                array[end] = temp;
            }
            else
            {
                end--;
            }
        }
        else
        {
            start++;
        }
    }
    return start;
}

void quickSort(int* array, int p, int r)
{
    if(p<(r-1))
    {
        int q = partition(array, p, r);
        quickSort(array, p, q);
        quickSort(array, q, r);
    }
}

int main()
{
    int *arr, n, T;
    cin>>T;

    for(int j=0;j<T;j++)
    {
        cin>>n;
        arr = new int[n];

        for(int i=0;i<n;i++)
        {
            cin>>arr[i];
        }

        quickSort(arr, 0, n);
        printArray(arr, 0, n);
        free(arr);
    }
    return 0;
}