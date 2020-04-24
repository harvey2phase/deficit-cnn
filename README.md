# Deficit CNN

## About
I investigated, using a convolutional neural
network (CNN), the classification of simulation data from a
[human aging model](https://journals.aps.org/pre/abstract/10.1103/PhysRevE.98.032302)
to predict mortality. I worked on this project part-time with
[Dr. Andrew Rutenberg](http://fizz.phys.dal.ca/~adr/index.php?TreeIndex=0).
This repo was made public on July 29, 2019.

The execution of CNN simulations was made possible by Compute Canada's
[Graham](https://docs.computecanada.ca/wiki/Graham) and Cedar clusters.



## Preliminary Results

### Binary Classification
**Question**: Can the CNN predict whether a model individual will reach mortality in 5 years
at age 80? Mortality in 10 years?
**Question**: Does the accurcy of the prediction improve given more history of 
individuals' health trajectory?

![alt text](https://github.com/harvey2phase/deficit-cnn/blob/master/results/config0.png)

**Question**: How does accuracy change with different configurations?
![alt text](https://github.com/harvey2phase/deficit-cnn/blob/master/results/config1.png)
![alt text](https://github.com/harvey2phase/deficit-cnn/blob/master/results/config2.png)
![alt text](https://github.com/harvey2phase/deficit-cnn/blob/master/results/config3.png)
![alt text](https://github.com/harvey2phase/deficit-cnn/blob/master/results/config4.png)
