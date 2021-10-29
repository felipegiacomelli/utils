import matplotlib.dates as md
import matplotlib.pyplot as plt


plainColours = ['k', 'r', 'c', 'y', 'm', 'g', 'b']
exColours = ['xk', 'xr', 'xc', 'xy', 'xm', 'xg', 'xb']
pointColours = ['.k', '.r', '.c', '.y', '.m', '.g', '.b']
asteriskColours = ['*k', '*r', '*c', '*y', '*m', '*g', '*b']
fullColours = ['-k', '-r', '-c', '-y', '-m', '-g', '-b']
segmentedColours = ['--k', '--r', '--c', '--y', '--m', '--g', '--b']

GOLD = 1.618
SILVER = 2.414

WIDTH = 20.0

GOLD_WIDTH = WIDTH * 0.393701  # cm to in
GOLD_HEIGHT = GOLD_WIDTH / GOLD

SILVER_WIDTH = WIDTH * 0.393701  # cm to in
SILVER_HEIGHT = SILVER_WIDTH / SILVER

plt.rcParams.update(
    {
        'text.latex.preamble': r'\usepackage{amsmath} \usepackage{bm} \usepackage{lmodern} \usepackage{siunitx}'
    }
)

plt.rc('text', usetex=False)
plt.rc('font', size=16, weight='bold')

plt.rc('lines', linewidth=1.5, markersize=10.0, markeredgecolor='k')

plt.rc('figure', figsize=(SILVER_WIDTH, SILVER_HEIGHT))
plt.rc('savefig', format='pdf')
