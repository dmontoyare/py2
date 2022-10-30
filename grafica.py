
import matplotlib.pyplot as plt



def generate_bar_chart():
    labels = ["a", "b", "c"]
    values = [100, 200, 300]
    

    fig, ax = plt.subplot()
    ax.bar(labels, values)
    plt.show()

if __name__ == 'main':
    generate_bar_chart()