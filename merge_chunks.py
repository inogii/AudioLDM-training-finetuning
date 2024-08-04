import requests
import os

def combine_files(output_file, input_files):
    with open(output_file, 'wb') as output:
        for file in input_files:
            with open(file, 'rb') as f:
                output.write(f.read())

def main():
    # Output directory for downloaded chunks
    output_dir = "data/dataset/inogii_audiocaps_compressed"

    # List of downloaded chunks
    parts = sorted([os.path.join(output_dir, f) for f in os.listdir(output_dir) if f.startswith("dataset.zip.part")])

    # Output file
    output_file = "data/dataset/reassembled_dataset.zip"

    # Combine the chunks
    combine_files(output_file, parts)

if __name__ == "__main__":
    main()
