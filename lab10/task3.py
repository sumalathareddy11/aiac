class emp:
    def __init__(self,n,s): self.n,self.s=n,s
    def inc(self,p):self.s+=self.s*p/100
    def pr(self):print("emp:",self.n,"salary:",self.s) 
e=emp("sumalatha",10000);e.inc(10);e.pr()