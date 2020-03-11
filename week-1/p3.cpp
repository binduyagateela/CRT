
#include<iostream>
using namespace std;
int main()
{
    int n,a[100];
    cin>>n;
    for(int i=0;i<n;i++)
    {
        cin>>a[i];
    }
   int b,c, m=0;
    for(int i=0;i<n-1;i++)
    {
        for(int j=i+1;j<n;j++)
        {

            if((a[i]^a[j])>m){
                m=(a[i]^a[j]);
                b=i;c=j;}
        }
    }
    cout<<a[b]<<"^"<<a[c]<<"="<<m;
}
