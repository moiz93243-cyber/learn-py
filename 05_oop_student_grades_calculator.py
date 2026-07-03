class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks                 #ye ek constructer he        
        
        
    def get_avg(self):  
        
                                             #ye ek oject method he 
        
        sum=0
        for val in self.marks:
            sum+=val
            
            
        avg_marks=sum/len(self.marks)
        print(f"hi,{self.name},your avg marks are:{(avg_marks):.2f}")
            
            
s1=student("ali",[93,92,91])                      #ye object he
s1.get_avg()
s2=student("hamza",[93,42,91])
s2.get_avg()

