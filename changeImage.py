#!/usr/bin/env python3

"""This script loads .tiff files from a target directory, reformats and
resizes them, then saves them to a destination directory."""

import os
from PIL import Image

def get_files(directory):
    """Return list of all files in a directory."""
    return os.listdir(directory)

def handle_image(filename, source_dir="~/supplier-data/images", target_dir="~/supplier-data/images"):
    """Manage opening, modifying, and saving of a single image."""
    source_name = os.path.join(source_dir, filename)
    print("source:", source_name)
    destination_name = os.path.join(target_dir, filename)
    print("destination name:", destination_name)
    with Image.open(source_name) as current_image:
        current_image = current_image.convert('RGB').resize((600,400))
        print("Image:", current_image)
        f, e = os.path.splitext(destination_name)
        outfile = f + ".jpeg"
        print("outfile:", outfile)
        if not os.path.isdir(target_dir):
            os.mkdir(target_dir)
        current_image.save(outfile, "JPEG")

#handle_image("mango.tiff", "supplier-data/images", "supplier-data/target")
