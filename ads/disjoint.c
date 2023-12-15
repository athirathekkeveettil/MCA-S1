#include<stdio.h>

int setA[10],setB[10],setC[10],i,j,m,n;

void create()
{
  printf("Enter the size of setA:");
  scanf("%d",&m);
  printf("Enter setA\n");
  for(i=1;i<=m;i++)
      scanf("%d",&setA[i]);
      
  printf("Enter the size of setB:");
  scanf("%d",&n);
  printf("Enter setB\n");
  for(i=1;i<=n;i++)
     scanf("%d",&setB[i]);
     
     printf("\nSET A:{");
    for(i=1;i<=m;i++)
      printf("%d",setA[i]);
  printf("}\n");
     printf("\nSET B:{");
    for(i=1;i<=n;i++)
      printf("%d",setB[i]);
  printf("}\n");
   
}

void uniondis()
{
	int j;
		for(i=1;i<=m;i++)
			setC[i]=setA[i];
		j=m+1;
		for(i=1;i<=n;i++)
		{
			setC[i]=setB[i];
			j++;
		}
		printf("\nUNION:{");
		for(i=1;i<=m+n;i++)
			printf("%d,",setC[i]);
		printf("}\n");
}

void find()
{
	int item,f=-1;
	printf("enter the element:");
	scanf("%d",&item);
	for(i=1;i<=m;i++)
	{
		if(item==setA[i])
		{
			printf("\nParent is:%d",setA[1]);
			f=1;
			break;
		}
	}
	for(i=1;i<=n;i++)
	{
		if(item==setB[i])
		{
			printf("\nPARENT IS:%d",setB[1]);
			f=1;
			break;
		}
	}
	if(f<0)
		printf("\nthere is no such element in the set");
}

int main()
{
 int choice;
 do
 {
  printf("\n--DISJOINT SET OPERATIONS--\n");
  printf("\n1.CREATION\n");
  printf("\n2.UNION\n");
  printf("\n3.FIND\n");
  printf("\n4.EXIT\n");
  printf("Enter Your Choice:");
  scanf("%d",&choice);
  switch(choice)
  {
   case 1:create();
          break;
   case 2:uniondis();
          break;
   case 3:find();
          break;
   case 4:printf("\nEXIT\n");
          return 0;
   default:printf("\nInvalid choice!!\n");
  }
 }
 while(choice!=0);
}
