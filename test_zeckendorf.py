from zeckendorf import *
def test():
    output = zeckendorf(12)
    np.testing.assert_allclose(output, [8, 3, 1])

    output = zeckendorf(21)
    np.testing.assert_allclose(output, [21])

    output = zeckendorf(4)
    np.testing.assert_allclose(output, [3, 1])

test()
