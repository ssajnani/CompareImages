from analysis.compare import *
import csv, time

def parse_analyze_write_back(csv_file_path, output_file_path="output.csv"):
    '''
    Reads two image columns from input csv row by row, 
    compares the two images given by their paths on each row to get a similarity index,
    measures the time taken to calculate the similarity index, and outputs 
    the image paths, similarity index, and time taken into an output csv.
    @param csv_file_path string
    @param output_file_path string  
    '''
    try:
        #Open the output file and setup it's header
        with open(output_file_path, mode='w') as employee_file:
            output_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            output_writer.writerow(['image1', 'image2', 'similar', 'elapsed'])
            #Open the input csv file
            with open(csv_file_path) as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                line_count = 0
                for row in csv_reader:
                    #Skip the header of the input csv file
                    if line_count == 0:
                        line_count += 1
                    else:
                        #Start of image analysis
                        start_time = time.time()
                        #Generate a similarity index
                        similarity_index = compare_two_images(row[0], row[1])
                        #End of image analysis
                        end_time = time.time()
                        elapsed_time = end_time - start_time
                        #Write to output csv file
                        output_writer.writerow([row[0], row[1], "{:.2f}".format(similarity_index), "{:.3f}".format(elapsed_time)])
                        line_count += 1
                    print(f'Processed {line_count} lines.')
        return True
    except Exception as e:
        print('Error: %s' % e)
        return False