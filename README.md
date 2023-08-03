# census_acs5

Using census package to extract acs5 data.


## Run

### Conda Environment

**Clone the repository** Clone the repository and create a conda environment.

```bash
git clone <https://github.com/<user>/repo>
cd <repo>

conda env create -f requirements.yml
conda activate <env_name> #environment name as found in requirements.yml
```

It is also possible to use `mamba`.

```bash
mamba env create -f requirements.yml
mamba activate <env_name>
```

**Create entrypoints** Add symlinks to input, intermediate and output folders inside the corresponding `/data` subfolders.

For example:

```bash
export HOME_DIR=$(pwd)

cd $HOME_DIR/data/input/ .
ln -s <input_path> . #paths as found in data/input/README.md if any

cd $HOME_DIR/data/output/
ln -s <output_path> . #paths as found in data/output/README.md if any
```

The README.md files inside the `/data` subfolders contain path documentation for NSAPH internal purposes.

**Run pipeline** Run the script for all years:

```bash
python ./src/<main_script>.py --year <year>
```

or run the pipeline:

```bash
snakemake --cores
```

In addition, `.sbatch` templates are provided for SLURM users. Be mindful that each HPC clusters has a different configuration and the `.sbatch` files might need to be modified accordingly. 

### Container
