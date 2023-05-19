import pandas as pd
from Bio import SeqIO

def write_single_line_fasta(records, output_file):
    with open(output_file, 'w') as f:
        for record in records:
            f.write(f'>{record.id}\n')
            f.write(f'{record.seq}\n')

def rename_asv_ids(asv_table_file, rep_seq_file, output_asv_table_file, output_rep_seq_file):
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

    # 将更新后的ASV表和代表序列文件保存到输出文件
    asv_table.to_csv(output_asv_table_file, sep='\t')
    write_single_line_fasta(new_rep_seq, output_rep_seq_file)

# 设置输入和输出文件的路径
asv_table_file = '/media/wzy/work/pytest/otu_table.txt'
rep_seq_file = '/media/wzy/work/pytest/dna-sequences.fasta'
output_asv_table_file = '/media/wzy/work/pytest/output_asv_table.tsv'
output_rep_seq_file = '/media/wzy/work/pytest/output_rep_seq.fasta'

# 调用rename_asv_ids()函数
rename_asv_ids(asv_table_file, rep_seq_file, output_asv_table_file, output_rep_seq_file)
