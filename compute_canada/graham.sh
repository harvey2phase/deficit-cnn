#!/bin/bash

#SBATCH --gres=gpu:1
#SBATCH --mem=1G
#SBATCH --time=0-03:00

module load python/3.7

seff #find mem utilized
salloc --time=15 # gives interactive session
nvidia-smi
module list
sbatch NAME_OF_SCRIPT # runs when has resources

# Create a virtual environment

mkdir DIR
virtualenv DIR
