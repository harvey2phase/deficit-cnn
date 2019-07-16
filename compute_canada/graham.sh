#!/bin/bash

#SBATCH --gres=gpu:1
#SBATCH --mem=1G
#SBATCH --time=0-03:00

module load python/3.6
source tensorflow/bin/activate

module list
sbatch NAME_OF_SCRIPT # runs when has resources

# Create a virtual environment

mkdir DIR
virtualenv DIR
