import pytest
from main import Math

class TestUserFunctions:
    def test_sum_all_numbr(self):
        math_obj1 = Math([9,1,5])
        assert math_obj1.sum_all_numb() == 15
        math_obj2 = Math([-1, 0, 1])
        assert math_obj2.sum_all_numb() == 0
        math_obj3 = Math([])
        assert math_obj3.sum_all_numb() == 0


    def test_average(self):
        math_obj = Math([1, 2, 3, 4, 5])
        assert math_obj.avearge() == 3.0
        math_obj2 = Math([10, 20, 30])
        assert math_obj2.avearge() == 20.0
        math_obj3 = Math([5])
        assert math_obj3.avearge() == 5.0


    def test_max_elements(self):
        math_obj = Math([1, 5, 3, 9, 2])
        assert math_obj.max_elemnets() == 9
        
        math_obj2 = Math([-5, -1, -10])
        assert math_obj2.max_elemnets() == -1
        
        math_obj3 = Math([7])
        assert math_obj3.max_elemnets() == 7


    def test_min_element(self):
        math_obj = Math([1, 5, 3, 9, 2])
        assert math_obj.min_element() == 1
        
        math_obj2 = Math([-5, -1, -10])
        assert math_obj2.min_element() == -10
        
        math_obj3 = Math([7])
        assert math_obj3.min_element() == 7