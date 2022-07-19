import pygal

from dice import Dice

# 创建一个D6
dice = Dice()

# 掷几次骰子，并将结果存储在一个列表中
results = []
for roll_num in range(1000000):
    result = dice.roll()
    results.append(result)

# 分析结果
frequencies = []
for value in range(1, dice.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# 对结果进行可视化
hist = pygal.Bar()

hist.title = "Results of rolling one D6 1000 times"
hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist.x_title = "Result"
hist.y_title = "frequency of Result"

hist.add('D6', frequencies)
hist.render_to_file('dice_visual.svg')
