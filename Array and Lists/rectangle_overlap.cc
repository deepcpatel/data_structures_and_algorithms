// Link: https://leetcode.com/problems/rectangle-overlap/

class Solution 
{
    public:
        bool isRectangleOverlap(vector<int>& coord1, vector<int>& coord2)
        {
            // Input and Output vector format: {x1, y1, x2, y2}
            int x1c1 = coord1[0], y1c1 = coord1[1], x2c1 = coord1[2], y2c1 = coord1[3];
            int x1c2 = coord2[0], y1c2 = coord2[1], x2c2 = coord2[2], y2c2 = coord2[3];

            if(x2c1<=x1c2 || y1c1>=y2c2 || x2c2<=x1c1 || y1c2>=y2c1)
            {
                return false;
            }
            else
            {
                return true;
            }   
        }
};