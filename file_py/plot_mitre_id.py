class PlotMitreId:
    """
    Class for visualizing the top 10 MITRE ATT&CK IDs in overall frequency and for attacks.

    Uses matplotlib to create subplots displaying the top 10 MITRE ATT&CK IDs by overall frequency
    and those corresponding to attacks in the provided dataframe.
    """

    import matplotlib.pyplot as plt

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
        fig, axes = PlotMitreId.plt.subplots(1, 2, figsize=(15, 6))  # Two side-by-side plots

        # Plot 1: Top 10 overall
        top_10_attacks_overall.plot(kind='bar', ax=axes[0])
        axes[0].set_title('Top 10 MITRE ATT&CK IDs (Overall)')
        axes[0].set_xlabel('MITRE ATT&CK ID')
        axes[0].set_ylabel('Frequency')
        axes[0].tick_params(axis='x', rotation=45)

        # Plot 2: Top 10 attacks
        top_10_attacks_attack.plot(kind='bar', ax=axes[1])
        axes[1].set_title('Top 10 MITRE ATT&CK IDs (Attacks)')
        axes[1].set_xlabel('MITRE ATT&CK ID')
        axes[1].set_ylabel('Frequency')
        axes[1].tick_params(axis='x', rotation=45)

        PlotMitreId.plt.tight_layout()  # To avoid overlapping
        PlotMitreId.plt.show()