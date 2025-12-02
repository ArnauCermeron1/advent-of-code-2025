# Advent of Code Utility (Common) Functions
def parse_input(file_path):
    with open(file_path, 'r') as file:
        return file.read().strip().split('\n')
    
def parse_input_commas(file_path):
    with open(file_path, 'r') as file:
        return file.read().strip().split(',')