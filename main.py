from parse_analyze import *
import sys

if (len(sys.argv) == 2):
    parse_analyze_write_back(sys.argv[1])
elif (len(sys.argv) == 3):
    parse_analyze_write_back(sys.argv[1], sys.argv[2])
else:
    print("""
    Image Comparison Program using SURF 
        Usage:
            `python3 main.py {input_csv_path}`
                if no second argument is passed the output will be named output.csv                and be in the current folder
            `python3 main.py {input_csv_path} {output_csv_name}`
            """)
