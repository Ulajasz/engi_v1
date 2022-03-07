import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


def draw_plot(temp):

    topics = []
    sim = []
    similarity = temp[0]
    skipped = temp[1]
    for value in similarity:
        topics.append(value[0])
        sim.append(value[1])
    #

    fig = plt.figure(figsize=(5,7))
    ax = plt.gca()
    plt.bar(topics, sim)
    plt.xticks(rotation=45)
    ax.set_ylim([0, 100])


    return fig, skipped