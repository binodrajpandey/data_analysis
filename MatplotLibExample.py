import matplotlib.pyplot as plt

def basicLinePlot():
    yield_apples = [0.895, 0.91, 0.919, 0.926, 0.929, 0.931]
    plt.plot(yield_apples)
    plt.show()


def customizePlot():
    years = [2010, 2011, 2012, 2013, 2014, 2015]
    yield_apples = [0.895, 0.91, 0.919, 0.926, 0.929, 0.931]
    plt.plot(years, yield_apples)
    plt.plot(years, yield_apples)
    plt.xlabel('year')
    plt.ylabel('Yield\'s tons per hector')
    plt.title("Fruits yield each year")
    plt.show()


def multiplePlot():
    years = range(2000, 2012)
    apples = [0.895, 0.91, 0.919, 0.926, 0.929, 0.931, 0.934, 0.936, 0.937, 0.9375, 0.9372, 0.939]
    oranges = [0.962, 0.941, 0.930, 0.923, 0.918, 0.908, 0.907, 0.904, 0.901, 0.898, 0.9, 0.896, ]
    plt.plot(years, apples)
    plt.plot(years, oranges)
    plt.xlabel('Years')
    plt.ylabel('Yield tons per hectare')
    plt.title('Crop yield in kanto')
    plt.legend(['Apple', 'Orange'])
    plt.show()


def plotWithMarker():
    years = range(2000, 2012)
    apples = [0.895, 0.91, 0.919, 0.926, 0.929, 0.931, 0.934, 0.936, 0.937, 0.9375, 0.9372, 0.939]
    oranges = [0.962, 0.941, 0.930, 0.923, 0.918, 0.908, 0.907, 0.904, 0.901, 0.898, 0.9, 0.896, ]
    plt.plot(years, apples, marker='o')
    plt.plot(years, oranges, marker='x')
    plt.xlabel('Years')
    plt.ylabel('Yield tons per hectare')
    plt.title('Crop yield in kanto')
    plt.legend(['Apple', 'Orange'])
    plt.show()

def styleLineAndMarker():
    years = range(2000, 2012)
    apples = [0.895, 0.91, 0.919, 0.926, 0.929, 0.931, 0.934, 0.936, 0.937, 0.9375, 0.9372, 0.939]
    oranges = [0.962, 0.941, 0.930, 0.923, 0.918, 0.908, 0.907, 0.904, 0.901, 0.898, 0.9, 0.896, ]
    plt.plot(years, apples, marker='s', c='b', ls='-', lw=2, ms=8, mew=2, mec='navy')
    plt.plot(years, oranges, marker='x', c='r', ls='--', lw=3, ms=10, alpha=0.5)
    plt.xlabel('Years')
    plt.ylabel('Yield tons per hectare')
    plt.title('Crop yield in kanto')
    plt.legend(['Apple', 'Orange'])
    plt.show()

# fmt = '[marker][line][color]'
def shortHandLineStyleMarkerAndColor():
    years = range(2000, 2012)
    apples = [0.895, 0.91, 0.919, 0.926, 0.929, 0.931, 0.934, 0.936, 0.937, 0.9375, 0.9372, 0.939]
    oranges = [0.962, 0.941, 0.930, 0.923, 0.918, 0.908, 0.907, 0.904, 0.901, 0.898, 0.9, 0.896, ]
    plt.plot(years, apples, 's-b')
    plt.plot(years, oranges, 'o--r')
    plt.xlabel('Years')
    plt.ylabel('Yield tons per hectare')
    plt.title('Crop yield in kanto')
    plt.legend(['Apple', 'Orange'])
    plt.show()

def plotWithFigureSize():
    years = range(2000, 2012)
    apples = [0.895, 0.91, 0.919, 0.926, 0.929, 0.931, 0.934, 0.936, 0.937, 0.9375, 0.9372, 0.939]
    oranges = [0.962, 0.941, 0.930, 0.923, 0.918, 0.908, 0.907, 0.904, 0.901, 0.898, 0.9, 0.896, ]
    # Aspect ratio
    plt.figure(figsize=(12, 6))
    plt.plot(years, apples, 's-b')
    plt.plot(years, oranges, 'o--r')
    plt.xlabel('Years')
    plt.ylabel('Yield tons per hectare')
    plt.title('Crop yield in kanto')
    plt.legend(['Apple', 'Orange'])
    plt.show()