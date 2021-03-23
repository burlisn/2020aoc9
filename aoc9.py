def main() -> None:
    #------------- VARIABLES ----------
    number_list: list[str] = []
    wrong_number: int = 0
    #----------------------------------

    #open input text file and get input
    with open("input.txt", "r") as fin:
        input_text=fin.read()

    #obtain list of numbers
    number_list = input_text.split('\n')

    #find the error number
    wrong_number = find_wrong_number(number_list)

    #pring results
    print(wrong_number)

    #testing area


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
    

if __name__ == "__main__":
    main()