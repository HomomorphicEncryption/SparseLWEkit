import pandas as pd
from functools import reduce

if __name__ == "__main__":
       toolnames = ['lattice_estimator']
       column_titles = {'lattice_estimator': "[Lattice Estimator](https://github.com/malb/lattice-estimator)"}

       all_tools_summary = pd.DataFrame()

       for toolname in toolnames:
              # load the estimates
              all_estimates_db = pd.read_csv(f'src/data/{toolname}_estimates.csv')

              # if we add a new metadata column, need to add it here so that it doesn't get treated as a security estimate
              metadata_columns = ['ID', r'$\log_2(n)$', r'$\log_2(q)$', 'σ', '$h$', 'machine_info', 'tool_commit', 'estimation_time']
              security_columns = [col for col in all_estimates_db.columns if col not in metadata_columns]

              # keep only the security estimates, and convert to numeric for comparison
              security_db = all_estimates_db[security_columns].apply(pd.to_numeric, errors='coerce')

              # for each row keep the lowest security value and the associated attack
              le_summary = pd.concat([pd.DataFrame(security_db.min(axis="columns"), columns=['lowest_sec']),pd.DataFrame(security_db.idxmin(axis="columns"), columns=['best_attack'])], axis=1)

              # convert the summary to a string, and add the toolname as a column title
              le_summary_str = le_summary.apply(lambda x: f"{x['lowest_sec']} bits ({x['best_attack']})", axis=1)
              le_summary_str = pd.DataFrame(le_summary_str.tolist(), columns=[column_titles[toolname]])

              # add the parameter set IDs 
              le_summary_str = pd.concat([all_estimates_db['ID'],le_summary_str],axis=1)

              # sorting rows by ID number
              le_summary_str.sort_values(by=['ID'], inplace=True)

              # join to master table
              if all_tools_summary.empty:
                     all_tools_summary = le_summary_str
              else:
                     all_tools_summary = all_tools_summary.merge(le_summary_str, on='ID')

       print(all_tools_summary.to_markdown(index=False))

