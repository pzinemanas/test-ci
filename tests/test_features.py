from dcase_models.data.feature_extractor import FeatureExtractor
from dcase_models.data.features import MelSpectrogram, Spectrogram, MFCC
from dcase_models.data.features import RawAudio, VGGishEmbeddings, FramesAudio
from dcase_models.data.dataset_base import Dataset
from dcase_models.data.data_generator import DataGenerator
from dcase_models.util.files import load_json, mkdir_if_not_exists

import os
import numpy as np
import pytest
import shutil
import librosa



def test_spectrogram():
    feature_extractor = Spectrogram(pad_mode='constant')
    shape = feature_extractor.get_shape(2.0)
    assert shape == (3, 32, 513)

    feature_extractor = Spectrogram(sequence_time=-1, pad_mode='constant')
    shape = feature_extractor.get_shape(2.0)
    assert shape == (1, 64, 513)

    feature_extractor = Spectrogram(sequence_time=1.0, sequence_hop_time=-1, pad_mode='constant')
    shape = feature_extractor.get_shape(2.0)
    assert shape == (1, 32, 513)

def test_mel_spectrogram():
    feature_extractor = MelSpectrogram(pad_mode='constant')
    shape = feature_extractor.get_shape(2.0)
    assert shape == (3, 32, 64)

    feature_extractor = MelSpectrogram(sequence_time=-1, pad_mode='constant')
    shape = feature_extractor.get_shape(2.0)
    assert shape == (1, 64, 64)

    feature_extractor = MelSpectrogram(sequence_time=1.0, sequence_hop_time=-1, pad_mode='constant')
    shape = feature_extractor.get_shape(2.0)
    assert shape == (1, 32, 64)


def test_mfcc():
    feature_extractor = MFCC(pad_mode='constant')
    shape = feature_extractor.get_shape(2.0)
    assert shape == (3, 32, 20)

    feature_extractor = MFCC(sequence_time=-1, pad_mode='constant')
    shape = feature_extractor.get_shape(2.0)
    assert shape == (1, 64, 20)

    feature_extractor = MFCC(sequence_time=1.0, sequence_hop_time=-1, pad_mode='constant')
    shape = feature_extractor.get_shape(2.0)
    assert shape == (1, 32, 20)

openl3_installed = True
try:
    import openl3
except:
    openl3_installed = False

@pytest.mark.skipif(not openl3_installed,
                    reason="Openl3 is not installed")
def test_openl3():
    from dcase_models.data.features import Openl3
    feature_extractor = Openl3()
    shape = feature_extractor.get_shape(2.0)
    assert shape == (4, 512)


def test_raw_audio():
    feature_extractor = RawAudio(pad_mode='constant')
    shape = feature_extractor.get_shape(2.0)
    assert shape == (3, 21760)

def test_frames_audio():
    feature_extractor = FramesAudio(pad_mode='constant')
    shape = feature_extractor.get_shape(2.0)
    assert shape == (3, 32, 1024)

    feature_extractor = FramesAudio(sequence_time=-1, pad_mode='constant')
    shape = feature_extractor.get_shape(2.0)
    assert shape == (1, 64, 1024)

    feature_extractor = FramesAudio(sequence_time=1.0, sequence_hop_time=-1, pad_mode='constant')
    shape = feature_extractor.get_shape(2.0)
    assert shape == (1, 32, 1024)

def test_vggish():
    feature_extractor = VGGishEmbeddings(load_pretrained_weights=False)
    shape = feature_extractor.get_shape(2.0)
    assert shape == (3, 128)
