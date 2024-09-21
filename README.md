## Schritt 1: Python installieren

1. Besuchen Sie die offizielle Python-Website: https://www.python.org/downloads/
2. Klicken Sie auf "Download Python" für die neueste Version.
3. Führen Sie die heruntergeladene Installationsdatei aus.
4. **Wichtig:** Aktivieren Sie das Kontrollkästchen "Add Python to PATH" während der Installation.
5. Folgen Sie den Anweisungen des Installationsassistenten.

## Schritt 2: Visual Studio Code installieren

1. Gehen Sie zur VS Code-Website: https://code.visualstudio.com/
2. Klicken Sie auf "Download for Windows".
3. Führen Sie die heruntergeladene Datei aus und folgen Sie den Installationsanweisungen.

## Schritt 3: Git installieren

Was ist Git: [Was ist GIT? Einfach erklärt! (youtube.com)](https://www.youtube.com/watch?v=fbEobQXZrpU)

1. Besuchen Sie die Git-Website: https://git-scm.com/download/win
2. Der Download sollte automatisch starten. Falls nicht, klicken Sie auf den manuellen Download-Link.
3. Führen Sie die heruntergeladene Datei aus und folgen Sie den Installationsanweisungen.
## Schritt 3b: TortoiseGit installieren

Tortoise Git ist eine Shell, um Kommandozeilenbefehle unter Windows zu vermeiden.
1. Installieren von [TortoiseGit – Windows Shell Interface to Git](https://tortoisegit.org/)
## Schritt 4: GitHub-Repository klonen

1. Öffnen Sie VS Code.
2. Drücken Sie `Ctrl+Shift+P`, geben Sie "Git: Clone" ein und wählen Sie es aus.
3. Fügen Sie die URL `https://github.com/ErikThiel/BKPhysik.git` ein und drücken Sie Enter.
4. Wählen Sie einen lokalen Ordner zum Speichern des Repositories aus.
5. Klicken Sie auf "Open", wenn VS Code fragt, ob Sie das geklonte Repository öffnen möchten.
## Schritt 5: Ausführungsrichtlinie ändern (Windows 11)

Bevor Sie ein virtuelles Environment erstellen, müssen Sie die PowerShell-Ausführungsrichtlinie ändern, um Skripte ausführen zu können:

1. Öffnen Sie PowerShell als Administrator:
   - Drücken Sie `Win + X` und wählen Sie "Windows PowerShell (Admin)" oder "Terminal (Admin)".
2. Geben Sie den folgenden Befehl ein und drücken Sie Enter:
   ```
   Set-ExecutionPolicy RemoteSigned
   ```
3. Bestätigen Sie die Änderung, indem Sie "Y" eingeben und Enter drücken.
4. Sie können die aktuelle Richtlinie überprüfen, indem Sie eingeben:
   ```
   Get-ExecutionPolicy
   ```
   Es sollte "RemoteSigned" anzeigen.

**Hinweis:** Diese Änderung erlaubt die Ausführung lokaler Skripte und signierter Remote-Skripte. Seien Sie vorsichtig beim Ausführen von Skripten aus unbekannten Quellen.
## Schritt 6: Virtuelles Environment erstellen

1. Öffnen Sie in VS Code ein neues Terminal (Terminal -> New Terminal).
2. Navigieren Sie zum Projektordner (falls nicht bereits dort):
   ```
   cd Pfad\zum\BKPhysik-Ordner
   ```
3. Erstellen Sie ein virtuelles Environment:
   ```
   python -m venv venv
   ```
4. Aktivieren Sie das virtuelle Environment:
   ```
   .\venv\Scripts\activate
   ```
## Schritt 7: Virtuelles Environment erstellen

1. Öffnen Sie in VS Code ein neues Terminal (Terminal -> New Terminal).
2. Navigieren Sie zum Projektordner (falls nicht bereits dort):
   ```
   cd Pfad\zum\BKPhysik-Ordner
   ```
3. Erstellen Sie ein virtuelles Environment:
   ```
   python -m venv venv
   ```
4. Aktivieren Sie das virtuelle Environment:
   ```
   .\venv\Scripts\activate
   ```

## Schritt 8: Bibliotheken installieren

1. Stellen Sie sicher, dass das virtuelle Environment aktiviert ist (Sie sollten `(venv)` am Anfang der Terminallinie sehen).
2. Installieren Sie numpy und matplotlib:
   ```
   pip install numpy matplotlib
   ```

## Schritt 9: Testdatei ausführen

1. Erstellen Sie eine neue Datei in VS Code: File -> New File.
2. Speichern Sie die Datei als `test.py` im Projektordner.
3. Fügen Sie folgenden Code ein:
   ```python
   import numpy as np
   import matplotlib.pyplot as plt

   x = np.linspace(0, 10, 100)
   y = np.sin(x)

   plt.plot(x, y)
   plt.title('Sinuswelle')
   plt.show()
   ```
4. Speichern Sie die Datei (`Ctrl+S`).
5. Führen Sie die Datei aus, indem Sie im Terminal eingeben:
   ```
   python test.py
   ```
## Zusätzliche Tipps

- Installieren Sie die Python-Erweiterung in VS Code für bessere Python-Unterstützung.
- Nutzen Sie die Git-Integration in VS Code, um Änderungen zu verfolgen und zu committen.
- Machen Sie sich mit den grundlegenden Git-Befehlen vertraut (`git add`, `git commit`, `git push`). [GitHub Beginner Tutorial in 20 Minuten deinen Workflow verbessern! [Deutsch/Tutorial] (youtube.com)](https://www.youtube.com/watch?v=0jzjz4MZ4ZU)

Folgen Sie dieser Anleitung Schritt für Schritt, und Sie sollten eine funktionierende Python-Umgebung mit VS Code und GitHub-Integration haben. Viel Erfolg bei Ihrem Projekt!
