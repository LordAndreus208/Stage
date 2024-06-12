class Plots:
    """
    The Plots class provides various methods to visualize data related to attack events using Matplotlib.
    It includes methods to plot pie charts, bar distributions, top MITRE ATT&CK IDs, and value counts 
    for unique values in specified columns of a DataFrame. The class is designed to help analyze and 
    display data in a clear and meaningful way, facilitating the understanding of attack patterns and distributions.

    Methods:
        plot_cake_attack(df):
            Generates and displays a pie chart showing the percentage of events that correspond to attacks.
        
        plot_distributions(df):
            Generates and displays subplots of distributions for attack and non-attack events based on specified columns.
        
        plot_top_10_mitre_id(df):
            Generates and displays subplots of the top 10 MITRE ATT&CK IDs in overall frequency and for attacks.
        
        plot_value_counts_per_unique(df):
            Plots the count of values for each unique value in a specified column of the DataFrame.
    """

    import matplotlib.pyplot as plt
    import math

    def plot_cake_attack(df):
        """
        Method to generate and display the pie chart of the percentage of events that correspond to attacks.

        Args:
            df (DataFrame): The DataFrame containing the event data.

        Returns:
            None
        """
        is_attack = df['corrisponde_ad_attacco'] == 1  # Filter attacks
        attack_percentage = is_attack.mean() * 100
        Plots.plt.figure(figsize=(6, 6))
        Plots.plt.pie([attack_percentage, 100 - attack_percentage], labels=['Attacks', 'Non-Attacks'], autopct='%1.1f%%', startangle=140)
        Plots.plt.title('Percentage of Events that Correspond to Attacks')
        Plots.plt.show()

    def plot_distributions(df):
        """
        Method to generate and display subplots of distributions for attack and non-attack events.

        Args:
            df (DataFrame): The DataFrame containing the event data.

        Returns:
            None
        """
        is_attack = df['corrisponde_ad_attacco'] == 1
        fig, axes = Plots.plt.subplots(3, 2, figsize=(12, 9))  # 3 rows, 2 columns

        for i, column in enumerate(['severity_id', 'tag', 'EventType']):

            # Attack distribution
            attack_values = df[is_attack][column].value_counts()
            attack_values.plot(kind='bar', ax=axes[i, 0], color='red')
            axes[i, 0].set_title(f'Distribution of {column} (Attacks)')
            axes[i, 0].tick_params(axis='x', rotation=0)

            # Add values on top of the bars for attack distribution
            for p in axes[i, 0].patches:
                height = p.get_height()
                if height > 100:  # Adjust this threshold as needed
                    axes[i, 0].annotate(str(height), (p.get_x() + p.get_width() / 2., height - 150), 
                                        ha='center', va='bottom', color='white')
                else:
                    axes[i, 0].annotate(str(height), (p.get_x() + p.get_width() / 2., height + 15), 
                                        ha='center', va='bottom', color='black')
                    
            # Non-Attack Distribution
            non_attack_values = df[~is_attack][column].value_counts()
            non_attack_values.plot(kind='bar', ax=axes[i, 1], color='blue')  # Same column, different row
            axes[i, 1].set_title(f'Distribution of {column} (Non-Attacks)')
            axes[i, 1].tick_params(axis='x', rotation=0)

            # Add values on top of the bars for attack distribution
            for p in axes[i, 1].patches:
                height = p.get_height()
                if height > 100:  # Adjust this threshold as needed
                    axes[i, 1].annotate(str(height), (p.get_x() + p.get_width() / 2., height - 150), 
                                        ha='center', va='bottom', color='white')
                else:
                    axes[i, 1].annotate(str(height), (p.get_x() + p.get_width() / 2., height + 15), 
                                        ha='center', va='bottom', color='black')


                    
        Plots.plt.tight_layout()
        Plots.plt.show()

    def plot_top_10_mitre_id(df):
        """
        Method to generate and display subplots of the top 10 MITRE ATT&CK IDs in overall frequency and for attacks.

        Args:
            df (DataFrame): The DataFrame containing the event data.

        Returns:
            None
        """
        # Top 10 MITRE ATT&CK ID per overall frequency
        top_10_attacks_overall = df['RuleAnnotation.mitre_attack.id'].value_counts().head(10)

        # Top 10 MITRE ATT&CK ID corresponding to attacks
        top_10_attacks_attack = df[df['corrisponde_ad_attacco'] == 1]['RuleAnnotation.mitre_attack.id'].value_counts().head(10)

        # Visualization with Matplotlib
        fig, axes = Plots.plt.subplots(1, 2, figsize=(15, 6))  # Two side-by-side plots

        # Plot 1: Top 10 overall
        top_10_attacks_overall.plot(kind='bar', ax=axes[0])
        axes[0].set_title('Top 10 MITRE ATT&CK IDs (Overall)')
        axes[0].set_xlabel('MITRE ATT&CK ID')
        axes[0].set_ylabel('Frequency')
        axes[0].tick_params(axis='x', rotation=45)

        # Add values on top of the bars for the first plot
        for p in axes[0].patches:
            axes[0].annotate(str(p.get_height()), (p.get_x() + 0.05, p.get_height() + 5))

        # Plot 2: Top 10 attacks
        top_10_attacks_attack.plot(kind='bar', ax=axes[1])
        axes[1].set_title('Top 10 MITRE ATT&CK IDs (Attacks)')
        axes[1].set_xlabel('MITRE ATT&CK ID')
        axes[1].set_ylabel('Frequency')
        axes[1].tick_params(axis='x', rotation=45)

        # Add values on top of the bars for the second plot
        for p in axes[1].patches:
            axes[1].annotate(str(p.get_height()), (p.get_x() + 0.05, p.get_height() + 5))

        Plots.plt.tight_layout()  # To avoid overlapping
        Plots.plt.show()

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
        rows = Plots.math.ceil(num_plots / cols)  # Calcola il numero di righe necessario

        # Creiamo i subplot
        fig, axes = Plots.plt.subplots(rows, cols, figsize=(figsize_multiplier[0] * cols, figsize_multiplier[1] * rows))

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

            # Aggiungiamo i valori sopra ogni barra
            for p in ax.patches:
                ax.annotate(str(p.get_height()), (p.get_x() + p.get_width() / 2., p.get_height()), ha='center', va='center', xytext=(0, 5), textcoords='offset points')

        # Rimuoviamo gli assi vuoti
        for i in range(num_plots, rows * cols):
            fig.delaxes(axes.flat[i])

        # Aggiustiamo il layout
        Plots.plt.tight_layout()
        Plots.plt.show()