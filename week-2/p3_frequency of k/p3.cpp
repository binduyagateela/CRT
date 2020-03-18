# include <bits/stdc++.h>
#include<iostream>
using namespace std;
int count(int arr[], int x, int n)
{
   int *low = lower_bound(arr, arr+n, x);
   if (low == (arr + n) || *low != x)
   {
        return 0;
   }
   int *high = upper_bound(low, arr+n, x);
   return high - low;
}
int main()
{
  while(1){
  int n;
  cin>>n;
  int a[n];
  for(int i=0;i<n;i++)
  cin>>a[i];
  sort(a,a+n);
  int k;
  cin>>k;
  int res=count(a,k,n);
  cout<<res;
  cout<<"\n";
    }
}
