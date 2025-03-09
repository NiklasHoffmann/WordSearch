# 🔍 Suche nach Dateien mit bestimmten Wörtern

![GitHub License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python Version](https://img.shields.io/badge/python-3.x-blue)

Dieses Skript durchsucht Dateien in einem angegebenen Verzeichnis oder Laufwerk nach bestimmten Wörtern. Es identifiziert Dateien, die eine festgelegte Mindestanzahl von Wörtern aus einer Wortliste enthalten.

## 📌 Features

 🔎 **Durchsucht Dateien nach bestimmten Wörtern**
 📂 **Unterstützt beliebige Verzeichnisse & Laufwerke**
 📊 **Zeigt Fortschritt während der Suche an**
 ⚡ **Bereits erstellte `.exe` kann direkt genutzt werden**
 🚀 **Autostart-Option für Windows**

## 🔧 Anforderungen

 **Python 3.x** (falls du das Skript manuell ausführst)
 Eine Datei mit 2048 Wörtern (`bip39_wordlist.txt`), in der jedes Wort in einer neuen Zeile steht.

## 📥 Installation

1. **Dieses Repository klonen oder das Skript herunterladen**

   git clone https://github.com/dein-github-username/suche-skript.git
   cd suche-skript

2. **wordlist.txt** mit den zu suchenden Wörtern in denselben Ordner legen

## 🚀 Verwendung

### 🔹 EXE-Datei ausführen

Falls du die bereits erstellte `.exe` verwenden möchtest, kannst du das Start-Skript nutzen. Führe einfach `start_script.bat` aus oder navigiere manuell in den `dist/`-Ordner und starte die `search_files.exe`:

cd Pfad/zu/deinem/Projekt/dist
search_files.exe

Alternativ kannst du die `.exe` direkt durch Doppelklick starten.

### 🔹 Python-Skript ausführen

Falls du das Skript in **Python** ausführen möchtest, öffne ein Terminal und navigiere in das Verzeichnis des Skripts:

cd Pfad/zu/deinem/Projekt

Starte das Skript mit:

python search_files.py

### 🏁 **Beim Start wirst du gefragt:**

 **Welches Laufwerk oder Verzeichnis durchsucht werden soll** (z. B. `C:/`, `D:/` oder ein bestimmter Ordner)
 **Wie viele Wörter aus der Wortliste mindestens enthalten sein müssen**

Das Skript zeigt während der Suche Fortschrittsinformationen an und listet am Ende die gefundenen Dateien auf.

## ⚙️ Autostart-Option

Falls das Skript bei jedem Systemstart automatisch laufen soll:

1. `Win + R` drücken und `shell:startup` eingeben
2. Die `search_files.exe` oder `start_script.bat` in diesen Ordner kopieren
3. Beim nächsten Hochfahren wird das Skript automatisch ausgeführt

## 🛠 Fehlerbehebung

Falls das Skript **sofort schließt**, öffne es in der Eingabeaufforderung (`CMD`):

cd Pfad/zu/deinem/Projekt/dist
search_files.exe

Falls du Fragen hast oder Probleme auftreten, kannst du mich jederzeit fragen! 🚀

## 📜 Lizenz

Dieses Projekt steht unter der **MIT-Lizenz**. Weitere Informationen findest du in der `LICENSE`-Datei.
