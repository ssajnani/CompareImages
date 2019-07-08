
# Setup Instructions for Image Comparison

## Windows:

1) Install Python 3.7.3 by downloading and running the executable from here: https://www.python.org/downloads/release/python-373/
2) Install Latest Pip. Open Powershell and run the following command: `py -m pip install --upgrade pip`
3) Run the following in Powershell: `py -m pip install numpy scipy Pillow imageio opencv-python==3.4.2.17 opencv-contrib-python==3.4.2.17`
4) Install git (https://git-scm.com/download/win) and clone the repository by running the following in Powershell: `git clone git@github.com:ssajnani/CompareImages.git`
5) To execute the image comparison, change directories to the root directory of this project, run the python script as follows, `py main.py {path_to_input_csv_file}` if you would like to provide a path to the output csv file you can execute the script like this, `py main.py {path_to_input_csv_file} {path_to_output_csv_file}`

## MacOS:

1) Install Python 3.7.3 by downloading and running the executable from here: https://www.python.org/downloads/release/python-373/
2) Install Latest Pip. Open Terminal and run the following command: `python3 -m pip install --user --upgrade pip`
3) Run the following in Terminal: `pip3 install numpy scipy Pillow imageio opencv-python==3.4.2.17 opencv-contrib-python==3.4.2.17`
4) Install git (https://git-scm.com/download/mac) and clone the git repository by running the following in Terminal: `git clone git@github.com:ssajnani/CompareImages.git`
5) To execute the image comparison, in Terminal, change directories to the root directory of this project, run the python script as follows, `python3 main.py {path_to_input_csv_file}` if you would like to provide a path to the output csv file you can execute the script like this, `python3 main.py {path_to_input_csv_file} {path_to_output_csv_file}`
