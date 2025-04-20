import pytest
from app import load_model

def test_model_loading():
    """Test that the model loads correctly"""
    model = load_model()
    assert model is not None, "Model should not be None"
    assert hasattr(model, 'pipe'), "Model should have a pipe attribute"
    assert hasattr(model.pipe, 'to'), "Model pipe should have a to method"

def test_model_device():
    """Test that the model is on the correct device"""
    model = load_model()
    device = model.pipe.device
    assert str(device).startswith(('cuda', 'cpu')), "Model should be on either CUDA or CPU" 