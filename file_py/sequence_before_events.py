from .lib import *

class SequenceBeforeEvents:
    def visualizza_sequenze_precedenti(dataset, regola_scelta, n):
        """
        Visualizza i n eventi precedenti l'attivazione di una specifica regola nel dataset.

        Parametri:
        dataset (pd.DataFrame): Il dataset contenente i log.
        regola_scelta (str): La regola per cui visualizzare gli eventi precedenti.
        n (int): Il numero di eventi precedenti da considerare.

        Ritorna:
        None
        """
        # Filtraggio dei dati per la regola scelta
        df_filtered = dataset[dataset['RuleAnnotation_mitre.attack_id'] == regola_scelta]

        # Ordinamento per tempo
        df_filtered = df_filtered.sort_values(by='_time')

        # Lista per memorizzare i dati delle sequenze
        sequences = []

        for i, row in df_filtered.iterrows():
            # Trova l'indice dell'evento attuale
            current_index = dataset.index.get_loc(i)
            # Controlla che ci siano abbastanza eventi precedenti
            if current_index >= n:
                previous_events = dataset.iloc[current_index - n:current_index]
                sequences.append(previous_events)

        # Concatenare tutte le sequenze in un unico DataFrame
        if sequences:
            sequences_df = pd.concat(sequences)
        else:
            print("Non ci sono abbastanza dati precedenti per la regola scelta.")
            return

        # Visualizzazione dei dati
        plt.figure(figsize=(12, 8))

        for col in sequences_df.columns:
            if col not in ['_time', 'RuleAnnotation_mitre.attack_id']:  # Escludiamo le colonne non numeriche per il grafico
                plt.plot(sequences_df['_time'], sequences_df[col], marker='o', label=col)

        plt.xlabel('Time')
        plt.ylabel('Value')
        plt.title(f'Valori delle colonne degli eventi precedenti la regola {regola_scelta}')
        plt.legend()
        plt.show()