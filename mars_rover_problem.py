def mars_rover(upper_right_coordinates,rover_position,instructions):
	corner_x,corner_y = map(int,upper_right_coordinates.split())
	# x,y,new_dir = map(int, rover_position.split())
	x,y,new_dir = rover_position.split()
	x,y = int(x),int(y)
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
		if x in xrange(0,corner_x+1) and y in xrange(0,corner_y+1):
			return x,y, new_dir
		else:
			print "Moved out of grid"
	else:
		print "Position out of grid."	
if __name__ == '__main__':
	# Enter values with space in between them.
	upper_right_coordinates = raw_input("Enter Grid Size")
	while True:
		rover_position = raw_input("Enter rover's initial position")
		instructions = raw_input("Enter instructions")
		print mars_rover(upper_right_coordinates,rover_position,instructions)

