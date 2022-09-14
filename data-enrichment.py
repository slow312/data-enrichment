import pandas as pd

sparcs_df = pd.read_csv("Hospital_Inpatient_Discharges__SPARCS_De-Identified___2015.csv")

# clean up column names
sparcs_df.columns = sparcs_df.columns.str.replace('[^A-Za-z0-9]+', '_')
sparcs_df.columns = sparcs_df.columns.str.lower()

# get rows where 'zip_code_3_digits' is not NA
sparcs_df = sparcs_df[sparcs_df['zip_code_3_digits'].notna()]

atlas_df = pd.read_csv("NY_2019_ADI_9 Digit Zip Code_v3.1.txt", sep = ",")

# clean up column names
atlas_df.columns = atlas_df.columns.str.replace('[^A-Za-z0-9]+', '_')
atlas_df.columns = atlas_df.columns.str.lower()

# drop unwanted columns
atlas_df = atlas_df[['zipid', 'adi_natrank', 'adi_staternk']]

# get 3 digit zip code
atlas_df['zipid'] = atlas_df['zipid'].str[1:4] 

# get rid of rows with NA values
atlas_df = atlas_df.dropna()

sparcs_df = sparcs_df.merge(atlas_df, left_on='zip_code_3_digits', right_on = 'zipid')
sparcs_df.head()