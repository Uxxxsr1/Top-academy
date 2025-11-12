class Math:
    def __init__(self, numbers):
        self.numbers = numbers

    def sum_all_numb(self):
        return sum(self.numbers)
    def avearge(self):
        return  sum(self.numbers) / len(self.numbers)
    def max_elemnets(self):
        return max(self.numbers)
    def min_element(self):
        return min(self.numbers)