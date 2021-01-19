#######################
# Basic Math          #
#######################

"""
여기서 간단한 수학을 하는 프로그램을 만들것입니다. 
"""


def get_greatest(number_list):
    """
    주어진 리스트에서 가장 큰 숫자를 반환함

        Parameters:
            number_list (list): integer로 값으로만 구성된 list
            ex - [10, 33, 22, 99, 33]

        Returns:
            greatest_number (int): parameter number_list 중 가장 큰 값

        Examples:
            >>> number_list = [39, 54, 32, 11, 99]
            >>> import basic_math as bm
            >>> bm.get_greatest(number_list)
            99
    """
    greatest_number = max(number_list)
    return greatest_number


def get_smallest(number_list):
    """
    주어진 리스트에서 제일 작은 숫자를 반환함

        Parameters:
            number_list (list): integer로 값으로만 구성된 list
            ex - [10, 33, 22, 99, 33]

        Returns:
            smallest_number (int): parameter number_list 중 가장 작은 값

        Examples:
            >>> number_list = [39, 54, 32, 11, 99]
            >>> import basic_math as bm
            >>> bm.get_smallest(number_list)
            11
    """
    smallest_number = min(number_list)
    return smallest_number


def get_mean(number_list):
    """
    주어진 리스트 숫자들의 평균을 구함.

        Parameters:
            number_list (list): integer로 값으로만 구성된 list
            ex - [10, 33, 22, 99, 33]

        Returns:
            mean (int): parameter number_list 숫자들의 평균

        Examples:
            >>> number_list = [39, 54, 32, 11, 99]
            >>> import basic_math as bm
            >>> bm.get_mean(number_list)
            47
    """
    mean = int(sum(number_list) / len(number_list))
    return mean


def get_median(number_list):
    """
    주어진 리스트 숫자들의 중간값을 구함.

        Parameters:
            number_list (list): integer로 값으로만 구성된 list
            ex - [10, 33, 22, 99, 33]

        Returns:
            median (int): parameter number_list 숫자들의 중간값

        Examples:
            >>> number_list = [39, 54, 32, 11, 99]
            >>> import basic_math as bm
            >>> bm.get_median(number_list)
            39
            >>> number_list2 = [39, 54, 32, 11, 99, 5]
            >>> bm.get_median(number_list2)
            35.5
    """
    number_list.sort()
    mid = int((len(number_list) - 1) / 2)
    # using ternary operator
    median = sum(number_list[mid:mid+2]) / 2 if len(number_list) % 2 == 0 else number_list[mid]
    
    # without using ternary operator
    # median = number_list[mid]
    # if len(number_list) % 2 == 0:
    #     median += number_list[mid+1]
    #     median /= 2

    return median


def main():
    number_list = [10, 33, 22, 99, 33]
    number_list2 = [39, 54, 32, 11, 99, 5]

    print ("Get Greatest Test")
    print (get_greatest(number_list)) # Expected Result: 99
    print ("Get Greatest Test Closed \n")


    print ("Get Smallest Test")
    print (get_smallest(number_list)) # Expected Result: 10
    print ("Get Smallest Test Closed \n")

    number_list = [39, 54, 32, 11, 99]

    print ("Get Mean Test")
    print (get_mean(number_list)) # Expected Result: 47
    print ("Get Mean Test Closed \n")

    print ("Get Median Test")
    print (get_median(number_list)) # Expected Result: 39
    print (get_median(number_list2)) # Expected Result: 35.5
    print ("Get Median Test Closed \n")


if __name__ == "__main__":
    main()