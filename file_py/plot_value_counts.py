class PlotValueCounts:
    """
    This class generates bar plots to visualize the count of values in a specified column of a DataFrame.
    Each unique value in the specified column is plotted separately.
    
    Parameters:
    - df: DataFrame: The DataFrame containing the data to be plotted.
    
    Usage:
    1. Instantiate the class.
    2. Call the 'plot_value_counts_per_unique' method with the DataFrame containing the data.
    
    Example:
    ```
    # Instantiate the class
    vcp = PlotValueCounts()
    
    # Plot the value counts for a DataFrame df
    vcp.plot_value_counts_per_unique(df)
    ```

    """
    
    import matplotlib.pyplot as plt
    import math

    def plot_value_counts_per_unique(df):
        """
        Plot the count of values for each unique value in a specified column of the DataFrame.

        Parameters:
        - df: DataFrame: The DataFrame containing the data to be plotted.
        """

        unique_col = 'RuleAnnotation.mitre_attack.id'
        count_col = 'corrisponde_ad_attacco'
        cols = 5  # Numero di colonne desiderato nella griglia dei subplot
        color = ['#5cabbf', '#a15cbf']  # Colori per le barre
        xlabel = ''  # Etichetta per l'asse x
        ylabel = 'N. record'  # Etichetta per l'asse y
        xtick_labels = ['Non attacco', 'Attacco']  # Etichette per i tick dell'asse x
        figsize_multiplier = (5, 4)  # Multiplicatore per la dimensione della figura (larghezza, altezza)

        # Troviamo i valori unici della colonna unique_col
        unique_values = df[unique_col].unique()

        # Impostiamo il numero di subplot (una per ciascun valore unico di unique_col)
        num_plots = len(unique_values)

        # Determiniamo il numero di righe e colonne per la griglia
        rows = PlotValueCounts.math.ceil(num_plots / cols)  # Calcola il numero di righe necessario

        # Creiamo i subplot
        fig, axes = PlotValueCounts.plt.subplots(rows, cols, figsize=(figsize_multiplier[0] * cols, figsize_multiplier[1] * rows))

        # Se c'è solo un valore unico, axes non è un array bidimensionale, quindi lo convertiamo
        if num_plots == 1:
            axes = [[axes]]
        elif rows == 1:
            axes = [axes]

        # Cicliamo su ciascun valore unico di unique_col e plottiamo i dati
        for ax, value in zip(axes.flat, unique_values):
            # Filtriamo il DataFrame per il valore corrente di unique_col
            filtered_df = df[df[unique_col] == value]

            # Contiamo i valori di count_col (0 e 1)
            count_values = filtered_df[count_col].value_counts().sort_index()

            # Creiamo il grafico sul subplot corrente
            count_values.plot(kind='bar', ax=ax, color=color)

            # Aggiungiamo etichette e titolo
            ax.set_xlabel(xlabel)
            ax.set_ylabel(ylabel)
            ax.set_title(value)
            ax.set_xticks([0, 1])
            ax.set_xticklabels(xtick_labels, rotation='horizontal')

        # Rimuoviamo gli assi vuoti
        for i in range(num_plots, rows * cols):
            fig.delaxes(axes.flat[i])

        # Aggiustiamo il layout
        PlotValueCounts.plt.tight_layout()
        PlotValueCounts.plt.show()