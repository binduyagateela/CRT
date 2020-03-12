#include<iostream>
using namespace std;
int main()
{
    while(1){
    int n,a[100],c=1,bit=1;
    cin>>n;
    a[0]=0;
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
    for(int i=0;i<=n;i++)
    {
        cout<<a[i]<<" ";
    }
    cout<<"\n";
    }
}

