# Steps

### Install anaconda

```
mkdir -p ~/Downloads
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/Downloads/miniconda.sh
bash ~/Downloads/miniconda.sh -b -p $HOME/miniconda

echo 'eval "$($HOME/miniconda/bin/conda shell.bash hook)"' >> ~/.bashrc
```

### Activate conda enviroment

conda create --name dles tensorflow-gpu=1.14.0 umap-learn visdom webrtcvad librosa>=0.5.1 matplotlib>=2.0.2 numpy>=1.14.0 scipy>=1.0.0 tqdm sounddevice Unidecode inflect PyQt5 multiprocess numba

### Play with the project

1. Clone this repository and
2.  
