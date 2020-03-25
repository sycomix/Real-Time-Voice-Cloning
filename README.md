# Steps

### Install anaconda

```
mkdir -p ~/Downloads
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/Downloads/miniconda.sh
bash ~/Downloads/miniconda.sh -b -p $HOME/miniconda

# Any new terminal will start the base enviroment
echo 'eval "$($HOME/miniconda/bin/conda shell.bash hook)"' >> ~/.bashrc

# This will activate the enviroemnt for you on this instance
eval "$($HOME/miniconda/bin/conda shell.bash hook)"
```

### Activate conda enviroment


```
conda create -n dles python=3.7 pip -y
conda activate dles


# After the repo has been cloned, and inside the project root folder, with the
# (dles) enviroment, execute:
pip install -r rtvc/requirements.txt

```

### Play with the project

Run the code with (**Currently not working due to a missing lib**)

```
cd rtvc
python demo_cli.py
```

