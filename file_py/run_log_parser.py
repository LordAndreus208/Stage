class RunLogParser:
    """A utility class for parsing run logs and processing attacks.

    This class provides static methods to parse a run log CSV file
    and process attacks based on the log data.

    Attributes:
        None

    Methods:
        parse_run_log(file_path): Parses a run log CSV file and returns a list of attacks.
        process_attacks(file_path, df): Processes attacks and updates a DataFrame accordingly.
    """
    import pandas as pd
    import csv

    @staticmethod
    def parse_run_log(file_path):
        """Parses a run log CSV file and returns a list of attacks.

        Args:
            file_path (str): The path to the run log CSV file.

        Returns:
            list: A list of dictionaries containing attack information.
        """
        attacks = []
        with open(file_path, newline='') as csvfile:
            reader = RunLogParser.csv.DictReader(csvfile, fieldnames=[field.lower().replace(' ', '_') for field in csvfile.readline().strip().split(',')])
            for row in reader:
                attack = {
                    'codice_attacco': row['codice_attacco'],
                    'data_inizio': row['data_inizio_attacco'],
                    'data_fine': row['data_fine_attacco'],
                }
                attack['data_inizio'] = RunLogParser.pd.to_datetime(attack['data_inizio'])
                attack['data_fine'] = RunLogParser.pd.to_datetime(attack['data_fine'])
                attacks.append(attack)
        return attacks

    @staticmethod
    def process_attacks(file_path, df):
        """Processes attacks and updates a DataFrame accordingly.

        Args:
            file_path (str): The path to the run log CSV file.
            df (pandas.DataFrame): The DataFrame to be updated.

        Returns:
            pandas.DataFrame: The updated DataFrame.
        """
        attacks = RunLogParser.parse_run_log(file_path)
        df_result = df.copy()
        df_result['corrisponde_ad_attacco'] = 0
        
        for attack in attacks:
            codice_attacco = attack['codice_attacco']
            data_inizio = attack['data_inizio']
            data_fine = attack['data_fine']
            
            mask = (df_result['_time'] >= data_inizio) & (df_result['_time'] <= data_fine)
            df_result.loc[mask, 'corrisponde_ad_attacco'] = 1
            df_result.loc[mask, 'codice_attacco'] = codice_attacco
        
        df_result.drop(columns=['codice_attacco'], inplace=True)
        
        return df_result