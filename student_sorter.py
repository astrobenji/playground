# SciCoder Tast 1 - Finding the right students
# Created by Benjamin Metha
# Last updated: November 19 2018
#import pdb
# Functions used:

def getname(student):
	''' Returns the name of the associated student, formatted nicely'''
	return student[0] + " " + student[1]
	
def print_dict(dictionary):
	'''Prints a dictionary in an aesthetic way'''
	for key in dictionary.keys():
		if key == "":
			print("Students without a club:\n")
		else:
			print(key + ':\n')
		for value in dictionary[key]:
			print('\t'+value)

		print('\n')

## Read our data file.
filename = "Datafiles/student_data.txt"
file_reader = open(filename)
students = []
club_rolls = dict()

# Read all students. Save data in students. Save club data in club_rolls.

for line in file_reader:
	# Skip all lines that don't begin with a capital letter
	if ord(line[0]) < ord('A') or ord(line[0]) > ord('Z') :
		continue
	line.rstrip('\n')
	curr_student = line.split('|')
	# Skip all lines that are incomplete (not enough entries)
	if len(curr_student) < 5:
		continue
	students.append(curr_student)
	curr_clubs = curr_student[5].rstrip('\n')
	curr_clubs = curr_clubs.split(', ')
	for club in curr_clubs:
		if club not in club_rolls.keys():
			club_rolls[club] = [getname(curr_student)]
		else:
			club_rolls[club].append(getname(curr_student))

file_reader.close()
#pdb.set_trace()
## Part 1 - Find all students from Attleboro
students_from_Attleboro = [getname(x) for x in students if 'Attleboro' == x[2]]
print(students_from_Attleboro)
## Part 2 - Find all students supervised by Baker
students_of_Baker = [getname(x) for x in students if 'Baker' in x[3]]
print(students_of_Baker)
## Part 3 - Find a list of all students enrolled in each club.
#That's what our dict is
print_dict(club_rolls)
