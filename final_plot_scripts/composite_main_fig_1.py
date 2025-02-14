import pylustrator as pyl
import matplotlib.pyplot as plt

pyl.start()
pyl.load("./sparse_chain_figure.png")
pyl.load("../notebooks/figures/hexbin_map1.png", offset=[-0.00,1.05])
pyl.load("../notebooks/figures/2328_skani.png", offset=[0,1.1])
pyl.load("../notebooks/figures/2328_fastani.png", offset=[0.33,0.66])
pyl.load("../notebooks/figures/2328_mash.png", offset=[0.66,0.66])

#% start: automatic generated code from pylustrator
#plt.figure(1).ax_dict = {ax.get_label(): ax for ax in plt.figure(1).axes}
#import matplotlib as mpl
#plt.figure(1).ax_dict["../notebooks/figures/2328_fastani.png"].set_position([0.323987, 0.063546, 0.275935, 0.221259])
#plt.figure(1).ax_dict["../notebooks/figures/2328_mash.png"].set_position([0.607878, 0.063546, 0.275935, 0.221259])
#plt.figure(1).ax_dict["../notebooks/figures/2328_skani.png"].set_position([0.040097, 0.063546, 0.275935, 0.221259])
#% end: automatic generated code from pylustrator
plt.savefig('auto_fig1.png')
#% start: automatic generated code from pylustrator
plt.figure(1).ax_dict = {ax.get_label(): ax for ax in plt.figure(1).axes}
import matplotlib as mpl
plt.figure(1).ax_dict["../notebooks/figures/2328_fastani.png"].set_position([0.324950, 0.070272, 0.270734, 0.225274])
plt.figure(1).ax_dict["../notebooks/figures/2328_mash.png"].set_position([0.611303, 0.070272, 0.352439, 0.225945])
plt.figure(1).ax_dict["../notebooks/figures/2328_skani.png"].set_position([0.038596, 0.070272, 0.270734, 0.225274])
#% end: automatic generated code from pylustrator
plt.show()
