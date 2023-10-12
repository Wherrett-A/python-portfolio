if __name__ == "__main__":
	students = int(input("enter the number of students: "))
	group_size = int(input("enter the desired group size: "))

	full_groups = students // group_size
	remainder = students % group_size

	print(f"you will have {full_groups} groups and {remainder} people left over")