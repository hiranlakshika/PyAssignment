from assignment_5 import Assignment5
from assignment_6 import Assignment6


def main():
    print('Enter the assignment number')
    assignment_number = int(input())
    if assignment_number == 5:
        as5 = Assignment5()
        as5.draw(True, 35)
    elif assignment_number == 6:
        as6 = Assignment6()
        as6.draw()
    else:
        print('Assignment ' + str(assignment_number) + ' is not available')


if __name__ == "__main__":
    main()
