import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Scanner;
import java.util.Set;
import java.util.concurrent.ThreadLocalRandom;

class test{
	

public static void main (String []args)
{
//    long A[]={1,2,4,3};
//    long B[]= {1,2,3,4};
//    int Asize=A.length;
//    int Bsize=B.length;
    Scanner S=new Scanner(System.in);
    System.out.println("Enter size of first list");
    int Asize=S.nextInt();
    System.out.println("Enter size of second list");
    int Bsize=S.nextInt();
    long A[]=new long[Asize];
    long B[]=new long[Bsize];
    System.out.println("Enter elements of first list");
    int Max=60;
    int Min=-60;
    for(int i=0;i<Asize;i++)
    {
    	//A[i]=S.nextLong();
    	A[i]=(long)(Math.random() * ((Max - Min) + 1))+Min;
    	System.out.println(A[i] +" ");
    }
    System.out.println("Enter elements of second list");
    for(int i=0;i<Bsize;i++)
    {
    	//B[i]=S.nextLong();
    	B[i]=(long)(Math.random() * ((Max - Min) + 1))+Min;
    	System.out.println(B[i]+" ");
    }
    
    
    long table[][]=new long[Asize+1][Bsize+1];
    List<List<Long>> list =new ArrayList<List<Long>>();
     list=test.findLCS(A,B,table);
     test.findLICS(list,table[Asize][Bsize]);
    // LongestCommonIncreasingSubsequence.findLICS(list);
     
    
   
    
}

public static List<List<Long>> findLCS(long A[],long B[],long table[][])
{
    
    for(int i=0;i<=A.length;i++)
    {
       for(int j=0;j<=B.length;j++)
        {
            if(i==0||j==0)
                 table[i][j]=0;
            else if(B[j-1]==A[i-1])
            	table[i][j]=table[i-1][j-1]+1;
            else
            	table[i][j]=(table[i-1][j]>table[i][j-1])?table[i-1][j]:table[i][j-1];
        }
    }
    List<List<Long>> strlist=new ArrayList<List<Long>>();
    strlist=findLCSStrings(A,B,A.length,B.length,table);
//    for(int i=0;i<strlist.size();i++)
//    {
//    	System.out.println("The "+ i +" list");
//    	for(int j=0;j<strlist.get(i).size();j++)
//    	{
//    		System.out.print(strlist.get(i).get(j));
//    		System.out.println();
//    	}
//    }
    return strlist;
}    
public static List<List<Long>> findLCSStrings(long A[],long B[],int i,int j,long table[][])
{
	
	List<List<Long>> intlist=new ArrayList<List<Long>>();
	if(i==0 || j==0)
	{
		List<Long> templonglist=new ArrayList<Long>();
		intlist.add(templonglist);
		return intlist;
	}
	if(A[i-1]==B[j-1])
	{
		 intlist=findLCSStrings(A,B,i-1,j-1,table);
		 
		
		for(int k=0;k<intlist.size();k++)
		{
			intlist.get(k).add(A[i-1]);
		
		}
	}
	else
	{
		if(table[i-1][j]>=table[i][j-1])
		{
			intlist=findLCSStrings(A,B,i-1,j,table);
		}
		if(table[i][j-1]>=table[i-1][j])
		{
			 List<List<Long>> temp=findLCSStrings(A,B,i,j-1,table);
			for(int t=0;t<temp.size();t++)
			{
				intlist.add(temp.get(t));
			}
			Set<List<Long>> set=new HashSet<List<Long>>();
			for(int t=0;t<intlist.size();t++)
			{
				set.add(intlist.get(t));
			}
			intlist=new ArrayList<List<Long>>();
			for(List<Long> templist :set)
			{
				intlist.add(templist);
			}
		}
	}
	return intlist;
}
public static void findLICS(List<List<Long>> list,long val)
{
	
	if(list.isEmpty())
	{System.out.println("There is no common subsequence between the two lists");return;}
	else 
	{
		int flag=0;
		for(int i=0;i<list.size();i++)
		{
			if(list.get(i).size()>0)
				{flag=1;break;}
		}
		if(flag==0)
		{System.out.println("There is no common subsequence between the two lists");return;}
	}
	long max=Long.MIN_VALUE;
	long temp=0;
	for(int i=0;i<list.size();i++)
	{
		temp=test.findMax(list.get(i));
		if(temp>max)
			max=temp;
	}
	for(int k=0;k<list.size();k++)
	{
		printLICS(list.get(k),max);
	
	}
	

}
public static long findMax(List<Long>list)
{
	long[] arr=new long[list.size()];
	for(int i=0;i<arr.length;i++)
		arr[i]=1;
	
	for(int i=1;i<list.size();i++)
	{
		for(int j=0;j<i;j++)
		{
			if(list.get(i)>list.get(j) && ((arr[j]+1)>arr[i]))
			{
				arr[i]=arr[j]+1;
			}
		}
	}
	long max=0;
	if(arr.length>=1)
	 max=arr[0];
	int maxindex=0;
	for(int i=0;i<arr.length;i++)
	{
		if(arr[i]>max)
			{max=arr[i];maxindex=i;}
	}
	return max;
}
public static void printLICS(List<Long>list,long val)
{
	long[] arr=new long[list.size()];
	for(int i=0;i<arr.length;i++)
		arr[i]=1;
	
	for(int i=1;i<list.size();i++)
	{
		for(int j=0;j<i;j++)
		{
			if(list.get(i)>list.get(j) && ((arr[j]+1)>arr[i]))
			{
				arr[i]=arr[j]+1;
			}
		}
	}
	long max=0;
	if(arr.length>=1)
		 max=arr[0];
	int maxindex=0;
	for(int i=0;i<arr.length;i++)
	{
		if(arr[i]>max)
			{max=arr[i];maxindex=i;}
	}
	if(max!=val)
		return;
	long newarr[]=new long[(int)max];
	
	long min=list.get(maxindex);
	int minindex=maxindex;
	int k=newarr.length-1;
	
	newarr[k]=min;
	
	
	for(int i=maxindex-1;i>=0;i--)
	{
		if(min>list.get(i) && arr[i]+1==arr[minindex] && --k>=0)
		{
			min=list.get(i);
			minindex=i;
			newarr[k]=min;
		}
	}
	System.out.println("The length of longest increasing common subsequence is :"+ max);
	for(int i=0;i<newarr.length;i++)
		System.out.print(newarr[i]+" ");
	System.out.println();
}
}
