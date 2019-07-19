#!/bin/bash

#SBATCH --gres=gpu:1
#SBATCH --mem=2.5G
#SBATCH --cpus-per-task=6
#SBATCH --time=0-5:00

#SBATCH --mail-user=harvey@dal.ca
#SBATCH --mail-type=ALL

module load cuda cudnn
module load python/3.6
source tensorflow/bin/activate
python3 ../cnn/1_layer_deficit_cnn.py
