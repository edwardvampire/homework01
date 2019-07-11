num = 5
buildingArea = {
    "sumplanValue":"var1",
	"detail":[
		{
			"name":"计容总建筑面积",
			"planValue":"var2"
		},
		{
			"name":"不计容总建筑面积",
			"planValue":"var3"
		}
	]
}
# print(buildingArea)

# def cal_building_area():
building_area = buildingArea["detail"]
print(building_area)
area = 0
for building_area_item in building_area:
    if building_area_item["name"] == "计容总建筑面积":
        area = building_area_item["planValue"]
        print(area)