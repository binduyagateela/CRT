#include<iostream>
using namespace std;
int main()
{
    int n,a[100],c=1,bit=1;
    cin>>n;
    for(int i=1;i<=n;i++)
    {
        if(i==bit)
        {
            a[i]=1;
            bit<<=1;
            c=1;
        }
        else{
            a[i]=a[c]+1;c++;
        }
    }
    for(int i=1;i<=n;i++)
    {
        cout<<a[i]<<" ";
    }
}
