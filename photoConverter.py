import os, subprocess        
from sys import platform
from optparse import OptionParser

directory = '.'

def convert_formats_to_formats(input, output):
    input_format_string = "." + input.strip().replace('.', '')
    output_format_string = "." + output.strip().replace('.', '')

    if not os.path.exists("output"):
        os.mkdir("output")

    for filename in os.listdir(directory):
        if not filename.lower().endswith(input_format_string):
            continue

        print('Converting %s...' % os.path.join(directory, filename))
        
        magick_command = ""
        if platform == "linux" or platform == "linux2":
            magick_command = "magick"
        elif platform == "darwin":
             magick_command = "magick"
        elif platform == "win32":
            magick_command = "magick.exe"

        subprocess.run([magick_command, "%s" % filename, "output/%s" % (filename[0:-5] + output_format_string)])
        continue

if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option("-i", "--input", action="store", dest="input_format", help="Specify conversion format. Default is heic", default="heic")
    parser.add_option("-o", "--output", action="store", dest="output_format", help="Specify conversion format. Default is jpg", default="jpg")
    (options, args) = parser.parse_args()

    convert_formats_to_formats(input=options.input_format, output=options.output_format)