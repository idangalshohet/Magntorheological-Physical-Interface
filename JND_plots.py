import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

plt.rcParams.update({'font.size': 12})
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = 'CMU Serif, Times New Roman'
plt.rcParams["mathtext.fontset"] = "dejavuserif"


colors = [[100/255, 143/255, 255/255, 1.0],
          [120/255, 94/255, 240/255, 1.0],
          [255/255, 176/255, 0/255, 1.0],
          [255/256, 97/255, 0/255, 1.0],
          [220/255, 38/255, 127/255, 1.0]]


def JND(name):
    df = pd.read_csv("JND" + name + '.csv')
    y = df['y']
    yhat = df['yhat']
    delta = df['delta']
    arr1inds = delta.argsort()
    delta = delta[arr1inds]
    y = y[arr1inds]
    yhat = yhat[arr1inds]
    correct = yhat == y
    accuracy = np.zeros(len(np.unique(delta)))
    unique_deltas, idx = np.unique(delta, return_index=True)
    n = 0
    for i in range(len(np.unique(delta))):
        N = np.count_nonzero(delta == unique_deltas[i])
        accuracy[i] = np.sum(correct[n:n+N]) / N
        n += N

    try:
        K = 7  # psychometric force scales between 0 and 1 on the delta scale, set this to your max delta
        delta_plot, accuracy_fit = psychometric_fit(unique_deltas/K, accuracy)
        idx = (np.abs(accuracy_fit - 0.75)).argmin()
        print('JND', ': ', delta_plot[idx]*K)
        percentage = np.abs(0.0092*(delta_plot[idx]*K))/((0.0092*(230)))
        # current = np.abs(0.0092*(delta_plot[idx]*K)- 1.8655)
        print('JND (current)', ':', percentage, '%')
        # print('JND (percentage)', ':', percentage, '%')
        plt.plot(delta_plot*K, accuracy_fit, label='Mean', linewidth=4.0, color='k', zorder=10)
    except Exception as e:
        print(e)
    # plt.ylabel('Accuracy')
    # plt.xlabel('Change in Normal Displacement - mm')
    # fig.subplots_adjust(bottom=0.110, top=0.980, left=0.145, right=0.995)
    # plt.legend()
    # plt.show()
    plt.scatter(unique_deltas, accuracy)
    plt.xlabel('Change in Stiffness (PWM)')
    plt.ylabel('Accuracy')
    plt.show()




def psychometric_fit(deltas, accuracy):
    from scipy.optimize import curve_fit
    from scipy.special import expit

    def sigmoid(x, x0, k):
        # y = L / (1 + np.exp(-k * (x - x0))) + b
        y = 0.5 / (1 + np.exp(-k * (x - x0))) + 0.5
        return (y)

    # deltas = np.linspace(0, 10, 10)
    delta_plot = np.linspace(0, 1, 100)
    # accuracy = np.clip(0.5*(expit(deltas - 5) + 1) + np.random.normal(0, 0.075, deltas.shape), 0.5, 1.0)

    p0 = [np.median(deltas), 1]  # this is an mandatory initial guess

    popt, pcov = curve_fit(sigmoid, deltas, accuracy, p0, method='dogbox')

    accuracy_fit = sigmoid(delta_plot, *popt)
    # fig = plt.figure(figsize=(6, 6))
    # plt.scatter(deltas, accuracy, label='data', color='k')
    # alldeltas = []
    # allaccuracy = []
    # for i in range(5):
    #     deltas = np.linspace(0, 10, 10)
    #     delta_plot = np.linspace(0, 10, 100)
    #     accuracy = np.clip(0.5 * (expit(deltas - 5) + 1) + np.random.normal(0, 0.05, deltas.shape), 0.5, 1.0)
    #     allaccuracy = np.concatenate([allaccuracy, accuracy])
    #     alldeltas = np.concatenate([alldeltas, deltas])
    #     p0 = [np.median(deltas), 1]  # this is an mandatory initial guess
    #
    #     popt, pcov = curve_fit(sigmoid, deltas, accuracy, p0, method='dogbox')
    #
    #     accuracy_fit = sigmoid(delta_plot, *popt)
    #     plt.scatter(deltas, accuracy, s=10, color=colors[i])
    #     plt.plot(delta_plot, accuracy_fit, linewidth=2.0, color=colors[i], label='Device '+str(i+1))
    # p0 = [np.median(deltas), 1]  # this is an mandatory initial guess

    # popt, pcov = curve_fit(sigmoid, alldeltas, allaccuracy, p0, method='dogbox')

    # accuracy_fit = sigmoid(delta_plot, *popt)
    # plt.ylim(0, 1.3)
    # plt.legend(loc='best')
    return delta_plot, accuracy_fit


if __name__ == "__main__":
    plot, value = JND('Abi2')
    


# 0.0092x - 1.8655 equation to convert to current 