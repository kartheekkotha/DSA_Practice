/**
 * 1. Sujith 2110110400
 * 2. Kartheek 2110110292
 * 3. Chekuri 2110110174
 */
#include<iostream>
#include<string>
#include<algorithm>
#include<vector>

using namespace std;

/**
 * tuples is a struct which stores the index, word and letter
 * index is the index of the word
 * word is the index of the letter in the word or like a pointer to the word
 * letter is the letter
*/
typedef struct tuples
{
    int index;
    int word;
    char letter;
} tuples;

/**
 * sort_by_letter() sorts the vector of tuples by individual characters
 * @param v is the vector of tuples
 * @return void
 *
 * steps:
 * 1. We first segregate the tuples by letter into different buckets according to the letter
 * 2. Then we clear the vector of tuples
 * 3. Then we push the tuples back into the vector in the order of letters
 *    i.e. first all the tuples with letter 'a', then all the tuples with letter 'b' and so on
 *    this makes the vector sorted by letter
 *
 */
void sort_by_letter(vector<tuples> &v)
{
    vector<vector<tuples>> m(26);

    for (int i = 0; i < v.size(); i++)
    {
        m[v[i].letter - 'a'].push_back(v[i]);
    }

    v.clear();

    for (int i = 0; i < 26; i++)
    {
        for (int j = 0; j < m[i].size(); j++)
        {
            v.push_back(m[i][j]);
        }
    }

    return;

    /**
     * Complexity Analysis:
     * 
     * 1. First `for` loop runs for v.size() times i.e. |∑| which is number of tuples 
     *    or number of total characters in all the words
     * 2. Second `for` loop runs for 26 times which is constant
     *    then the inner `for` loop runs for m[i].size() times which is the number of tuples
     * 
     * Overall complexity is O(|∑| + 26 * |∑|) which is O(|∑|)
     * 
    */

}

/**
 * sort_by_index() sorts the vector of tuples by index
 * @param v is the vector of tuples
 * @param len is the length of the longest word
 * @return void
 *
 * steps:
 * 1. We first segregate the tuples by index into different buckets
 * 2. Then we clear the vector of tuples
 * 3. Then we push the tuples back into the vector in the order of indexes
 *    i.e. first all the tuples with index 0, then all the tuples with index 1 and so on
 *    this makes the vector sorted by index
 *
 */
void sort_by_index(vector<tuples> &v, int len)
{
    vector<vector<tuples>> m(len);

    for (int i = 0; i < v.size(); i++)
    {
        m[v[i].index].push_back(v[i]);
    }

    v.clear();

    for (int i = 0; i < len; i++)
    {
        for (int j = 0; j < m[i].size(); j++)
        {
            v.push_back(m[i][j]);
        }
    }

    return;

    /**
     * Complexity Analysis:
     * 
     * 1. First `for` loop runs for v.size() times i.e. |∑| which is number of tuples
     * 2. Second `for` loop runs for len times which is the length of the longest word
     *    then the inner `for` loop runs for m[i].size() times which is the number of tuples
     *    with index i
     * 
     * Overall complexity is O(|∑| + len * |∑|) which is O(|∑|)
    */

}

/**
 * arrange_words_by_length() arranges the words in the vector by length of the word
 * @param max_len is the length of the longest word
 * @param words is the vector of words
 * @return void
 *
 * steps:
 * 1. We first segregate the words by length into different buckets bounded by max_len
 * 2. Then we clear the vector of words
 * 3. Then we push the words back into the vector in the order of length
 *    i.e. first all the words with length 1, then all the words with length 2 and so on
 *    this makes the vector sorted by length
 *
 */
void arrange_words_by_length(int max_len, vector<string> &words)
{
    vector<vector<string>> m(max_len);

    for (int i = 0; i < words.size(); i++)
    {
        m[words[i].length() - 1].push_back(words[i]);
    }

    words.clear();

    for (int i = 0; i < max_len; i++)
    {
        for (int j = 0; j < m[i].size(); j++)
        {
            words.push_back(m[i][j]);
        }
    }

    return;

    /**
     * Complexity Analysis:
     * 
     * 1. First `for` loop runs for words.size() times i.e. n which is number of words
     * 2. Second `for` loop runs for max_len times which is the length of the longest word
     *    then the inner `for` loop runs for m[i].size() times which is the number of words
     *    with length i
     * 
     * Overall complexity is O(n + max_len * n) which is O(n)
     * 
    */

}

int main()
{

    /**
     * n is the number of words
     * len is the length of the longest word
     * v is the vector of tuples which stores the index, word and letter
     * words is the vector of words
     * 
    */
    int n, len = 0;
    cout << "Enter the number of words: ";
    cin >> n;

    vector<tuples> v;
    vector<string> words;

    // take input and find the length of the longest word
    for (int i = 0; i < n; i++)
    {
        string s;
        cin >> s;
        words.push_back(s);
        if (len < s.length())
        {
            len = s.length();
        }
    }

    // sort the vector of tuples by length
    arrange_words_by_length(len, words);

    // create a vector of tuples
    for (int i = 0; i < words.size(); i++)
    {
        for (int j = 0; j < words[i].length(); j++)
        {
            tuples t;
            t.index = j;
            t.word = i;
            t.letter = words[i][j];
            v.push_back(t);
        }
    }

    cout << "Tuples before any sorting: \n";
    for (int i = 0; i < v.size(); i++)
    {
        cout << v[i].index << " " << v[i].letter << " " << words[v[i].word] << endl;
    }

    // sort the vector of tuples by letter
    sort_by_letter(v);
    cout << "Tuples after sorting the characters: \n";
    for (int i = 0; i < v.size(); i++)
    {
        cout << v[i].index << " " << v[i].letter << " " << words[v[i].word] << endl;
    }

    // sort the vector of tuples by index
    sort_by_index(v, len);
    cout << "Tuples after sorting the indexes: \n";
    for (int i = 0; i < v.size(); i++)
    {
        cout << v[i].index << " " << v[i].letter << " " << words[v[i].word] << endl;
    }

    cout << "The sorted order is: \n";
    for (int i = 0; i < n; i++)
    {
        cout << words[v[i].word] << "\n";
    }

    return 0;

    /**
     * Complexity Analysis:
     * 
     * 1. sort_by_letter() runs in O(|∑|) time
     * 2. sort_by_index() runs in O(|∑|) time
     * 3. arrange_words_by_length() runs in O(n) time
     * 
     * Overall complexity is O(|∑| + |∑| + n) which is O(|∑| + n)
    */
}
