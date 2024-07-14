from matplotlib.testing.decorators import compare_images
pathGrafico = 'figBCCgrafico07.png'
plt.savefig(pathGrafico)
pathGraficoCompare = 'figBCCgrafico07(a3)(b-14).png'
print(compare_images(pathGrafico, pathGraficoCompare, 0.5))