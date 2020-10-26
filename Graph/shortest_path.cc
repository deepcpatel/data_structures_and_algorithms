/*
Clutter 2019:

I got this question in a Hackerrank assessment for a CA based company for New Grad SDE position. My solution had TLE for hidden test cases. My idea was to expand edges to have weight 1 by inserting w-1 nodes between every pair of nodes where w is the weight of the edge between them. Now find all the shortest paths (there may be more than 1 path with same total weight) between the source and the destination using BFS and DFS. I'm unable to code a working solution for this question even days after the interview. Can anyone come up with the code?

Question

You need to travel between cities, but some roads may have been blocked by a recent storm. You want to check before you travel to make sure you avoid them. Given a map of the cities and their bidirectional roads, determine which roads are along any shortest path so you can check that they are not blocked. The roads or edges are named using their 1-based index within the input arrays.

For example, given a map of g_nodes = 5 nodes, the starting nodes, ending nodes and road lengths are:

Road from/to/weight
1 (1, 2, 1)
2 (2, 3, 1)
3 (3, 4, 1)
4 (4, 5, 1)
5 (5, 1, 3)
6 (1, 3, 2)
7 (5, 3, 1)

You always need to go from node 1 to node g_nodes, so from node 1 to node 5 in this case. The shortest path is 3, and there are three paths of that length: 1 → 5, 1 → 2 → 3 → 5, and 1 → 3 → 5. We create an array of strings, one for each road in order, where the value is YES if a road is along a shortest path or NO if it is not. In this case, the resulting array is [YES, YES, NO, NO, YES, YES, YES].

Function Description

Complete the function classifyEdges in the editor below. The function must return an array of g_edges strings where the value at ith index is YES if the ith edge is a part of a shortest path from vertex 1 to vertex g_nodes. Otherwise it should contain NO.

classifyEdges has the following parameter(s):

    g_nodes: an integer, the number of nodes
    g_from[g_from[1],...g_from[g_nodes]]: an array of integers, the start g_nodes for each road
    g_to[to[1],...g_to[g_nodes]]: an array of integers, the end g_nodes for each road
    g_weight[g_weight[1],...g_weight[g_nodes]]: an array of integers, the lengths of each road

Constraints

    2 ≤ g_nodes ≤ 3000
    1 ≤ g_edges ≤ min(105, (g_nodes x g_nodes - 1)/2)
    1 ≤ g_weight[i] ≤ 105
    1 ≤ g_from[i], g_to[i] ≤ g_nodes
    There is at most one edge between any pair of g_nodes
    The given graph is connected

Sample Input 1

4 5
1 2 1
2 4 1
1 3 1
3 4 2
1 4 2

Sample Output 1

YES
YES
NO
NO
YES

Sample Input 2

5 7
1 2 1
2 3 1
3 5 1
1 4 1
4 5 2
3 4 2
2 4 4

Sample Output 2

YES
YES
YES
YES
YES
NO
NO

Sample Input 3

4 5
1 2 1
1 3 1
1 4 1
2 3 1
2 4 1

Sample Output 3

NO
NO
YES
NO
NO
*/

#include<iostream>
#include<climits>
#include "dictionary.h"

using namespace std;

struct node
{
    int dest = -1;              // Node Number
    int cost = INT_MAX;         // Node Cost
    struct node* next = NULL;

    node(int d, int w, struct node* n) : dest(d), cost(w), next(n) {}   // Constructor
};

pair<vector<int>, vector<int>> djikstra_algorithm(dict<int, struct node*>& graph, int source, int dest)
{
    vector<int> key_vec = graph.keys();
    vector<int> dist, prev;        // Shortest Distance [dist] from the previous node [prev] (both Zero Indexed)
    
    int min = INT_MAX, min_idx = -1, q = -1, alt = -1, n = key_vec.size();
    
    struct node* temp = NULL;

    // Initializing values
    for(int i=0;i<=key_vec.size();i++)
    {
        dist.push_back(INT_MAX);
        prev.push_back(-1);
    }
    dist[source-1] = 0;     // Source distance is 0

    // Iterating over all the nodes
    while(n>0)
    {
        min = INT_MAX;
        min_idx = -1;

        // Finding minimum element
        for(int i=0;i<key_vec.size();i++)
        {
            if(key_vec[i] != -1)
            {
                if(min > dist[key_vec[i]-1])
                {
                    min = dist[key_vec[i]-1];
                    q = key_vec[i];
                    min_idx = i;
                }
            }
        }
        key_vec[min_idx] = -1;   // Removing the element from the bag
        n--;

        // Iterating over the neighbours of node q
        temp = graph[q];
        while(temp != NULL)
        {
            alt = dist[q-1] + temp->cost; 
            if(alt < dist[temp->dest-1])
            {
                dist[temp->dest-1] = alt;   // Setting Minimum Distance
                prev[temp->dest-1] = q;
            }
            temp = temp->next;
        }
    }
    return make_pair(dist, prev);
}

template<typename T, typename U> void print_graph(dict<T, U>& v) // Display Graph
{
    vector<T> key_vec = v.keys();

    cout<<"Graph:\n";
    for(int i=0;i<key_vec.size();i++)
    {
        U temp = v[key_vec[i]];

        cout<<"Node "<<key_vec[i]<<" => ";
        while(temp != NULL)
        {
            cout<<"("<<temp->dest<<", "<<temp->cost<<")";
            temp = temp->next;

            if(temp != NULL)
            {
                cout<<" -> ";
            }
        }
        cout<<"\n";
    }
}

int main()
{
    int g_node, n, s, d, w, source = 1;
    dict<int, struct node*> v;
    
    cin>>g_node;    // Final destination
    cin>>n;         // Number of edges in graph

    for(int i=1;i<g_node;i++)
    {
        v[i] = NULL;
    }

    for(int i=0;i<n;i++)
    {
        cin>>s>>d>>w;
        v[s] = new node(d, w, v[s]);
    }

    // Printing Graph
    print_graph<int, struct node*>(v);

    // Finding Shortest Path
    pair<vector<int>, vector<int>> ans = djikstra_algorithm(v, source, g_node);

    cout<<"\nResult:\n";
    for(int i=0;i<ans.first.size();i++)
    {
        cout<<"Node pair: ("<<ans.second[i]<<", "<<i+1<<") : Distance = "<<ans.first[i]<<"\n";
    }
    return 0;
}
