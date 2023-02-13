import matplotlib.pyplot as plt

def p():
    while True:
        try:
            plt.pause(0.1)
        except KeyboardInterrupt:
            break
