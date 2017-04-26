def mars_rover(upper_right_coordinates,rover_position,instructions):
	input1_new = upper_right_coordinates.split()
	corner_x = input1_new[0]
	corner_y = input1_new[1]
	rover_position_list = rover_position.split()
	x = int(rover_position_list[0])
	y = int(rover_position_list[1])
	if x <= corner_x and y <= corner_y:
		dirs = {'E,L': 'N',
				 'E,R': 'S',
				 'N,L': 'W',
				 'N,R': 'E',
				 'S,L': 'E',
				 'S,R': 'W',
				 'W,L': 'S',
				 'W,R': 'N'
			}
		new_dir = rover_position_list[2]
		instructions_list = list(instructions)
		for i in instructions_list:
			if i == 'M':
				if new_dir == 'N':
					y+=1
				elif new_dir == 'S':
					y-=1
				elif new_dir == 'W':
					x-=1
				elif new_dir == 'E':
					x+=1
				else:
					print "Wrong Direction"
			else:
				curr_dir = ','.join([new_dir,i])
				new_dir = dirs[curr_dir]
	else:
		print "Position out of grid."	
	return x,y, new_dir
if __name__ == '__main__':
	upper_right_coordinates = "5 5"
	rover_position = "3 3 E"
	instructions = "MMRMMRMRRM"
	print mars_rover(upper_right_coordinates,rover_position,instructions)
