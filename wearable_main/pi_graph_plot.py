import calendar


def plot_pi_graph(plt=None, data_frame=None, input_series=None):

    if plt is not None and data_frame is not None and input_series is not None:
        filter_referance = data_frame.loc[data_frame['Date'] == input_series]
        x = filter_referance['Activity']
        y = filter_referance['Calories']
        explode_list = list()
        for d in range(len(x)):
            if d % 2 == 0:
                explode_list.append(.02)
            else:
                explode_list.append(.02)
        plt.pie(y, explode=explode_list, labels=x, autopct='%1.2f', startangle=90)
        proper_date = input_series.split('/')[0] + " " + calendar.month_name[int(input_series.split('/')[1])][
                                                         :3] + ". 20" + input_series.split('/')[2]
        plt.title("Calories Burn Percent on (" + proper_date + ")")
    else:
        pass

