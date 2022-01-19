// Online C++ compiler to run C++ program online
#include <iostream>

int main() {
    
    int ar[]={4,2,0,3,2,5};
    int max, i, count=0, sum=0;
    max = ar[0];
    int n = sizeof(ar)/sizeof(ar[0]);
    for(i=1;i<n;i++)
    {
        if(ar[i]<max)
        count=count + (max-ar[i]);
        else
        {
       max=ar[i];
       sum+=count;
       count=0;
        } 
    }
    if(i==n)
    {
    count=0;
    i=n-1;
    while(ar[i]<max)
    {
        if(ar[i]>ar[i-1])
        count+=(ar[i]-ar[i-1]);
        
      i--;  
    } 
    sum=sum+count;
    } 
    
    std::cout<<sum;

    return 0;
}