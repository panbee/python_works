from dice import Dice

import pygal

# 创建一个D6和一个D10
dice_1 = Dice()
dice_2 = Dice(10)

# 掷骰子多次，并将结果存储在一个列表中
results = []
for roll_num in range(50000):
    result = dice_1.roll() + dice_2.roll()
    results.append(result)

# 分析结果
frequencies = []
max_result = dice_1.num_sides + dice_2.num_sides 
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# 可视化结果
hist = pygal.Bar()

hist.title = "Results of rolling a D6 and a D10 50,000 times." 
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12',
       '13', '14', '15', '16']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"
hist.add('D6 + D10', frequencies)
hist.render_to_file('dice_visual.svg')