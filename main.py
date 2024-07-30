
class LargestNonPurchasable():
    """
    Finds the largest non-perfectly purchasable order volume.
    Args:
        input: A list of positive integers representing package sizes.
    Returns:
        The largest non-perfectly purchasable order volume.
    """
    def __init__(self, input: list):
        if not input or len(input) == 1:
            raise ValueError("Input list cannot be empty or single int.")
        self.input = input
        self.find_largest_number()

    def find_common_divisor(self):
        # check if the input has finite purchasable order by finding the great common divisor
        def check_gcd(input):
            result = input[0]
            for num in input[1:]:
                while num:
                    result, num = num, result % num
                    #print(f"{result}, {num} = {num}, {result} % {num}")
            return result
        return check_gcd(self.input) == 1

    def find_largest_number(self):
        #find largest number that cannot be expressed as a linear combination of input values
        
        if not self.find_common_divisor():
            return -1
    
        # Find upper bound on the maximum order volume to limit compute and list of possible order
        max_order_volume = max(self.input) * max(self.input)
        possible_order = [False] * (max_order_volume + 1)
        possible_order[0] = True # 0 is always possible so set to true

        # iterate over the list of possible to value
        for packaging_size in self.input:
            for i in range(packaging_size, max_order_volume + 1):
                if possible_order[i - packaging_size]:
                    possible_order[i] = True

        # iterates over each possible order volume from max_order_volume to 0 in reverse
        for i in range(max_order_volume, -1, -1):
            # return the largest order volume that cannot be expressed
            if not possible_order[i]:
                return i

        return -1  #All order can be expressed


if __name__ == '__main__':
    input = [5, 14]
    find = LargestNonPurchasable(input)
    result = find.find_largest_number()
    print(f"Largest order volume that is NOT perfectly purchasable is {result}")
