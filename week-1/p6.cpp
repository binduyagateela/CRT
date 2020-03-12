#include<iostream>
using namespace std;
int main()
{
    int n,a[100],x1=0,x2=0,x3=0,x4=0;
    cin>>n;
    for(int i=0;i<n;i++)
    {
        cin>>a[i];
    }
    for(int i=0;i<n;i++)
    {
        x1=x1+(a[i]%2);
        a[i]=a[i]/2;
        x2=x2+(a[i]%2);
        a[i]=a[i]/2;
        x3=x3+(a[i]%2);
        a[i]=a[i]/2;
        x4=x4+(a[i]%2);
    }
    x1=x1%3;
    x2=x2%3;
    x3=x3%3;
    x4=x4%3;
    cout<<(x1+(x2*2)+(x3*4)+(x4*8));

}
