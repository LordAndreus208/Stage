# [Tirocinio](https://github.com/SigmaCorvallisYoroi/Tirocinio/tree/main)
  
## File principali:
### [analisi_log_attacco.ipynb](https://github.com/SigmaCorvallisYoroi/Tirocinio/blob/main/analisi_log_attacco.ipynb)
Caricamento e visualizzazione del **dataframe grezzo**.  
Visualizzazione del dataframe dopo **Processing** e **StandardScaling**.  
Visualizzazione del dataframe con la **colonna** che indica se ciascun evento **corrisponde ad attacco** o no.  
Visualizzazione dei **grafici** con le varie analisi statistiche su **regole e attacchi** e delle loro **descrizioni**.
Scelta della **regola da studiare** e visualizzazione dei **grafici** con le varie analisi statistiche relativi ad essa.  
Scelta del numero di **eventi da considerare** prima della regola che interessa per visualizzare **grafici** con i **pattern degli eventi antecedenti** alla sua attivazione.  
Visualizzazione dei **grafici** delle **Matrici di Correlazione**.  
Visualizzazione dei **risultati** dei modelli di **Machine Learning** e della **rete neurale** in base al tipo di codifica utilizzato, OneHot e Label Encoder.  
  
### [analisi_pattern.ipynb](https://github.com/SigmaCorvallisYoroi/Tirocinio/blob/main/analisi_pattern.ipynb) (TODO)
Visualizzazione dei **pattern** in base a ogni attacco.  

### [analisi_log_completa.ipynb](https://github.com/SigmaCorvallisYoroi/Tirocinio/blob/main/analisi_log_completa.ipynb)
Copia di analisi_log_attacco funzionante con il dataset intero.  
  
## File secondari:
### [lib.py](https://github.com/SigmaCorvallisYoroi/Tirocinio/blob/main/file_py/lib.py)
Classe per **importare** tutte le librerie necessarie

### [utils.py](https://github.com/SigmaCorvallisYoroi/Tirocinio/blob/main/file_py/utils.py)
Classe per scriveree le **descrizioni** di alcuni dei **grafici** in formato *markdown*
  
### [csv_preprocessing_scaler.py](https://github.com/SigmaCorvallisYoroi/Tirocinio/blob/main/file_py/csv_preprocessing_scaler.py)
Classe per:  
            **visualizzare il df**;  
            **preprocessing di base** (rimozione delle colonne superflue e dei valori nulli rimanenti, conversione in datetime dove necessario);  
            **preprocessing** per preparare i dati per **Label** e **OneHot Encoder**;  
            applicare lo **Standard Scaler** al dataset.  
  
### [run_log_parser.py](https://github.com/SigmaCorvallisYoroi/Tirocinio/blob/main/file_py/run_log_parser.py)
Classe per:  
            importare ed elaborare i **log di esecuzione**;  
            individuare e **riportare gli attacchi** nel dataset fornito nella nuova **colonna** "**corrisponde_ad_attacco**".  
  
### [plots.py](https://github.com/SigmaCorvallisYoroi/Tirocinio/blob/main/file_py/plots.py)
Classe per:  
            visualizzare un **grafico** con la **percentuale** di eventi corrispondenti ad **attacchi**;  
            visualizzare un **grafico** con le **10 regole** che si sono **attivate più volte** in generale, durante un attacco e durante un falso attacco;  
            visualizzare dei **grafici** con **Precisione** e **Recall** di ogni regola;  
            visualizzare un **grafico** con la **distribuzione di attacchi e non-attacchi** in base alle colonne "**severity_id**", "**tag**" e "**EventType**";  
            visualizzare un grafico con attacchi e non-attacchi per ogni regola.  
  
### [plots_single_attack.py](https://github.com/SigmaCorvallisYoroi/Tirocinio/blob/main/file_py/plots_single_attack.py)
Classe per:  
            visualizzare attacchi e non attacchi in un **grafico** con la **frequenza di attivazione** di una **regola specifica** per intervalli di 5 minuti;  
            visualizzare dei **grafici** con attacchi e non-attacchi di una **regola specifica** in base ai **mitre attack** a cui ha risposto, ai **tipi di evento**, alle **criticità**, ai **tag**, agli **id dei             processi** e dei **processi genitori**;  
            visualizzare dei **grafici** con le **regole, gli attacchi, i parent process, i process, gli EventType, i tag e le severity** che si sono **attivate subito prima della attivazione di una regola                    specifica** (il numero di eventi da considerare prima dell'attivazione della regola è a scelta).  

### [correlation_matrix_plots.py](https://github.com/SigmaCorvallisYoroi/Tirocinio/blob/main/file_py/correlation_matrix_plots.py)  
Classe per visualizzare il **grafico** delle **matrici di correlazione** per **Label** e **One Hot** Encoder.  

### [preprocessing_train_test_split.py](https://github.com/SigmaCorvallisYoroi/Tirocinio/blob/main/file_py/preprocessing_train_test_split.py)  
Classe per **dividere** i dati preprocessati nei set di **training** e **test**.

### [initial_training.py](https://github.com/SigmaCorvallisYoroi/Tirocinio/blob/main/file_py/initial_training.py)  
Classe per **addestrare** e **valutare** i dati di train e test su diversi modelli di **machine learning di base**.  

### [hyperparameter_tuning.py](https://github.com/SigmaCorvallisYoroi/Tirocinio/blob/main/file_py/hyperparameter_tuning.py)  
Classe per il **tuning degli iperparametri** dei modelli di machine learning tramite **grid search**.  

### [advanced_models.py](https://github.com/SigmaCorvallisYoroi/Tirocinio/blob/main/file_py/advanced_models.py)  
Classe per **addestrare** e **valutare** i dati di train e test su diversi modelli di **machine learning avanzati**.  

### [deep_learning_model.py](https://github.com/SigmaCorvallisYoroi/Tirocinio/blob/main/file_py/deep_learning_model.py)  
Classe per **addestrare** e **valutare** i dati di train e test su un modello di **rete neurale** tramite l'uso della libreria **Keras**.  

### [model_evaluator.py](https://github.com/SigmaCorvallisYoroi/Tirocinio/blob/main/file_py/model_evaluator.py)  
Classe per visualizzare i **risultati dei modelli** tramite vari **report di classificazione**.

### [stat_severity.py](https://github.com/SigmaCorvallisYoroi/Tirocinio/blob/main/file_py/stat_severity.py)
Classe per visualizzare il **grafico delle criticità** *massime*, *medie* e *minime* di **ogni attacco**.
