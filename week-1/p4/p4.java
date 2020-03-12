import java.lang.*;
import java.util.*;
class fun
{
	public int one(int n)
	{
		int c=0;
		while(n!=0)
		{
			if(n%2==0)
					n=n/2;
			else
				if(Integer.bitCount(n+1)<Integer.bitCount(n-1))
						n=n+1;
				else
					n=n-1;
			c++;
		}
		return c-1;
	}

}
class p4
{

	public static void main(String[] args) 
	{
		int input[]=new int[10];
		int expctoutput[]=new int[10];
		int output[]=new int[10];
		input[0]=3;
		input[1]=4;
		input[2]=8;
		input[3]=16;
		input[4]=15;
		input[5]=1000;
		input[6]=100;
		input[7]=50;
		input[8]=75;
		input[9]=80;
		expctoutput[0]=2;
		expctoutput[1]=2;
		expctoutput[2]=3;
		expctoutput[3]=4;
		expctoutput[4]=5;
		expctoutput[5]=12;
		expctoutput[6]=8;
		expctoutput[7]=7;
		expctoutput[8]=9;
		expctoutput[9]=7;
		fun f=new fun();
		for(int i=0;i<10;i++){
			output[i]=f.one(input[i]);}	
		for(int i=0;i<10;i++)
		{
			if(output[i]==expctoutput[i])
				System.out.println(output[i]);
			else
				break;
		}

	}
}
