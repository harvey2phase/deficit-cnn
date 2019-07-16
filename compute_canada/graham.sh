#!/bin/bash

#SBATCH --gres=gpu:1
#SBATCH --mem=1G
#SBATCH --time=0-03:00

module load cuda cudnn
module load python/3.6
source tensorflow/bin/activate
