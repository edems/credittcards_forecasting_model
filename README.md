# Vorhersagemodell zur Transaktionsvorhersage und Kostenreduktion

Dieses Repository enthält ein umfassendes Projekt zur Erstellung und Optimierung eines maschinellen Lernmodells zur Vorhersage von Transaktionsergebnissen und zur Minimierung von Transaktionskosten. Das Hauptziel ist es, ein Vorhersagemodell zu entwickeln, das erfolgreich Transaktionen prognostizieren und die damit verbundenen Gebühren basierend auf vordefinierten Gebührenstrukturen reduzieren kann.

## Projektübersicht

1. **Projektorganisation**:
    - Verwendung der CRISP-DM Methode zur strukturierten und systematischen Herangehensweise an die Datenanalyse und Modellentwicklung.
    - Ziel ist es, die Zuweisung von Kreditkartenzahlungen an die geeigneten Zahlungsdienstleister (PSPs) zu automatisieren, um die Erfolgsrate der Transaktionen zu erhöhen und die Transaktionskosten gering zu halten.

2. **Datenanalyse**:
    - Datenbereinigung: Entfernen von Duplikaten, Kodieren kategorialer Variablen und Normalisierung der Daten.
    - Explorative Datenanalyse (EDA): Untersuchung der Datenstruktur und der Beziehungen zwischen den Variablen.
    - Korrelationsanalyse: Identifikation der Merkmale, die den Erfolg von Transaktionen beeinflussen.

3. **Modellierung und Evaluation**:
    - Erstellung eines Basismodells (RandomForestClassifier) zur Vorhersage des Erfolgs von Transaktionen.
    - Modellbewertung: Bewertung der Modelle anhand von Metriken wie Genauigkeit, Precision, Recall und F1-Score.
    - Optimierung durch Hyperparameter-Tuning für verschiedene Modelle: RandomForestClassifier, GradientBoostingClassifier, XGBoostClassifier, LightGBMClassifier, CatBoostClassifier und SVM.
    - Berechnung der Transaktionsgebühren vor und nach der Anwendung der Vorhersagemodelle.

4. **Integration in die tägliche Arbeit**:
    - Entwicklung eines Dashboards zur Überwachung der Erfolgsrate von Transaktionen, Analyse der Modellmetriken, Darstellung der Kosteneinsparungen und Prognose zukünftiger Kosten.
    - Schulung der Mitarbeiter im Fachbereich zur Nutzung des Dashboards und Interpretation der Visualisierungen.

## Wichtige Metriken

- **Genauigkeit**
- **Precision**
- **Recall**
- **F1-Score**
- **Gesamte Transaktionsgebühren**

## Ergebnisse

- Die optimierten Modelle, insbesondere RandomForestClassifier, GradientBoostingClassifier und LightGBMClassifier, zeigten signifikante Verbesserungen bei der Vorhersage von Transaktionsergebnissen und der Reduzierung von Transaktionsgebühren.

## Tools und Bibliotheken

- **Python**
- **Pandas**
- **NumPy**
- **Scikit-learn**
- **XGBoost**
- **LightGBM**
- **CatBoost**
- **Seaborn**
- **Matplotlib**
- **Joblib**

## Nutzung

1. **Repository klonen**:
    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

2. **Erforderliche Bibliotheken installieren**:
    ```bash
    pip install pandas numpy scikit-learn xgboost lightgbm catboost joblib matplotlib seaborn
    ```

3. **Jupyter-Notebooks oder Python-Skripte ausführen**, um die Analyse und das Modelltraining zu reproduzieren:
    - `daten_analyse.ipynb`: Durchführung der explorativen Datenanalyse.
    - `basismodel.ipynb`: Training des Basismodells.
    - `advanced_models_hyperparameter_and_CV.ipynb`: Training mehrerer Modelle, deren Hyperparameteroptimierung und Kreuzvalidierung. In diesem Notebook werden folgende Schritte durchgeführt:
        - Laden und Vorverarbeiten der Daten
        - Umwandeln von kategorischen Merkmalen in numerische Werte
        - Aufteilen der Daten in Trainings- und Testsets
        - Definieren und Trainieren mehrerer Modelle (RandomForest, GradientBoosting, XGBoost, CatBoost und SVM)
        - Hyperparameter-Tuning mit RandomizedSearchCV
        - Speichern und Laden der trainierten Modelle
        - Berechnung der Transaktionsgebühren vor und nach der Prognose
        - Durchführung einer Sweet Spot Analyse zur Bewertung der Modelle

4. **Ergebnisse evaluieren** und das optimierte Modell zur Vorhersage von Transaktionsergebnissen und zur Minimierung der Gebühren verwenden. Zusätzlich wurde ein Dashboard entwickelt:
    - Das Dashboard bietet Funktionen zur Überwachung der Erfolgsrate von Transaktionen, zur Analyse der Modellmetriken, zur Darstellung der Kosteneinsparungen und zur Prognose zukünftiger Kosten.
    - Es ermöglicht eine einfache und intuitive Visualisierung der wichtigsten Kennzahlen, was die Entscheidungsfindung erleichtert.

Viel Erfolg bei der Nutzung des Projekts! Bei Fragen oder Anregungen können Sie gerne ein Issue im Repository erstellen.
