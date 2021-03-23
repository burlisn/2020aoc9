def main() -> None:
    #------------- VARIABLES ----------
    number_list: list[str] = []
    wrong_number: int = 0
    encryption_weakness: int =0
    #----------------------------------

    #open input text file and get input
    with open("input.txt", "r") as fin:
        input_text=fin.read()

    #obtain list of numbers
    number_list = input_text.split('\n')

    #find the error number (part 1)
    wrong_number = find_wrong_number(number_list)

    #find the encryption weakness (part 2)
    encryption_weakness = find_encryption_weakness(number_list, wrong_number)

    #print results
    print(wrong_number)
    print(encryption_weakness)

############### FUNCTION DEFINITIONS ########################

#Description: finds a number that isn't a sum of the last 25, if any
#Returns: The wrong number
def find_wrong_number(number_list: list[str]) -> int:
    for i in range(len(number_list)):
        if i < len(number_list)-25:
            if False == check_if_sum(number_list[i:i+25], int(number_list[i+25])):
                return int(number_list[i+25])
        elif i >= len(number_list)-25:
            return 0

#Description: checks if a number is the sum of 2 numbers in the last 25 numbers
#Returns: if it is (true), if not (false)
def check_if_sum(number_slice: list[str], test_number: int) -> bool:
    for i in number_slice:
        for j in number_slice:
            if int(i)+int(j) == test_number and int(i) != int(j):
                return True

    return False

#Description: finds the answer to part 2 (they call it the 'encryption weakness')
#Returns: sum of the smallest and largest number in the correct range
def find_encryption_weakness(number_list: list[str], wrong_number: int) -> int:
    range: list[str] = []

    range = find_range(number_list, wrong_number)

    return (smallest_and_largest_sum(range))

#Description: finds the range that adds up to the number found in part 1
#Returns: the correct range of numbers
def find_range(number_list: list[str], wrong_number: int) -> list[str]:
    s_i: int = 0 #starting index
    c_i: int = 0 #current index

    while False == is_range_valid(number_list[s_i:c_i], wrong_number)[0]:
        if is_range_valid(number_list[s_i:c_i], wrong_number)[1] > wrong_number:
            s_i += 1
            c_i = s_i
        elif c_i >= len(number_list):
            print("Current index is going over the size of the number list!!!")
        c_i += 1

    return number_list[s_i:c_i]

        

#Description: determines if the number range adds up to number found from part 1
#Returns: boolean value that determines if it is, int that is the sum of the range
def is_range_valid(range: list[str], wrong_number: int) -> tuple[bool, int]:
    running_sum: int =0
    
    for i in range:
        running_sum += int(i)

    if running_sum == wrong_number:
        return True, running_sum
    else:
        return False, running_sum

#Description: returns the smallest and largest sum
#Returns: the sum of the smallest and largest number in a range
def smallest_and_largest_sum(range: list[str]) -> int:
    smallest: int = int(range[0])
    largest: int = int(range[0])

    for number in range:
        if int(number) > largest:
            largest = int(number)
        elif int(number) < smallest:
            smallest = int(number)
    
    return int(smallest) + int(largest)
  
if __name__ == "__main__":
    main()