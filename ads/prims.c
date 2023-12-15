#include<stdio.h>
#include<stdlib.h>
int main()
{
 int i,j,n,cost[10][10];
 printf("Enter the no. of nodes:");
 scanf("%d",&n);
 printf("enter the cost matrix:");
 for(i=1;i<=n;i++)
 {
  for(j=1;j<=n;j++)
  {
   scanf("%d",&cost[i][j]);
   if(cost[i][j]==0)
     cost[i][j]=999;
  }
 }
 prims(n,cost);
 return 0;
}

void prims(int n,int cost[10][10])
{
 int i,j,u,v,min,mincost=0,visited[10];
}
