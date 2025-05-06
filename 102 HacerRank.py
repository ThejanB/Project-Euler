# formula of area of a triangle =  | (x1(y2 – y3) + x2(y3 – y1) + x3(y1-y2))/2 |
# method 1 ->  if area(ABC) = area(OBC)+area(AOC)+area(ABO) , O lies inside the triangle
# method 2 ->  if these all areas are +ve or -ve ,  O lies inside the traingle

def is_o_inside(x1,y1,x2,y2,x3,y3):
    area1 = (x2*y3-x3*y2)/2
    area2 = (x3*y1-x1*y3)/2
    area3 = (x1*y2-x2*y1)/2    
    if (area1>=0 and area2>=0 and area3>=0) or (area1<=0 and area2<=0 and area3<=0):
        return True
    return False

triangle_list = []
for _ in range(int(input())):
    triangle_list.append(input().split())

count = 0
for i in triangle_list:
    if is_o_inside(int(i[0]),int(i[1]),int(i[2]),int(i[3]),int(i[4]),int(i[5])) == 1:
        count += 1    
print(count)
