"""CSC 161 Lab: Functions

Lihang Liu
Lab Section TR 2:00-3:15pm
Spring 2022
"""


def to_numbers(str_list):
    for i in range(len(str_list)):
        str_list[i] = float(str_list[i])


def square_each(nums):
    for a in range(len(nums)):
        nums[a] = nums[a] ** 2


def sum_list(nums):
    a = sum(nums)
    return a


def main():
    print("This program computes the sum of the"
          "squares of numbers read from a file.")
    all_list = input("Please enter the file name: ")
    open_file = open(all_list, "r")

    num_str = open_file.readline()
    num_list = num_str.split(",")

    to_numbers(num_list)
    square_each(num_list)
    three_list = sum_list(num_list)
    print("The sum of the squares of the numbers in the file is", three_list)


if __name__ == "__main__":
    main()
