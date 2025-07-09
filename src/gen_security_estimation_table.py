import pandas as pd

#####################
# Lattice Estimator #
#####################

# name of the tool
tool_name = 'lattice_estimator'

# load the database
le_db = pd.read_csv('src/data/'+tool_name+'.csv')

# keep only the security estimations
sec_db = le_db[['dual_hybrid_sec','dual_sec', 
       'bdd_mitm_hybrid_sec',  'bdd_hybrid_sec',
        'bdd_sec', 'usvp_sec', 
       'bkw_sec',  'mitm_simple_sec',
       'dual_hybrid_Alb17_sec',  'CHHS19_mitm_sec']]


# for each row keep the lowest security value and the associated attack
le_summary = pd.concat([pd.DataFrame(sec_db.min(axis="columns"), columns=['lowest_sec']),pd.DataFrame(sec_db.idxmin(axis="columns"), columns=['best_attack'])], axis=1)

# add and the CPU time and concat into a single string
le_summary = pd.concat([le_summary,le_db['cpu time']],axis=1)
le_summary_str = le_summary.apply(lambda x: str(x['lowest_sec']) + ' bits ('+x['best_attack']+') '+x['cpu time'], axis=1)
le_summary_str = pd.DataFrame(le_summary_str.tolist(), columns=["[Lattice estimator](https://github.com/malb/lattice-estimator)"])

# add the parameter set IDs 
le_summary_str = pd.concat([le_db['ID'],le_summary_str],axis=1)

# sorting rows by Hamming weight
le_summary_str.sort_values(by=['ID'], inplace=True)

# print the markdown table
print(le_summary_str.to_markdown(index=False))