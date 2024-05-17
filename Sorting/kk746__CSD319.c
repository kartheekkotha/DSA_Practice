//Question 
// The first line contains single positive integer (1 ≤ 𝑛 ≤ 106
// ) — the number of integers.
// The second line contains positive integers z1, z2 … zn (1 ≤ zi ≤ 109
// ).
// Output:
// Print the longest possible length of the subsequence that is strictly increasing using dynamic programming


#include <stdio.h>


int max(int a, int b); // function Prototype of the max function
int longestSubSequence(int arr[], int n); // function Prototype of the longestSubSequence function

void main() {
    int n;
    // Inputting the size of the array
    scanf("%d", &n);
    int arr[n];
    // Inputting the elements of the array
    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }
    int res = longestSubSequence(arr, n);
    printf("%d\n", res);
}

// function declaration of the longestSubSequence function
// the dynamic programming recursive formula is 
// dp[i] = max(dp[i], dp[j] + 1) where j < i and arr[j] < arr[i]
// else dp[i] = 1
int longestSubSequence(int arr[], int n) {
    int dp[n];
    int maxLen = 1;
    for (int i = 0; i < n; i++) {
        dp[i] = 1;
        for (int j = 0; j < i; j++) {
            if (arr[j] < arr[i]) {
                dp[i] = max(dp[i], dp[j] + 1);
            }
        }
        maxLen = max(maxLen, dp[i]);
    }

    return maxLen;
}
// function definition of the max function
int max(int a, int b) {
    return a > b ? a : b;
}