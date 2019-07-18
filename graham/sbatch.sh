#!/bin/bash

#SBATCH --gres=gpu:1
#SBATCH --mem=4G
#SBATCH --cpus-per-task=12
#SBATCH --time=0-10:00

#SBATCH --mail-user=harvey@dal.ca
#SBATCH --mail-type=ALL

module load cuda cudnn
module load python/3.6
source tensorflow/bin/activate
python3 ../cnn/deficit_cnn15.py
