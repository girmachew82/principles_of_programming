n = 10
match n:
    case  1:
        print("Positive")
    case -1:
        print("Negative")
    case _:
        print(0)


day = "Saturday"


match day:
	case "Monday":
		print(f" The day to day is {day}")
	case "Tuesday":
		print(f" The day to day is {day}")
	case "Wednesday":
		print(f" The day to day is {day}")
	case "Thursday":
		print(f" The day to day is {day}")
	case "Friday":
		print(f" The day to day is {day}")
	case "Saturday":
		print(f" The day to day is {day}")
	case "Sunday":
		print(f" The day to day is {day}")
	case _:
		print("Wrong input")
       



match day:
	case "Monday":
		print(f" The day to day is {day}")
	case "Tuesday":
		print(f" The day to day is {day}")
	case "Wednesday":
		print(f" The day to day is {day}")
	case "Thursday":
		print(f" The day to day is {day}")
	case "Friday":
		print(f" The day to day is {day}")
	case "Sunday" | "Saturday":
		print(f" Weekend day {day}")
	case _:
		print("Wrong input")
 
y = True
match y:
    case y > 0 | y < 0:
        print(f'{y} is positive or negative')
    case y == 0:
        print(f'{y} is zero')