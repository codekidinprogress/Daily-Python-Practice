nterms=int(input("how many terms:"))
n1=0
n2=1
count=2 #To keep a track
if nterms<=0:
    print("Please Enter postive Number!")
elif nterms==1:
    print("Fibonacci Series upto",nterms,":")
    print(n1)
else:
    print("Fibonaaci series upto",nterms,":")
    print(n1,",",n2,end=",")
    while count<nterms:
        nth=n1+n2
        print(nth,end=",")
        n1=n2
        n2=nth
        count+=1