# function to test validity of kernels

def valid_conv(conv_list):
    # kernel should match input channels, why [1] index?
    assert(3 == kernel.shape[1])
    Cin = 3
    H = 36
    W = 36
    (Cin, H, W) = img.shape
    (Cout, _, Kh, Kw) = kernel.shape
    output = np.zeros((Cout, H - Kh + 1, W - Kw + 1))
    # next layer should be output size?
    '''
    assert kernel shape matches
    does the kernel have to fit nicely into the image?
    img_shape = (3,36,36)
    kernal_shape = kernel.shape()
    for c in convolutions:
        (Cin, H, W) = img.shape
        (Cout, _, Kh, Kw) = kernel.shape
        next_layer = next in c
        assert(next_layer.shape() = (Cout, H - Kh + 1, W - Kw + 1))
        
    
    '''
    return True