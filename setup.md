
# Setup Instructions for Image Comparison

## Windows:

1) Install Python 3.7.3: https://www.python.org/downloads/release/python-373/
2) Install Latest Pip. Open Powershell and run the following command: `py -m pip install --upgrade pip`
3) Install VirtualEnv. Run the following in Powershell: `py -m pip install --user virtualenv`
4) Open powershell as adminstrator and run the following: `Set-ExecutionPolicy RemoteSigned`
5) Run the following in Powershell: `py -m pip install numpy scipy Pillow imageio opencv-python==3.4.2.17 opencv-contrib-python==3.4.2.17`
6) To execute the image comparison, run the python script as follows, `py main.py {path_to_input_csv_file}` if you would like to provide a path to the output csv file you can execute the script like this, `py main.py {path_to_input_csv_file} {path_to_output_csv_file}`
