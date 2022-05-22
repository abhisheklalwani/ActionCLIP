#!/bin/bash
#SBATCH --gres=gpu:1
#SBATCH -p gypsum-m40-course
#SBATCH --mail-type=ALL
#SBATCH --mail-user=alalwani@cs.umass.edu
#SBATCH --job-name actionClipGym99FewShot
#SBATCH -o unity_logs/actionClipGym99FewShot.out
#SBATCH -e unity_logs/actionClipGym99FewShot.err
#SBATCH --mem 40960
. /work/alalwani_umass_edu/miniconda/etc/profile.d/conda.sh
conda activate action-clip
srun python -u train.py --config ./configs/gym99/gym99_train_set_labels_few_shot.yaml