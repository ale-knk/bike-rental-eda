# Bike Rental EDA

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Status](https://img.shields.io/badge/status-Under%20Development-yellow.svg)
![Python Version](https://img.shields.io/badge/python-3.12%2B-blue.svg)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?logo=docker&logoColor=white)
![Git](https://img.shields.io/badge/git-F05032.svg?logo=git&logoColor=white)


## Introduction

Welcome to my professional portfolio project in the fields of Data Science and Software Engineering. This repository is dedicated to developing a robust interface that facilitates Exploratory Data Analysis (EDA) on bike rental system data in an urban environment. The primary objective is to provide users with a versatile toolset that enables them to uncover meaningful insights, patterns, and trends within the dataset, thereby informing strategic decision-making and optimizing bike rental operations.

Rather than focusing directly on performing EDA, this project emphasizes creating an intuitive and efficient software interface that streamlines the data exploration process. By leveraging various EDA techniques through this interface, users can easily interact with the data, generate comprehensive visualizations, and conduct statistical analyses without the need for extensive coding or technical expertise.

This project lays the foundation for empowering data analysts and stakeholders to perform in-depth investigations into bike rental dynamics, facilitating informed decisions and fostering data-driven strategies for enhancing bike-sharing services.

## Installation

1. **Clone the repository**

    ```bash
    git clone https://github.com/yourusername/bike-rental-eda.git
    cd bike-rental-eda
    ```

2. **Create a virtual environment**
    For example, using conda:

    ```bash
    conda create -n your_env_name python==3.12
    conda activate your_env_name
    ```

3. **Install the package**
    In order to install the package (and all the deppendencies):

    ```bash
    pip install .
    ```

## Usage

This package offers a flexible interface for performing Exploratory Data Analysis (EDA) on bike rental system data through both programmatic plotters and an interactive Dash application.

Within the `pybike/plots` directory, various Python modules define classes dedicated to creating different types of plots such as boxplots, lineplots, and heatmaps. These plotter classes are designed to support multiple filtering options, enhancing interactivity and allowing for customized data exploration.

For comprehensive examples and detailed usage, please refer to the [Plotters Notebook](./docs/plotters.ipynb).


In addition, to facilitate a more user-friendly experience, a Dash application has been developed. This web-based interface leverages the plotter classes to allow users to create and manipulate various plots interactively. While the current version provides essential functionalities, there are aspects that could be enhanced in terms of UI/UX design. However, improving the user interface is not the primary focus of this project.


In order to run the Dash app:

*Note: The following instructions are provisional and subject to change as the app development progresses.*

1. **Ensure All Dependencies Are Installed**

    Make sure you have all necessary dependencies installed, which can be done during the package installation step.

2. **Launch the Dash Application**

    ```bash
    # Navigate to the project directory if not already there
    cd bike-rental-demand-pred

    # Run the Dash app
    python pybike/app.py
    ```

3. **Access the App in Your Browser**

    Once the app is running, open your web browser and navigate to `http://localhost:8050` to access the interface.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

-   **Your Name** - [rb.jandro@gmail.com](mailto:rb.jandro@gmail.com)
-   **GitHub**: [yourusername](https://github.com/yourusername)
