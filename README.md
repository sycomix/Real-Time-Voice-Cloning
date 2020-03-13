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

conda create --name dles tensorflow-gpu=1.14.0 umap-learn visdom webrtcvad librosa>=0.5.1 matplotlib>=2.0.2 numpy>=1.14.0 scipy>=1.0.0 tqdm sounddevice Unidecode inflect PyQt5 multiprocess numba

```
conda create -n dles python=3.7 pip -y
conda activate dles


# After the repo has been cloned, and inside the project root folder, with the
# (dles) enviroment, execute:
pip install -r rtvc/requirements.txt

```

### Play with the project

TODO
