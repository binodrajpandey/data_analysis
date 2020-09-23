import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def main():
    barChart()


def darkGrid():
    # sns.set_style("whitegrid")
    sns.set_style("darkgrid")
    years = range(2000, 2012)
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


def scattorPlot():
    sns.set_style("darkgrid")
    flowers_df = sns.load_dataset("iris")
    print(flowers_df)
    species = flowers_df.species.unique()
    print(species)
    # See what happen with plt.plot(flowers_df.sepal_length,flowers_df.sepal_width)
    # no need to set xlabel and ylabel
    sns.scatterplot(flowers_df.sepal_length, flowers_df.sepal_width)
    plt.show()


def scattorPlotWithHue():
    sns.set_style("darkgrid")
    flowers_df = sns.load_dataset("iris")
    print(flowers_df)
    species = flowers_df.species.unique()
    print(species)
    # if we set s (size) size of the dot will increase.
    # sns.scatterplot(flowers_df.sepal_length, flowers_df.sepal_width, hue=flowers_df.species, s=100)
    # or
    sns.scatterplot('sepal_length', 'sepal_width', hue='species', s=100, data=flowers_df)
    plt.show()


def histogramPlot():
    sns.set_style("darkgrid")
    flowers_df = sns.load_dataset("iris")
    sns.histplot(flowers_df.sepal_width)
    plt.show()


def histogramPlotWithCustomizeBinSize():
    sns.set_style("darkgrid")
    flowers_df = sns.load_dataset("iris")
    # sns.histplot(flowers_df.sepal_width, bins=5)
    sns.histplot(flowers_df.sepal_width, bins=np.arange(2, 5, 0.25))
    # sns.histplot(flowers_df.sepal_width, bins=[1,3,4,4.5])
    plt.show()


def multipleHistogram():
    sns.set_style("darkgrid")
    flowers_df = sns.load_dataset("iris")
    setosa_df = flowers_df[flowers_df.species == 'setosa']
    versicolor_df = flowers_df[flowers_df.species == 'versicolor']
    verginica_df = flowers_df[flowers_df.species == 'virginica']
    print(flowers_df)
    # plt.hist(setosa_df.sepal_width, alpha =0.4)
    # plt.hist(versicolor_df.sepal_width, alpha = 0.4)
    # plt.hist(verginica_df.sepal_width, alpha = 0.4)
    plt.hist([setosa_df.sepal_width, versicolor_df.sepal_width, verginica_df.sepal_width], bins=np.arange(2, 5, 0.25),
             stacked=True)
    plt.legend(['Setosa', 'Versicolor', 'Virginica'])
    plt.show()


def barChart():
    years = range(2000, 2006)
    apples = [0.35, 0.6, 0.9, 0.8, 0.65, 0.8]
    oranges = [0.4, 0.8, 0.9, 0.7, 0.6, 0.8]
    plt.bar(years, apples)
    plt.bar(years, oranges, bottom=apples)
    plt.legend(['apples', 'oranges'])
    plt.show()


if __name__ == '__main__':
    main()
