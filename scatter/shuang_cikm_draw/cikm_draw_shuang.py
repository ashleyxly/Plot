import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
from matplotlib import rcParams
import matplotlib.pylab as pylab

print(rcParams.keys())

params = {
    'font.family': 'sans-serif',
    'font.sans-serif': 'Times New Roman',
    'font.weight': 'bold',

    'legend.fontsize': 45,

    'xtick.labelsize': 35,
    'ytick.labelsize': 35,

    'axes.labelsize': 45,
    'axes.labelweight': 'bold',

    'lines.linewidth': 3.5,

    'figure.figsize': [12, 10],
    # 'figure.figsize': [16, 10],

    'grid.alpha': 0.3,
    # 'grid.color': '#b0b0b0',
    'grid.linestyle': (5, 9),
    # 'grid.linewidth': 0.8,
}

pylab.rcParams.update(params)


def plot_purchase_attack():
    """
    Returns: 折线图

    """
    x = np.arange(1, 21)
    z = [0.78477313, 0.81788236, 0.85982635, 0.86693807, 0.87313761, 0.88258049, 0.8915335, 0.89133079, 0.89617892,
         0.90374675, 0.89967566, 0.89930403, 0.9054191, 0.91128079, 0.90388189, 0.90584141, 0.91322342, 0.91415251,
         0.91499713, 0.90508125]

    # error rate
    v1 = [0.01186758, 0.01156371, 0.01925192, 0.02457606, 0.02433478, 0.03003762, 0.02821923, 0.02565503, 0.03092966,
          0.03042565, 0.03247866, 0.03600498, 0.03591394, 0.03453252, 0.03563844, 0.03533031, 0.04028614, 0.04159193,
          0.04000808, 0.03874105]
    v2 = [0.16636697, 0.09011596, 0.05275138, 0.03363397, 0.02310207, 0.01730564, 0.01393261, 0.0117885, 0.0105344,
          0.00975418, 0.00904857, 0.00858518, 0.00842041, 0.00830077, 0.00817736, 0.00806694, 0.00812135, 0.00820261,
          0.00825487, 0.00838416]
    plt.figure()
    plt.subplots_adjust(right=0.87)
    ax = plt.gca()  # 注意:一般都在ax中设置,不再plot中设置
    l1 = plt.plot(x, v1, 'o-', color='#377eb8', label='static', linewidth=4.5, markersize=12)  # 修改linewidth和markersize
    l2 = plt.plot(x, v2, 's-', color='#4daf4a', label='adaptive', linewidth=4.5, markersize=12)

    # ax.invert_yaxis()

    xmajorLocator = MultipleLocator(2)  # 将x主刻度标签设置为5的倍数
    # # 设置主刻度标签的位置,标签文本的格式
    ax.xaxis.set_major_locator(xmajorLocator)
    ymajorFormatter = FormatStrFormatter('%.2f')
    ax.yaxis.set_major_formatter(ymajorFormatter)
    xminorLocator = MultipleLocator(2)  # 将x轴次刻度标签设置为1的倍数
    ax.xaxis.set_minor_locator(xminorLocator)
    ax.xaxis.grid(True, linestyle='dotted')  # x坐标轴的网格使用主刻度
    ax.yaxis.grid(True, linestyle='dotted')  # y坐标轴的网格使用次刻度

    ###设置坐标轴的粗细
    # ax1 = plt.gca();  # 获得坐标轴的句柄
    ax.spines['bottom'].set_linewidth(3.5);  ###设置底部坐标轴的粗细
    ax.spines['left'].set_linewidth(3.5);  ####设置左边坐标轴的粗细
    ax.spines['right'].set_linewidth(3.5);  ###设置右边坐标轴的粗细
    ax.spines['top'].set_linewidth(3.5);  ####设置上部坐标轴的粗细

    ax.set_xlabel('epoch')
    ax.set_ylabel('error rate')

    ax2 = ax.twinx()  # this is the important function

    l3 = ax2.plot(x, z, 'D-', color='#ff8000', label='accuracy', linewidth=4.5, markersize=12)
    ax2.yaxis.set_major_formatter(ymajorFormatter)
    ax2.set_ylabel('accuracy')

    line = l1 + l2 + l3
    labs = [l.get_label() for l in line]
    ax.legend(line, labs, loc=7)
    plt.savefig(
        './purchase/purchase_attack_error_rate.eps')
    plt.show()


