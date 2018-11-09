

import matplotlib.pyplot as plt
import matplotlib as mpl
from neuralnet import Neural_Network


mpl.rcParams['toolbar'] = 'None'
def draw_neural_net(ax, left, right, bottom, top, net, layer_text=None):
    layer_sizes = [net.no_of_in_nodes, net.no_of_hidden_nodes, net.no_of_out_nodes]
    layers = [net.weights_in_hidden,net.weights_hidden_out]
    n_layers = len(layer_sizes)
    v_spacing = (top - bottom)/float(max(layer_sizes))
    h_spacing = (right - left)/float(len(layer_sizes) - 1)
    ax.axis('off')
    for n, layer_size in enumerate(layer_sizes):
        layer_top = v_spacing*(layer_size - 1)/2. + (top + bottom)/2.
        for m in range(layer_size):
            x = n*h_spacing + left
            y = layer_top - m*v_spacing
            circle = plt.Circle((x,y), v_spacing/4.,
                                color='w', ec='k', zorder=4)
            ax.add_artist(circle)
            if layer_text:
                text = layer_text.pop(0)
                plt.annotate(text, xy=(x, y), zorder=5, ha='center', va='center')

    for n, (layer_size_a, layer_size_b,layer) in enumerate(zip(layer_sizes[:-1], layer_sizes[1:], layers)):
        layer_top_a = v_spacing*(layer_size_a - 1)/2. + (top + bottom)/2.
        layer_top_b = v_spacing*(layer_size_b - 1)/2. + (top + bottom)/2.
        for i,m in enumerate(range(layer_size_a)):
            for ii,o in enumerate(range(layer_size_b)):
                weight = layer[ii][i]
                line = plt.Line2D([n*h_spacing + left, (n + 1)*h_spacing + left], [layer_top_a - m*v_spacing, layer_top_b - o*v_spacing], linewidth=abs(weight*7)+1, c= (1 if weight > 0 else 0, 0, 1 if -weight > 0 else 0))
                ax.add_artist(line)

def show_player_net(winner):
    node_text = ['ball x > or < paddle x', 'ball y > or < half screen y', 'ball dir x', 'ball dir y','','','','','paddle vel left', 'paddle vel right']
    fig = plt.figure(figsize=(8, 8))
    ax = fig.gca()
    draw_neural_net(ax, .1, .9, .1, .9, winner.neural_net, node_text)
    plt.show()
