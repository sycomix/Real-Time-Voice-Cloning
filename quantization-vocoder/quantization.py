import torch
import torch.nn as nn
import torch.quantization
import os
from vocoder.fatchord_version import WaveRNN
from vocoder import hparams as hp

def print_size_of_model(model):
    torch.save(model.state_dict(), "temp.p")
    print('', os.path.getsize("temp.p")/1e6)
    os.remove('temp.p')


def main():
    saved_model_dir = './saved_models/'
    float_model_file = 'pretrained.pt'

    # create directory
    if not os.path.exists(saved_model_dir):
        try:
            os.makedirs(saved_model_dir)
        except OSError as e:
            raise Exception("Could not create directory {0:}. Please check file system permissions.".format(saved_model_dir))
    if not os.path.exists(saved_model_dir + float_model_file):
        raise Exception("Cannot perform static quantization without trained model. Please provide weights file.")

    # set default device to cpu since pytorch only supports quantization on CPU
    _device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    _device = torch.device("cpu")

    myModel = WaveRNN(
        rnn_dims=hp.voc_rnn_dims,
        fc_dims=hp.voc_fc_dims,
        bits=hp.bits,
        pad=hp.voc_pad,
        upsample_factors=hp.voc_upsample_factors,
        feat_dims=hp.num_mels,
        compute_dims=hp.voc_compute_dims,
        res_out_dims=hp.voc_res_out_dims,
        res_blocks=hp.voc_res_blocks,
        hop_length=hp.hop_length,
        sample_rate=hp.sample_rate,
        mode=hp.voc_mode
    )

    checkpoint = torch.load(saved_model_dir + float_model_file)
    myModel.load_state_dict(checkpoint["model_state"])
    myModel.to(_device)
    myModel.eval()

    # Convert to quantized model
    myModel_quantized = torch.quantization.quantize_dynamic(myModel, {nn.Linear}, dtype=torch.qint8)
    print("Size of model before quantization(MB): ", end="")
    print_size_of_model(myModel)
    print("Size of model after quantization(MB): ", end="")
    print_size_of_model(myModel_quantized)
    quantized_model_file = f'{saved_model_dir}./quantized.pt'
    torch.save({"model_state":myModel_quantized.state_dict()}, quantized_model_file)

if __name__ == '__main__':
    main()
