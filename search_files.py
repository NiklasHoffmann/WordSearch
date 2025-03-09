import os
import re
import sys

def load_words(wordlist_path):
    """Lädt die 2048 Wörter aus einer Datei."""
    with open(wordlist_path, 'r', encoding='utf-8') as f:
        return set(f.read().splitlines())

def search_files(root_dir, words, min_matches):
    """Durchsucht alle Dateien im root_dir nach mindestens min_matches der Wörter."""
    matching_files = []
    print(f"Zähle Dateien in {root_dir}... Bitte warten.")
    
    total_files = sum(len(files) for _, _, files in os.walk(root_dir))
    print(f"Anzahl der zu durchsuchenden Dateien: {total_files}")
    
    processed_files = 0
    
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            try:
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                    found_words = {word for word in words if re.search(rf'\b{re.escape(word)}\b', content)}
                    if len(found_words) >= min_matches:
                        matching_files.append(file_path)
            except (PermissionError, IsADirectoryError, UnicodeDecodeError):
                continue
            
            # Fortschrittsanzeige
            processed_files += 1
            percent_done = (processed_files / total_files) * 100
            sys.stdout.write(f"\rDurchsuche Dateien... {percent_done:.2f}% abgeschlossen")
            sys.stdout.flush()
    
    print("\nSuche abgeschlossen.")
    return matching_files

if __name__ == "__main__":
    wordlist_path = "bip39_wordlist.txt"  # Hier den Pfad zu deiner Datei mit den 2048 Wörtern angeben
    
    search_dir = input("Gib das Laufwerk oder Verzeichnis ein, das durchsucht werden soll (z.B. C:/ oder D:/): ")
    min_matches = int(input("Gib die Mindestanzahl der Wörter an, die in einer Datei vorkommen müssen: "))
    
    words = load_words(wordlist_path)
    result_files = search_files(search_dir, words, min_matches)
  
    print("Gefundene Dateien:")
    for file in result_files:
        print(file)
    
    input("\nDrücke Enter, um das Programm zu beenden...")
