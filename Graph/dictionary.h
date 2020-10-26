#ifndef __DICTIONARY__H__
#define __DICTIONARY__H__

#include <unordered_map>
#include <vector>

template<class T, class U>  class dict  
{ 
    private: 
        std::unordered_map<T, U> m;                   // Dictionary
        typename std::unordered_map<T, U>::const_iterator it;  // Iterator

    public:
        dict()
        {
            it = m.end();
        }

        bool exists(T key)          // Search for elements in the dictionary
        {
            it = m.find(key);
            return it!=m.end();
        }

        U& operator[](const T &key) // Inserts value in the dictionary
        {
            return m[key];
        }

        void erase(const T &key)    // Erases particular element in the dictionary
        {
            m.erase(key);
        }

        std::vector<T> keys()       // Returns vector of all the keys of the dictionary
        {
            std::vector<T> k;

            for(it = m.begin(); it != m.end(); it++)
            {
                k.push_back(it->first);
            }
            return k;
        }

        bool empty()                // Checks whether Ditionary is empty or not
        {
            return m.empty();
        }

        unsigned int size()         // Returns size of Dictionary
        {
            return m.size();
        }

        std::unordered_map<T, U>& orig_map()  // Returns reference to inherent Map
        {
            return m;
        }
};
#endif // __DICTIONARY__H__ 

// Some helpful links:
// 1). https://stackoverflow.com/questions/5346890/what-is-the-difference-between-const-iterator-and-iterator
// 2). https://stackoverflow.com/questions/11275444/c-template-typename-iterator