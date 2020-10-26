// Similar question: https://leetcode.com/problems/matrix-block-sum/
// Reference: https://www.techiedelight.com/calculate-sum-elements-sub-matrix-constant-time/

// Approach: Using Dynamic Programming (Tabulation Method) to store sum of all elements in a rectangle/square in its bottom-right corner.
// It is depicted in "preprocess" function below.

#include <iostream>
#include <vector>

using namespace std;

int min(int a, int b)
{
    return a>b?b:a;
}

int max(int a, int b)
{
    return a>b?a:b;
}

void preprocess(vector<vector<int>>& matrix)
{
    int n = matrix.size(), m = matrix[0].size();

    for(int i=0;i<n;i++)
        for(int j=0;j<m;j++)
        {
            if(i>0 && j>0)
            {
                matrix[i][j] = matrix[i][j] + matrix[i-1][j] + matrix[i][j-1] - matrix[i-1][j-1];
            }
            else if(i>0)
            {
                matrix[i][j] = matrix[i][j] + matrix[i-1][j];
            }
            else if(j>0)
            {
                matrix[i][j] = matrix[i][j] + matrix[i][j-1];
            }
        }
}

int find_sum(vector<int> coord, vector<vector<int>>& matrix)
{
    // Input vector format: {x1, y1, x2, y2}
    // (x1, y1) -> Top Left Pair, (x2, y2) -> Botttom Right Pair
    // x -> Columns (Horizontal), y -> Rows (Vertical)

    int x1 = coord[1], y1 = coord[0], x2 = coord[3], y2 = coord[2];

    if(x1<0)
    {
        return 0;
    }

    if(x1 > 0 && y1 > 0)
    {
        // cout<<"\n"<<x1<<" "<<y1<<" "<<x2<<" "<<y2<<"\n";
        // cout<<matrix[y2][x2]<<"\n";
        // cout<<matrix[y2][x1-1]<<"\n";
        // cout<<matrix[y1-1][x2]<<"\n";
        // cout<<matrix[y1-1][x1-1]<<"\n";
        
        return matrix[y2][x2] - matrix[y2][x1-1] - matrix[y1-1][x2] + matrix[y1-1][x1-1];
    }
    else if(x1>0)
    {
        return matrix[y2][x2] - matrix[y2][x1-1];
    }
    else if(y1>0)
    {
        return matrix[y2][x2] - matrix[y1-1][x2];
    }
    else
    {
        return matrix[y2][x2];
    }
}

// Finding Intersection rectangle of two rectangles
vector<int> find_intersection(vector<int> coord1, vector<int> coord2)
{
    // Input and Output vector format: {x1, y1, x2, y2}
    // (x1, y1) -> Top Left Pair, (x2, y2) -> Bottom Right Pair

    int x1c1 = coord1[1], y1c1 = coord1[0], x2c1 = coord1[3], y2c1 = coord1[2];
    int x1c2 = coord2[1], y1c2 = coord2[0], x2c2 = coord2[3], y2c2 = coord2[2];

    if(x2c1<x1c2 || y2c1<y1c2 || x2c2<x1c1 || y2c2<y1c1)
    {
        return vector<int>{-1, -1, -1, -1};
    }
    else
    {
        int x1 = max(x1c1, x1c2);
        int y1 = max(y1c1, y1c2);
        int x2 = min(x2c1, x2c2);
        int y2 = min(y2c1, y2c2);
        return vector<int>{y1, x1, y2, x2};
    }
}

void display(string message, vector<vector<int>>& matrix)
{
    int n = matrix.size(), m = matrix[0].size();

    cout<<"\n"<<message<<":\n";
    for(int i=0;i<n;i++)
    {
        cout<<matrix[i][0];
        for(int j=1;j<m;j++)
        {
            cout<<", "<<matrix[i][j];
        }
        cout<<"\n";
    }
}

float jaccard_rank(vector<int>& sq1, vector<int>& sq2, vector<vector<int>>& matrix)
{
    int ar1, ar2, ar3;
    vector<int> inter;

    preprocess(matrix);
    inter = find_intersection(sq1, sq2);

    ar1 = find_sum(sq1, matrix);
    ar2 = find_sum(sq2, matrix);
    ar3 = find_sum(inter, matrix);    // Intersection area

    // cout<<ar1<<" "<<ar2<<" "<<ar3;

    return (float)ar3/(float)(ar1 + ar2 - ar3);
}

int main()
{
    int n, m, queries, temp;
    vector<vector<int>> matrix;

    vector<int> sq1({-1, -1, -1, -1});  // Square 1
    vector<int> sq2({-1, -1, -1, -1});  // Square 2

    cin>>n>>m>>queries;

    for(int i=0;i<n;i++)
    {
        matrix.push_back(vector<int>());
    }

    for(int i=0;i<n;i++)
        for(int j=0;j<m;j++)
        {
            cin>>temp;
            matrix[i].push_back(temp);
        }

    for(int i=0;i<queries;i++)
    {
        // sq1
        for(int j=0;j<4;j++)
        {
            cin>>sq1[j];
        }

        // sq2
        for(int j=0;j<4;j++)
        {
            cin>>sq2[j];
        }

        // Jaccard Score Calculation
        cout<<"Query "<<i+1<<" -> Jaccard Score: "<<jaccard_rank(sq1, sq2, matrix)<<"\n";
    }

    /*
    display("Input Matrix", matrix);
    preprocess(matrix);
    display("Processed Matrix", matrix);

    cout<<"\nSum: "<<find_sum(vector<int>{0, 1, 1, 2}, matrix)<<"\n";

    vector<int> ans = find_intersection(vector<int>{1, 0, 0, 1}, vector<int>{1, 0, 0, 1});
    cout<<"\nIntersection: "<<ans[0]<<", "<<ans[1]<<", "<<ans[2]<<", "<<ans[3]<<"\n";
    */
}