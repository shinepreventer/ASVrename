import pandas as pd
from Bio import SeqIO, Phylo
import tkinter as tk
from tkinter import filedialog

def write_single_line_fasta(records, output_file):
    with open(output_file, 'w') as f:
        for record in records:
            f.write(f'>{record.id}\n')
            f.write(f'{record.seq}\n')

def rename_asv_ids(asv_table_file, rep_seq_file, tree_file, output_asv_table_file, output_rep_seq_file, output_tree_file):
    # 读取ASV表
    asv_table = pd.read_csv(asv_table_file, sep='\t', index_col=0)

    # 创建新的ASV号索引映射
    new_index = {}
    for i, asv_id in enumerate(asv_table.index):
        new_index[asv_id] = f'ASV{i+1}'

    # 重命名ASV表的行
    asv_table = asv_table.rename(index=new_index)

    # 读取代表序列文件
    rep_seq = SeqIO.parse(rep_seq_file, 'fasta')

    # 重命名代表序列文件中的ASV号
    new_rep_seq = []
    for record in rep_seq:
        record.id = new_index[record.id]
        record.description = ''
        new_rep_seq.append(record)

    # 读取树文件
    tree = Phylo.read(tree_file, 'newick')

    # 重命名树文件中的ASV号
    for clade in tree.find_clades():
        if clade.name in new_index:
            clade.name = new_index[clade.name]

    # 将更新后的ASV表、代表序列文件和树文件保存到输出文件
    asv_table.to_csv(output_asv_table_file, sep='\t')
    write_single_line_fasta(new_rep_seq, output_rep_seq_file)
    Phylo.write(tree, output_tree_file, 'newick')

def select_file():
    filename = filedialog.askopenfilename()
    return filename

def select_directory():
    directory = filedialog.askdirectory()
    return directory

def main():
    root = tk.Tk()
    asv_table_file = tk.StringVar()
    rep_seq_file = tk.StringVar()
    tree_file = tk.StringVar()
    output_dir = tk.StringVar()

    asv_table_file_button = tk.Button(root, text="选择ASV表文件", command=lambda: asv_table_file.set(select_file()))
    asv_table_file_button.pack()
    rep_seq_file_button = tk.Button(root, text="选择代表序列文件", command=lambda: rep_seq_file.set(select_file()))
    rep_seq_file_button.pack()
    tree_file_button = tk.Button(root, text="选择树文件", command=lambda: tree_file.set(select_file()))
    tree_file_button.pack()
    output_dir_button = tk.Button(root, text="选择输出文件夹", command=lambda: output_dir.set(select_directory()))
    output_dir_button.pack()
    run_button = tk.Button(root, text="运行", command=lambda: rename_asv_ids(asv_table_file.get(), rep_seq_file.get(), tree_file.get(), f"{output_dir.get()}/output_asv_table.tsv", f"{output_dir.get()}/output_rep_seq.fasta", f"{output_dir.get()}/output_tree.nwk"))
    run_button.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
