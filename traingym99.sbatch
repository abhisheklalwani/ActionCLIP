#!/bin/bash
#SBATCH --gres=gpu:2
#SBATCH -p gpu-long
#SBATCH --mail-type=ALL
#SBATCH --mail-user=alalwani@cs.umass.edu
#SBATCH --job-name actionClipGym99TrainSet0InitializationV3
#SBATCH -o unity_logs/actionClipGym99TrainSet0InitializationV3.out
#SBATCH -e unity_logs/actionClipGym99TrainSet0InitializationV3.err
#SBATCH --mem 40960
. /work/alalwani_umass_edu/miniconda/etc/profile.d/conda.sh
conda activate action-clip
srun python -u train.py --config ./configs/gym99/gym99_train_set_labels_0_initialization.yaml