import tensorflow as tf

g = tf.Graph()

with g.as_default() as g:
    # Actual Implementation (Used by our project)
    tf.train.import_meta_graph('/home/agostini/Development/Real-Time-Voice-Cloning/rtvc/synthesizer/saved_models/logs-pretrained/taco_pretrained/tacotron_model.ckpt-278000.meta')
    
    # Tacotron2 implementation (does not have voice encoder), easier to visualize
    # uncomment next line
    #tf.train.import_meta_graph('/home/agostini/Development/data/saved_models/tacotron2/pretrained/model.ckpt-189500.meta')

with tf.Session(graph=g) as sess:
    file_writer = tf.summary.FileWriter(logdir='/tmp/log_dir_delete_me/tacotron2', graph=g)
    
    
    
print('With tensorboard installed:')
print('tensorboard --logdir=/tmp/log_dir_delete_me')

print('On your laptop:')
print('ssh -N -L localhost:6006:localhost:6006 <user@ip-of-lambda-machine>')
print('Now connect to: localhost:6006')
