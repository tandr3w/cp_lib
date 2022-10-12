#include<iostream>
#include<vector>
#include<map>
#include<set>
using namespace std;

int main()
{
    vector<int> v;
    v.push_back(3);
    v.push_back(5);
    cout << v[0] << endl << endl;
    // You can use v.begin() and v.end() for pointers to the start and end elements respectively
    // To do this with sets, use set<int>::iterator it = s.begin(); and set<int>::iterator it = s.end();


    set<int> s;
    s.insert(3);
    s.insert(5);
    s.insert(4);
    s.insert(5);
    s.erase(3);
    cout << s.count(5) << endl;
    cout << s.count(3) << endl;
    cout << s.count(4) << endl << endl; // Only returns 0 or 1

    map<string, int> m;
    m["key1"] = 4;
    m["key2"] = 7;
    cout << m["key1"];
}

// Other data structures (check documentation for implementation):
// Bitset: Only 1 or 0
// Deque: Slower vector but lets you pop elements at the front and back
// Stack: You can only add or remove the top
// Queue: You can only add at the back and remove from the front.
// Priority Queue: A queue where each element has a priority and the largest is at the back.

// Non-standard structures
// Indexed Set: Set but with index (sorted order)