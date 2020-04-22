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


#### Commmandline:

For the command line interface, put the pre-trained models in the correct locations

```
rtvc/vocoder/saved_models/pretrained/pretrained.pt
rtvc/synthesizer/saved_models/logs-pretrained/taco_pretrained/<tf checkpoints>
rtvc/encoder/saved_models/pretrained/pretrained.pt
```

And run the code with:

```
cd rtvc
python demo_cli.py
```

#### Graphical interface:

```
cd rtvc
python demo_toolbox.py
```


### Quantization experiments

Files associatied with quantization can be found in:

```
quantization-encoder
quant_demo_enc.ipynb
quant_demo_synth.ipynb
quantization-vocoder
```


