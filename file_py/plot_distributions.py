class PlotDistributions:
    """
    Class for visualizing the distributions of selected columns for attack and non-attack events.

    Uses matplotlib to create subplots displaying the distribution of selected columns for both attack and non-attack events.
    """

    import matplotlib.pyplot as plt

    def plot_distributions(df):
        """
        Method to generate and display subplots of distributions for attack and non-attack events.

        Args:
            df (DataFrame): The DataFrame containing the event data.

        Returns:
            None
        """
        is_attack = df['corrisponde_ad_attacco'] == 1
        fig, axes = PlotDistributions.plt.subplots(3, 2, figsize=(12, 9))  # 3 rows, 2 columns

        for i, column in enumerate(['severity_id', 'tag', 'EventType']):

            # Attack distribution
            attack_values = df[is_attack][column].value_counts()
            attack_values.plot(kind='bar', ax=axes[i, 0], color='salmon')
            axes[i, 0].set_title(f'Distribution of {column} (Attacks)')
            axes[i, 0].tick_params(axis='x', rotation=45)

            # Non-Attack Distribution
            non_attack_values = df[~is_attack][column].value_counts()
            non_attack_values.plot(kind='bar', ax=axes[i, 1], color='skyblue')  # Same column, different row
            axes[i, 1].set_title(f'Distribution of {column} (Non-Attacks)')
            axes[i, 1].tick_params(axis='x', rotation=45)

        PlotDistributions.plt.tight_layout()
        PlotDistributions.plt.show()