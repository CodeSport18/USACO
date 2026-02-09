# https://usaco.org/index.php?page=viewproblem2&cpid=663

file = open('square.in','r')

bottom_left_corner = [float('inf'),float('inf')]
top_right_corner = [0,0]

for a in file:
    the_input = list(map(int,a.strip().split()))
    bottom_left_corner[0] = min(bottom_left_corner[0],the_input[0])
    bottom_left_corner[1] = min(bottom_left_corner[1],the_input[1])
    top_right_corner[0] = max(top_right_corner[0],the_input[2])
    top_right_corner[1] = max(top_right_corner[1],the_input[3])

file.close()

if (top_right_corner[0]-bottom_left_corner[0]) >= (top_right_corner[1]-bottom_left_corner[1]):
    the_area = (top_right_corner[0]-bottom_left_corner[0])*(top_right_corner[0]-bottom_left_corner[0])

else:
    the_area = (top_right_corner[1]-bottom_left_corner[1])*(top_right_corner[1]-bottom_left_corner[1])

file = open('square.out','w')
file.write(str(the_area))
file.close()