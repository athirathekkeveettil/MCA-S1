#include<stdio.h>
int main()
{
  int n,item,i,mid,high=n-1,low=0,a[20],f=0;
  
  printf("Enter the size:");
  
  scanf("%d",&n);
  
  printf("Enter the elements\n");
  
  for(i=0;i<n;i++)
  
  scanf("%d",&a[i]);
  
  printf("Enter the element to search:");
  
  scanf("%d",&item);
  
  while(low<high)
  {
    mid=(low+high)/2; 
    
     if(item==a[mid])
     {
       printf("item found");
       
       return mid;
      }
     else if(item<a[mid])
     
        high=mid-1;
        
     else
     
        low=mid+1;
        
    }
    
    return 0;
  
}   
      