def purchase_poison_ratio():
    """

    Returns: 柱状图

    """
    poison_ratio = [0.05, 0.1, 0.5, 1, 5, 10, 20, 30]

    static_index = np.arange(len(poison_ratio))
    width = 0.4
    adaptive_index = static_index + width

    # error rate
    error_static = [0.368806435, 0.280237774, 0.196768945, 0.129812961, 0.01156371, 0.004586263, 0.003169986,
                    0.002514591]
    error_adaptive = [0.259904267, 0.23979933, 0.119779218, 0.060267627, 0.008066936, 0.004222962, 0.00206704,
                      0.001303285]

    plt.figure()

    plt.grid(linestyle='dotted')  # 显示网格
    ###设置坐标轴的粗细
    ax1 = plt.gca();  # 获得坐标轴的句柄
    ax1.spines['bottom'].set_linewidth(3.5);  ###设置底部坐标轴的粗细
    ax1.spines['left'].set_linewidth(3.5);  ####设置左边坐标轴的粗细
    ax1.spines['right'].set_linewidth(3.5);  ###设置右边坐标轴的粗细
    ax1.spines['top'].set_linewidth(3.5);  ####设置上部坐标轴的粗细
    # plt.ylim(0.5,1.1)
    plt.bar(static_index, error_static, width=width, label='static', fc='#769fcd')
    plt.bar(adaptive_index, error_adaptive, width=width, label='adaptive', fc='#96bb7c')
    plt.xticks(static_index + width / 2, poison_ratio)
    plt.xlabel('poison ratio(%)')
    plt.ylabel('error rate')
    plt.legend(loc='upper right')
    plt.savefig(
        './purchase_poison_ratio_error_rate_bar.eps')
    plt.show()


def plot_purchase_defense_add_simple():
    """

    Returns: 散点图

    """
    x1 = [0.914997128]
    x2 = [0.912480151, 0.901195986, 0.890367918, 0.868255684, 0.856278928, 0.801902091, 0.895705936]
    x3 = [0.91665259, 0.910571303, 0.909625325, 0.900976384, 0.894861313, 0.895537011, 0.892901787, 0.888560424,
          0.885401534, 0.880992601]
    x4 = [0.922885908, 0.913358559, 0.909050981, 0.908510423, 0.896651914, 0.919710125, 0.912209872, 0.909811142,
          0.905841414]
    x5 = [0.897682354, 0.901449373, 0.904642049, 0.909287476, 0.905588027, 0.908476638, 0.911517281, 0.914794419]

    # error rate
    y1 = [0.008066936]
    # basic
    y2 = [0.069849997, 0.182988899, 0.225155312, 0.269002642, 0.296149494, 0.315669283, 0.179683102]
    # naive
    y3 = [0.04245585, 0.066065894, 0.07010631, 0.085913123, 0.103716202, 0.11709051, 0.115459,
          0.124743865, 0.133296068, 0.137090484]
    # our
    y4 = [0.121662602, 0.160826449, 0.187192374, 0.219530255, 0.22867731, 0.154856704, 0.174315348,
          0.200074811, 0.215688081]
    # our+variant
    y5 = [0.133952649, 0.130124702, 0.143909821, 0.14283689, 0.158703678, 0.156199106, 0.157739572,
          0.153855992]

    fig, ax = plt.subplots()
    ax.scatter(np.array(x1), np.array(y1), label="no defense", c='#e41b1b', marker='o', s=500)  # 散点的大小
    ax.scatter(np.array(x3), np.array(y3), label="naive", c='#377eb8', marker='D', s=500)
    ax.scatter(np.array(x2), np.array(y2), label="basic", c='#4daf4a', marker='s', s=500)
    ax.scatter(np.array(x4), np.array(y4), label="ours", c='#ff8000', marker='8', s=500)
    ax.scatter(np.array(x5), np.array(y5), label=r'ours:fix $\tau$', c='#8b5e83', marker='p', s=500)
    # yMajorFormatter = FormatStrFormatter('%1.1f')
    # ax.yaxis.set_major_formatter(yMajorFormatter)

    plt.grid(linestyle='dotted')  # 显示网格
    # plt.gca().invert_yaxis()

    ###设置坐标轴的粗细
    ax1 = plt.gca();  # 获得坐标轴的句柄
    ax1.spines['bottom'].set_linewidth(3.5);  ###设置底部坐标轴的粗细
    ax1.spines['left'].set_linewidth(3.5);  ####设置左边坐标轴的粗细
    ax1.spines['right'].set_linewidth(3.5);  ###设置右边坐标轴的粗细
    ax1.spines['top'].set_linewidth(3.5);  ####设置上部坐标轴的粗细
    plt.xlabel("accuracy")
    plt.ylabel("error rate")
    plt.legend(loc='lower left', fancybox=True, framealpha=0)  # 图例设置透明
    # plt.set_facecolor('none')
    plt.savefig(
        './purchase_defense_add_simple_error_rate.eps')
    plt.show()


if __name__ == "__main__":
    plot_purchase_attack()
    purchase_poison_ratio()
    plot_purchase_defense_add_simple()
