// Heap Sort based on Min Heap. Sorts First K elements in O(k*log(n))
#include <iostream>

using namespace std;

void print_array(int* array, int n)
{
    for(int i=0;i<n;i++)
    {
        cout<<array[i]<<" ";
    }
    cout<<"\n";
}

void heap_insert(int* heap, int element, int curr_heap_size)
{
    int i = curr_heap_size + 1, temp = 0;
    heap[i] = element;

    while(i>1)
    {
        if(heap[i/2] > heap[i])
        {
            temp = heap[i/2];
            heap[i/2] = heap[i];
            heap[i] = temp;
        }
        else
        {
            break;
        }
        i = i/2;
    }
}

void heapify(int* heap, int curr_heap_size, int target_pos)
{
    int i = target_pos, temp = 0, min_val = 0, mini = 1, flag = 0;

    while(i<=curr_heap_size)
    {
        flag = 0;
        if(2*i<=curr_heap_size)
        {
            if(heap[i]>heap[2*i])
            {
                min_val = heap[2*i];
                mini = 2*i;
                flag = 1;
            }
        }

        if((2*i)+1<=curr_heap_size)
        {
            if(flag != 1)
            {
                if(heap[i]>heap[(2*i) + 1])
                {
                    min_val = heap[2*i + 1];
                    mini = (2*i) + 1;
                    flag = 1;
                }
            }
            {
                if(min_val>heap[(2*i) + 1])
                {
                    min_val = heap[(2*i) + 1];
                    mini = (2*i)+1;
                    flag = 1;
                }
            }
        }

        if(flag == 1)
        {
            heap[mini] = heap[i];
            heap[i] = min_val;
            i = mini;
        }
        else
        {
            break;
        }
    }
}

int* heap_sort(int* array, int n, int k)
{
    int* heap = new int[n+1];
    int* sorted_arr = new int[k];
    int curr_heap_size = 0;

    for(int i=0;i<n;i++)
    {
        heap_insert(heap, array[i], curr_heap_size);
        curr_heap_size++;
    }

    for(int i=0;i<k;i++)
    {
        sorted_arr[i] = heap[1];
        heap[1] = heap[curr_heap_size--];
        heapify(heap, curr_heap_size, 1);
    }
    return sorted_arr;
}

int main()
{
    int t, n, k, *array, *sorted_arr;
    cin>>t;         // Number of Test Cases

    for(int i=0;i<t;i++)
    {
        cin>>n;     // Number of elements in Array
        cin>>k;     // For K-least element sorting
        
        if(k<=n)
        {
            array = new int[n];

            for(int j=0;j<n;j++)
            {
                cin>>array[j];
            }
            sorted_arr = heap_sort(array, n, k);
            print_array(sorted_arr, k);
            free(array);
        }
        else
        {
            cout<<"K cannot be greater than Array size\n";
            break;
        }
    }
    return 0;
}