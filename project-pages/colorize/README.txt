For main.ipynb, you can specify any file you want to run the code on by setting the "imname" variable:
Example: imname = '../../proj1/data/harvesters.tif'
Then, you can experiment with the render_image function, which takes four parameters:
    method:
        0 - L2 Norm
        1 - NNC
        2 - SSD
    approach:
        True - Naive
        False - Pyramid
    gradient:
        True - Apply gradient for edge detection
        False - Do not apply gradient for edge detection
    crop:
        True - Apply automatic cropping
        False - Do not apply automatic cropping

For main.py, you can change the variables names, imname, extension, and output_dir to run the code. This Python file is used to run the code and save files to a specific path.
    Description of variables:
        - names: Names of the files that you want to run.
        - imname: Path to the data directory.
        - extension: File extension, either jpg or tif.
        - output_dir: Output path where the files will be saved.
    What it does: Assuming you set these variables correctly, it iterates over the names and saves images using different methods: running SSD, SSD with cropping, SSD with edge detection, and SSD with both cropping and edge detection.