a,b,c,d,e,f = map(int, input().split())
x = int(((b*f)-(c*e))/((b*d)-(a*e)))
y = int(((c*d)-(a*f))/((b*d)-(a*e)))

print("%d %d" %(x,y))