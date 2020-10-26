// Link: https://leetcode.com/problems/search-suggestions-system/

/*
Not my Solution

Explanation:
Link: https://leetcode.com/problems/search-suggestions-system/discuss/496222/Easy-to-understand-Java-solution-beat-95

At first we sort the products lexicographically, then we try to find:
if we have to inseart the prefix of searchWord in products, where should we put?
For example,

products = ["mobile","mouse","moneypot","monitor","mousepad"],
searchWord = "mouse"
sortedProducts=["mobile","moneypot","monitor","mouse","mousepad"]
then put the prefix into sortedProducts
put "m", sortedProducts=["m","mobile","moneypot","monitor","mouse","mousepad"]
put "mo" , sortedProducts=["mo","mobile","moneypot","monitor","mouse","mousepad"]
put"mou", sortedProducts=["mobile","moneypot","monitor","mou","mouse","mousepad"]
put"mous", sortedProducts=["mobile","moneypot","monitor","mous","mouse","mousepad"]
put"mouse", sortedProducts=["mobile","moneypot","monitor","mouse","mouse","mousepad"]
so the [insertion point, insertion point+2] should be the answer. Note that we also need to check if each potential answer starts with the prefix
*/

class Solution
{
    public List<List<String>> suggestedProducts(String[] products, String searchWord)
    {
        List<List<String>> result = new ArrayList();
        Arrays.sort(products);
        for(int i = 1; i <= searchWord.length(); i++)
        {
            String prefix = searchWord.substring(0, i);
            int pos = Arrays.binarySearch(products, prefix);
            if(pos < 0) pos = -pos-1;
            List<String> tmp = new ArrayList();
            
            for(int j = pos; j < pos+3 && j < products.length; j++)
            {
                if(!products[j].startsWith(prefix)) break;
                tmp.add(products[j]);
            }
            
            result.add(tmp);
        }
        return result;
    }
}