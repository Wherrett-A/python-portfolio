if __name__ == "__main__":
	# takes number of students and desired group size as inputs
	students = int(input("enter the number of students: "))
	group_size = int(input("enter the desired group size: "))

	# uses floor division to find the number of whole groups
	full_groups = students // group_size
	# used modulus to find the numer of students left over
	remainder = students % group_size

	# prints the number results
	print(f"you will have {full_groups} groups and {remainder} people left over")