class PlotCakeAttack:
    """
    Class for visualizing the percentage of events that correspond to attacks.

    Uses matplotlib to create a pie chart showing the percentage of events identified as attacks
    compared to the total events in the provided dataframe.
    """

    import matplotlib.pyplot as plt

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
        PlotCakeAttack.plt.figure(figsize=(6, 6))
        PlotCakeAttack.plt.pie([attack_percentage, 100 - attack_percentage], labels=['Attacks', 'Non-Attacks'], autopct='%1.1f%%', startangle=140)
        PlotCakeAttack.plt.title('Percentage of Events that Correspond to Attacks')
        PlotCakeAttack.plt.show()