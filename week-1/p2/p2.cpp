#include<iostream>
using namespace std;
int main()
{
    while(1){
    int a,b,c,cu=0,m,n,o;
    cin>>a>>b>>c;
    while(a!=0 || b!=0 || c!=0)
    {
        m=a&1;a=a>>1;
        n=b&1;b=b>>1;
        o=c&1;c=c>>1;
        if((m|n)==o)
            continue;
        else if(((!m)|n)==o)
            cu+=1;
        else
            cu+=2;
    }
    cout<<cu;
    cout<<"\n";
    }
}
