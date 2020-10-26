// Link: https://leetcode.com/problems/rectangle-area/

class Solution
{
    private:
        int find_intersection(vector<int> coord1, vector<int> coord2)
        {
            // Input and Output vector format: {x1, y1, x2, y2}
            // (x1, y1) -> Bottom Left Pair, (x2, y2) -> Top Right Pair

            int x1c1 = coord1[0], y1c1 = coord1[1], x2c1 = coord1[2], y2c1 = coord1[3];
            int x1c2 = coord2[0], y1c2 = coord2[1], x2c2 = coord2[2], y2c2 = coord2[3];

            if(x2c1<=x1c2 || y1c1>=y2c2 || x2c2<=x1c1 || y1c2>=y2c1)
            {
                return 0;
            }
            else
            {
                int x1 = max(x1c1, x1c2);
                int y1 = max(y1c1, y1c2);
                int x2 = min(x2c1, x2c2);
                int y2 = min(y2c1, y2c2);
                return (x2-x1)*(y2-y1);
            }
}
    public:
        int computeArea(int A, int B, int C, int D, int E, int F, int G, int H)
        {
            int intersect_area = find_intersection(vector<int>{A, B, C, D}, vector<int>{E, F, G, H});
            
            return (long)(C-A)*(D-B) + (long)(G-E)*(H-F) - intersect_area;
        }
};