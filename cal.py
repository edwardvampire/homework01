

class Apartment:

    # 输入变量
    def __init__(self, json_para):
        # 输入变量
        self.json_para = json_para

        # 中间变量
        # 户配整理 {115: 0.5, 140: 0.3, 180: 0.2}
        self.house_matching = {}

        # 输出变量
        # 初始化函数
        # 第一阶段
        self.cal_house_matching()

    def cal_house_matching(self):
        # 户配比
        apartment_radio = self.json_para["marketingRequirement"]["apartmentRadio"]

        for apartment_radio_item in apartment_radio:

            area = 0
            count_rate = 0

            for key, value in apartment_radio_item.items():
                if key == "area":
                    area = value
                if key == "countRate":
                    count_rate = value

            self.house_matching[area] = count_rate / 100
