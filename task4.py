if __name__ == "__main__":
	# take inputs
	batted = int(input("number of times batted\n>>"))
	not_out = int(input("number of times not out\n>>"))
	runs = int(input("runs scored\n>>"))

	# calculate and print the batting average
	batting_average = runs / (batted - not_out)
	print("your batting average is ", batting_average)