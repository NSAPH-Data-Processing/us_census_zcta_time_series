#!/bin/bash
#
#SBATCH -p fasse # partition (queue)
#SBATCH -c 4 # number of cores
#SBATCH --mem 48GB # memory pool for all cores
#SBATCH -t 0-00:30 # time (D-HH:MM)
#SBATCH --array=2011-2020

python census_zcta.py --year $SLURM_ARRAY_TASK_ID