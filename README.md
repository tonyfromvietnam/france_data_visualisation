<!-- ABOUT THE PROJECT -->
## About The Project

This project illustrates my knowledge about the basic data visualisation in Matplotlib; using additional libraries, including pandas & numpy.
This project contains:
* A python file: plot.py. This file demonstrates the use of libraries in visualising the needed graph. This graph is about the location of big cities, in which the population is above 5000 in France in 1999.
* A CSV file: france.csv. This file is the data file, which I found and download from Kaggle (a sharing data site). [Link](https://www.kaggle.com/datasets/arnaud58/french-cities-population-lat-long-1999) to the dataset.
* Two png files: Route_of_the_1999_Tour_de_France.png & France_Visualisation.png. The file France_Visualisation.png is the resulting graph from the python code, compared to the real locations of cities in France (by using the map of the 1999 Tour de France).
This project aims to get used to the additional libraries, which are useful in data manipulating & data visualisation: matplotlib, pandas, numpy.

<!-- GETTING STARTED -->
## Getting Started

You should have installed a Python IDE, in which you could edit & writing codes. There are multiple Python IDEs, or even text editor.
**If you are using a TextEditor, you would have to run by terminal**

### Prerequisites

Because of that, I would recommend using a IDE, in order for additional support; some of the IDEs I would recommend:
1. Pycharm
2. Visual Studio Code
3. Spyder (via Anaconda Navigator)
The information of download I will let it down here:
[Pycharm](https://www.jetbrains.com/pycharm/download)
[Visual Studio Code](https://code.visualstudio.com/download)
[Anaconda Navigator](https://www.anaconda.com/products/distribution)

### Installation

You should install the recommended libraries, including matplotlib, pandas & numpy.
* maplotlib
  ```sh
    python -m pip install -U pip
    python -m pip install -U matplotlib
  ```
  or
  ```sh
    python -m pip install -U pip
    pip install matplotlib
  ```
  
* numpy
  ```sh
    python -m pip install -U numpy
  ```
  or
  ```sh
    pip install numpy
  ```

* pandas
  ```sh
    python -m pip install -U pandas
  ```
  or
  ```sh
    pip install pandas
  ```

After that, you will have to import into your python file by:
  ```sh
    import maplotlib.pyplot as plt
    import numpy as np
    import pandas as pd
  ```

<!-- USAGE EXAMPLES -->
## Usage

You can see and have an overview how those libaries are used in Data Science.
* Matplotlib is a library in drawing graphs.
* Numpy is a library in manipulating numeric in Python.
* Pandas is a library in dealing with dataframe in Python.

Through the codes in the project, you can have a view how I'm dealing with the data from an open-source dataset.
Here are the steps that I used to approach a dataset so far:
1. Have an overview on what information in this dataset can be used.
2. Evaluate the value of the information
3. Extract the information needed to visualisation.
4. Start graphing and adding details to the graph.

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


<!-- CONTACT -->
## Contact

Duy Chinh Dinh - [@Linkedin](https://www.linkedin.com/in/duychinhdinh/) - chinh.dinhduy03@gmail.com