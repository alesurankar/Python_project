############
# my data
############
my_title = 'Sunny Days per Month'
my_label = 'Sunny Days'
my_xLabel = 'Month'
my_yLabel = 'Sunny Days'

my_x = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
my_y = [8,10,7,14,20,18,25,19,18,14,12,7]

my_avg = False
my_avg_label = 'Average Sunny Days'
############################################


class Data:
    title = my_title
    label = my_label
    xLabel = my_xLabel
    yLabel = my_yLabel

    x = my_x
    y = my_y

    avg = my_avg
    avg_label = my_avg_label
    avg_value = sum(y) / len(y)
