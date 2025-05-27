import pandas as pd

# load the database
attack_db = pd.read_csv('src/attack_db.csv')  

# sort rows by chronological order for the attack's year of publication and then by alphabetical order for the authors
attack_db.sort_values(by=['Year','Authors'], inplace=True)

# build the attack's display name in the format {Venue}:{Authors}{YY}{Note} with an hyperlink to the paper
def gen_attack_display_name(db):
    display_names = []
    for index, row in db.iterrows():
        row_note = '' if row['Note']=='empty' else row['Note']
        display_names.append(
            '['+
            row['Venue']+
            ':'+
            row['Authors']+
            str(row['Year']%100).zfill(2)+
            ']('+
            row['Paper']+
            ')'+
            row_note
            )
    return display_names
attack_display_names_list = gen_attack_display_name(attack_db[['Venue', 'Authors' ,'Year' ,'Paper' , 'Note']])

# replace the Venue, Authors, Year, Paper and Note column with the new column with the display names
tool_list = ['[Lattice estimator](https://github.com/malb/lattice-estimator)', '[SparseLWE-estimator](https://github.com/yonghaason/SparseLWE-estimator)', '[LWE-benchmarking](https://github.com/facebookresearch/LWE-benchmarking)', '[PrimalMeetLWE](https://github.com/yonghaason/PrimalMeetLWE/tree/main/estimator)']
attack_with_display_names_db = attack_db[tool_list]
attack_with_display_names_db.insert(0, 'Attack', attack_display_names_list)

# sort columns by number of check marks (the least on the right)
column_sorting_dict = {column_name : sum(list(map(lambda x: (x.find('✅')) >= 0 ,attack_with_display_names_db[column_name].tolist()))) for column_name in attack_with_display_names_db.columns[1:]}
column_sorting_dict.update({'Attack' : attack_db.shape[0] + 1})
ready_to_print_db = attack_with_display_names_db.sort_index(axis=1, ascending=False, key=lambda x: x.map(column_sorting_dict))

# print the markdown table
print(ready_to_print_db.to_markdown(index=False))
