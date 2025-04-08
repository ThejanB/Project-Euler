    # formula of area of a triangle = | (x1(y2 – y3) + x2(y3 – y1) + x3(y1-y2))/2 |
    # if area(ABC) = area(OBC)+area(AOC)+area(ABO) , O lies inside the triangle

def is_o_inside(x1,y1,x2,y2,x3,y3):
    total_area = abs( (x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2))/2 )
    area1 = abs( (x2*y3-x3*y2)/2 )
    area2 = abs( (x3*y1-x1*y3)/2 )
    area3 = abs( (x1*y2-x2*y1)/2 )    
    if total_area == area1+area2+area3:
        return True
    return False

file = open('102 Project Euler.Txt','r')
triangles = file.read()
triangles = triangles.split('\n')

triangle_list = []
for x in triangles:
    y = x.split(',')
    triangle_list.append(y)

count = 0
for i in triangle_list:
    if is_o_inside(int(i[0]),int(i[1]),int(i[2]),int(i[3]),int(i[4]),int(i[5])) == 1:
        count += 1    
print(count)


