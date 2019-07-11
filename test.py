from cal import Apartment
from json_input_0620 import json_input_0620

def test_cal_house_matching():
    json_para = json_input_0620
    apartment = Apartment(json_para)

    apartment.cal_house_matching()
    print(apartment.house_matching)

test_cal_house_matching()
