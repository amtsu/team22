# Weight = 92
# MoonWeight = Weight * 0.165
# Year = 0

# for Year in range (0,15):
#     Year = Year + 1
#     MoonWeight = MoonWeight + 1
#     print(MoonWeight)

def MoonWeightFn(Weight, Years, WeighGainStep):
    YearCount = 0
    MoonWeight = Weight * 0.165
    while YearCount < Years:
        YearCount = YearCount + 1
        MoonWeight = MoonWeight + WeighGainStep
        print(MoonWeight)

MoonWeightFn(92, 15, 1)
