#include<iostream>
using namespace std;
void fun(int l,int h,int a[])
{
    l=l;
    h=h;
    int x=0;
    for(int j=l;j<h;j+=2)
        {
            x=x^(a[j]^a[j+1]);
            if(j==h)
            {
                x=x^a[j];
            }
    }
    cout<<x<<" ";
}
int main()
{
    int n,a[100],n1,q[100][2];
    cin>>n;
    for(int i=0;i<n;i++)
    {
        cin>>a[i];
    }
   cin>>n1;
    for(int i=0;i<n1;i++)
    {
        cin>>q[i][0];
        cin>>q[i][1];
    }
    for(int i=0;i<n1;i++)
    {
        fun(q[i][0],q[i][1],mi,a);
    }
}
