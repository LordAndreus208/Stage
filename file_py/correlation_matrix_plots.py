class CorrelationMatrixPlots:
    """A utility class for plotting correlation matrices.

    This class provides static methods to plot correlation matrices using matplotlib and seaborn.

    Attributes:
        None

    Methods:
        plot_correlation_matrix(df, title): Plots a correlation matrix for a DataFrame with a specified title.
        plot_correlation_matrix_big(df, title): Plots a larger correlation matrix for a DataFrame with a specified title.
    """

    import matplotlib.pyplot as plt
    import seaborn as sns
    
    def plot_correlation_matrix(df, title):
        """Plots a correlation matrix for a DataFrame with a specified title.

        Args:
            df (pandas.DataFrame): The DataFrame containing the data.
            title (str): The title for the plot.

        Returns:
            None
        """

        correlation_matrix = df.corr()
        CorrelationMatrixPlots.plt.figure(figsize=(10, 8))
        CorrelationMatrixPlots.sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap='coolwarm', linewidths=0.5)
        CorrelationMatrixPlots.plt.xticks(rotation=45, ha='right')
        CorrelationMatrixPlots.plt.yticks(rotation=0)
        CorrelationMatrixPlots.plt.title(title)
        CorrelationMatrixPlots.plt.show()

    def plot_correlation_matrix_big(df, title):
        """Plots a larger correlation matrix for a DataFrame with a specified title.

        Args:
            df (pandas.DataFrame): The DataFrame containing the data.
            title (str): The title for the plot.

        Returns:
            None
        """
        
        correlation_matrix = df.corr()
        CorrelationMatrixPlots.plt.figure(figsize=(20, 18))
        CorrelationMatrixPlots.sns.heatmap(correlation_matrix, annot=False, fmt=".2f", cmap='coolwarm', linewidths=0.5)
        CorrelationMatrixPlots.plt.xticks(rotation=45, ha='right')
        CorrelationMatrixPlots.plt.yticks(rotation=0)
        CorrelationMatrixPlots.plt.title(title)
        CorrelationMatrixPlots.plt.show()