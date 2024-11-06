import matplotlib.pyplot as plt
import numpy as np
from sys import argv

#The data
"""
1995      0.45
1997      0.47
1999      0.38
2001      0.53
2003      0.62
2005      0.68
2007      0.66
2009      0.65
2011      0.61
2013      0.68
2015      0.89
2017      0.92
2019      0.97
2021      0.85
2023      1.17
"""

label_font = {'fontname':'DejaVu Sans Mono', 'weight' : 'normal', 'size' : 22}
tick_font = {'fontname':'DejaVu Sans Mono', 'weight' : 'normal', 'size' : 12}

years =          np.array([1995, 1997, 1999, 2001, 2003, 2005, 2007, 2009, 2011, 2013, 2015, 2017, 2019, 2021, 2023])
change_in_temp = np.array([0.45, 0.47, 0.38, 0.53, 0.62, 0.68, 0.66, 0.65, 0.61, 0.68, 0.89, 0.92, 0.97, 0.85, 1.17])

#regression line
#a + bx
regression_y_int = -44.464625
regression_slope = 0.02248214

def main(args: list[str]):
    if "-residual_plot" in args:
        plt.scatter(years, change_in_temp - (regression_y_int + regression_slope * years))
        plt.xlabel("Year", **label_font)
        plt.ylabel("Residual", **label_font)
        plt.axhline(**{'color' : 'black'})
    else:
        plt.scatter(years, change_in_temp)
        plt.xlabel("Year", **label_font)
        plt.ylabel("Change in Temperature (C°)", **label_font)



    #scales
    plt.xticks(years[::2], **tick_font)
    plt.yticks(**tick_font)

    left, right = plt.xlim()
    plt.xlim(left, right)
    top, bottom = plt.ylim()
    plt.ylim(top, bottom)

    if "-regression_line" in args:
        plt.axline([0, regression_y_int], slope=regression_slope, **{'color':'red'})


    plt.show()


if __name__ == "__main__":
    main(argv[1:])