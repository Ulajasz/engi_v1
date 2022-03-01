import matplotlib
matplotlib.use('TkAgg')
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np
def draw_plot(similarity):

    topics = []
    sim = []
    for value in similarity:
        topics.append(value[0])
        sim.append(value[1])
    #

    fig = plt.figure(figsize=(5,7))
    plt.bar(topics, sim)
    plt.xticks(rotation=30)
    #ax.ylabel('Podobieństwo')

    return fig