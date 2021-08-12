# GenericFramework

## Introduction
This branch is the implementation of plotting line chart and scatter chart.

* matplotlib == 3.4.1
* Numpy == 1.19.5


## Utility Modules
Let's see the utility modules first. 

* `plotter.py`  It is the main drawing code, which can read the input data file and draw the information into the corresponding '.pdf' file. 

* `*.data`  This is a data file with corresponding data and corresponding parameter settings. Among them, the corresponding adjustment is the figure format, and the 'plot_type' is set to 'line' and 'bar' to correspond to the line chart and the histogram respectively. 'legend_loc' corresponds to different positions, 'up' corresponds to the top out of the figure, 'right' corresponds to the right outside the figure, 'auto' corresponds to the position inside the picture that can be set by 'loc', and 'none' corresponds to not generating a legend. The part of the data, the first column corresponds to the x-axis data, and each remaining column corresponds to different graph data.

Run the code with 
~~~python
python plotter.py -f train_acc.data
~~~
