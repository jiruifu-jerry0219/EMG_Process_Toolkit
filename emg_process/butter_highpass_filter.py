import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import math

def butter_highpass_filter(f_s, f_pass, f_stop, fs = 0.5, td = 1, g_pass = 1, g_stop = 50, wc = None):
    """
    Return explanation:
    N: number of orders
    b: numerator of the Filter
    a: denominator of the filter
    """
    wp = f_pass / (f_s / 2)
    ws = f_stop / (f_s / 2)
    omega_p = (2 / td) * np.tan(wp / 2)
    omega_s = (2 / td) * np.tan(ws / 2)
    # Find the order and natural frequency of the highpass filter
    N, wn = signal.buttord(omega_p, omega_s, g_pass, g_stop, analog = True)
    # Find the Gain of the highpass filter
    if wc:
        b, a = signal.butter(N, wc, btype = 'high', analog = True)
        wn = wc
    else:
        b, a = signal.butter(N, wn, btype = 'high', analog = True)
    return N, b, a, wn
# def main(input):
#     f_sample = 3500
#     f_pass = 1050
#     f_stop = 600
#     fs = 0.5
#     n, b, a, wn = butter_highpass_filter(f_sample, f_pass, f_stop, wc = 0.5)
#     print("Order of the Filter=", n)
#     print("Cut-off frequency= {:.3f} rad/s ".format(wn))
#     response = signal.lfilter(b, a, input)
#     # Illustrating impulse response
#     plt.stem(np.arange(0, 40), input, markerfmt='D', use_line_collection=True)
#     plt.stem(np.arange(0, 40), response, use_line_collection=True)
#     plt.margins(0, 0.1)
#
#     plt.xlabel('Time [samples]')
#     plt.ylabel('Amplitude')
#     plt.grid(True)
#     plt.show()
#
#
# if __name__ == '__main__':
#     input = signal.unit_impulse(40)
#     main(input)
