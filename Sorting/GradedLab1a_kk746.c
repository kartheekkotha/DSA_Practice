//Name: Kartheek Kotha
//Roll Number: 2110110292
//Question 1
/*You have an array containing N integers in the range (-2^9, 2^9). 
  Implement quick sort to arrange contents of the array in increasing order. 
  You are required to show the array contents after completing each iterations.*/
/*
Sample Input
2
8
2 7 4 -30 5 3 0 1
6
10 7 4 -2 0 -10

Sample Output
-30 0 1 2 3 4 5 7
-10 -2 0 4 7 10
*/
#include<stdio.h>
#include<stdlib.h>

//Functional Argument fot the quick sort function and print function
void quickSort(int arr[] , int size , int start , int end);

//Main function 
int main() {
    int testCases = 0;
    printf("Sample Input\n" );
    scanf("%d", &testCases);
    FILE *fp = fopen("GradedLab1a_kk746_output.txt", "w");
    for(int i =0 ; i<testCases ; i++){
        int size = 0; 
        scanf("%d", &size);
        int arr[size];
        //create a file with writing mode
        for(int j = 0; j<size; j++){
            scanf("%d", &arr[j]);
        }
        quickSort(arr, size, 0, size-1);
        for(int j = 0; j<size; j++){
            fprintf(fp, "%d ", arr[j]);
        }
        fprintf(fp, "\n");
    }
    fclose(fp);
    printf("\nSample Output\n");
    //open file with reading mode
    FILE *fp1 = fopen("GradedLab1a_kk746_output.txt", "r");
    char ch;
    while((ch = fgetc(fp1)) != EOF){
        printf("%c", ch);
    }
    fclose(fp1);
    exit(0);
}

//Function for quickSort
void quickSort(int arr[] , int size , int start , int end){
    if(start < end){
        int pivot = arr[end];
        int i = start - 1;
        for(int j = start; j<end; j++){
            if(arr[j] <= pivot){
                i++;
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }
        int temp = arr[i+1];
        arr[i+1] = arr[end];
        arr[end] = temp;
        quickSort(arr, size, start, i);
        quickSort(arr, size, i+2, end);
    }
}
