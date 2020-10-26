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

void merge(int* array, int p, int q, int r)
{
    int n1 = q - p;
    int n2 = r - q;

    int *temp_ar = new int[n1+n2];

    int i = p, j = q, k = 0;

    while(i<q && j<r)
    {
        if(array[j]<=array[i])
        {
            temp_ar[k] = array[j];
            k++;
            j++;
        }
        else
        {
            temp_ar[k] = array[i];
            k++;
            i++;
        }
    }

    while(i<q)
    {
        temp_ar[k] = array[i];
        i++;
        k++;
    }

    while(j<r)
    {
        temp_ar[k] = array[j];
        j++;
        k++;
    }

    k = 0;
    for(int l=p; l<r;l++)
    {
        array[l] = temp_ar[k];
        k++;
    }
}

void mergeSort(int* array, int p, int r)
{
    int q = p + (r - p)/2;      // We can also write int q = (p + r)/2, but this declaration is stable

    if(p<(r-1))
    {
        mergeSort(array, p, q);
        mergeSort(array, q, r);
        merge(array, p, q, r);
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

        mergeSort(arr, 0, n);
        printArray(arr, 0, n);
        free(arr);
    }
    return 0;
}