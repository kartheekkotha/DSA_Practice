#include<iostream>
#include<string>
#include<algorithm>
#include<vector>
#include<map>
using namespace std;

typedef struct tuples{
    int index;
    string word;
    char letter;
}tuples;

void sort_by_letter(vector<tuples> &v){
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

}

void sort_by_index(vector<tuples> &v, int len){
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
}

int main(){
    // input the strings of words and then insert into the tuples based on index of the letter and the charecter and the word related to it
    int n, len=0;
    // ask to enter the number of words through cout
    cout<<"Enter the number of words: ";
    cin>>n;
    vector<tuples> v;
    for (int i = 0; i < n; i++)
    {
        string s;
        cin>>s;
        tuples t;
        for (int j = 0; j < s.length(); j++)
        {
            t.index = j;
            t.word = s;
            t.letter = s[j];
            v.push_back(t);
        }
        if(len < s.length()){
            len = s.length();
        }
    }
    cout<<"Tuples before any sorting: \n";
    //print tuple vector
    for (int i = 0; i < v.size(); i++)
    {
        cout<<v[i].index<<" "<<v[i].letter<<" "<<v[i].word<<endl;
    }
    // sort the vector of tuples by letter
    sort_by_letter(v);
    cout<<"Tuples after sorting the charecters: \n";
    //print tuple vector
    for (int i = 0; i < v.size(); i++)
    {
        cout<<v[i].index<<" "<<v[i].letter<<" "<<v[i].word<<endl;
    }
    // sort the vector of tuples by index
    sort_by_index(v, len);
    cout<<"Tuples after sorting the indexes: \n";
    //print tuple vector
    for (int i = 0; i < v.size(); i++)
    {
        cout<<v[i].index<<" "<<v[i].letter<<" "<<v[i].word<<endl;
    }
    // print the sorted words
    cout<<"The sorted order is: \n";
    for (int i = 0; i < n; i++)
    {
        cout<<v[i].word<<"\n";
    }

}


