class Data:
    title = 'Sunny Days per Month'
    label = 'Sunny Days'
    xLabel = 'Month'
    yLabel = 'Sunny Days'

    x = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    y = [8,10,7,14,20,18,25,19,18,14,12,7]

    avg = False
    avg_label = 'Average Sunny Days'
    avg_value = sum(y) / len(y)
