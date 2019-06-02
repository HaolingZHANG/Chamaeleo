"""
Name: Symmetrical testing for DDC

Coder: HaoLing ZHANG (BGI-Research)[V1]

Current Version: 1

Function(s): The Feasibility of Testing the Whole Process of DDC
"""


import methods.double_double as ddc

import utils.model_saver as saver
import utils.data_handle as data_handle


read_file_path = "..\\..\\test\\test_files\\founding ceremony.mp4"
write_file_path = "..\\..\\test\\generated_files\\target.mp4"

dna_path = "..\\..\\test\\generated_files\\target.dna"

model_path = "..\\..\\test\\generated_files\\ddc.pkl"

if __name__ == '__main__':
    tool = ddc.DDC()
    input_matrix, size = data_handle.read_binary_from_all(read_file_path)
    dna_motifs = tool.encode(input_matrix, size)
    data_handle.write_dna_file(dna_path, dna_motifs)
    saver.save_model(model_path, tool)

    tool = saver.load_model(model_path)
    dna_motifs = data_handle.read_dna_file(dna_path)
    output_matrix = tool.decode(dna_motifs)
    data_handle.write_all_from_binary(write_file_path, output_matrix, tool.file_size)