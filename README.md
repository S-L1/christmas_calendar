# Christmas Calendar

*- English Version Below -*

### Beschreibung

Dieses Repository enthält einen Adventskalender in drei Varianten:
 - Original Code als [Python-Skript](/source/christmas_calendar.py)
 - Lauffähiges [Programm](/linux/Christmas%20Calendar) für ubuntu-basierte Linux-Betriebssysteme
 - Lauffähiges [Programm](/windows/Christmas%20Calendar) für Windows-Betriebssystem

Je nach dem, auf welchem Betriebssystem die Anwendung laufen soll, kann der entsprechende Ordner heruntergeladen und die Anwendung
mit Doppelklick auf die *Christmas Calendar*-Datei gestartet werden.

Diese Arbeit unterliegt den Bestimmungen einer MIT-Lizenz. Alle verwendeten Bilder wurden von mir selbst angefertigt.<br/>
© 2023 S. Liedtke.

### Inhalte

Inhalte des Adventskalenders sind einzelne Zitate. Diese sind in der [contents.json](/source/assets/contents/contents.json) Datei abgelegt.
Da einmal angezeigte Inhalte aus der contents.json gelöscht werden, sobald sie angezeigt wurden, existiert in dem Ordner auch eine entsprechende [Backup-Datei](/source/assets/contents/contents.json.bak),
sodass der ursprüngliche Zustand wiederhergestellt werden kann. Es können auch eigene Inhalte in dieser Datei hinzugefügt werden. Die beiden Dateien existieren in allen drei Versionen der Anwendung (Unterordner *assets/contents*).<br/>
Die Inhalte werden dann von der Anwendung in pseudo-zufälliger Reihenfolge ausgewählt.

### System-Anforderungen

Die nachfolgenden Python-Bibliotheken werden für das Skript im Ordner *source* benötigt:
 - json
 - PyQt6
 - random

## English Version

### Description

This repository contains a christmas calendar in three different versions::
 - Original code as [Python script](/source/christmas_calendar.py)
 - Runnable [program](/linux/Christmas%20Calendar) for ubuntu-based Linux OS
 - Runnable [program](/windows/Christmas%20Calendar) for Windows OS

Depending on the operating system the application should run, the respective folder and application may be downloaded and
started by double clicking the *Christmas Calendar* file.

This work is licensed under an MIT License. Any pictures used are my own.<br/>
© 2023 S. Liedtke.

### Contents

The christmas calendar contains some quotations. Those are listed in the [contents.json](/source/assets/contents/contents.json) file.
The content is removed from the contents.json file after it has been displayed once, but there is a [backup file](/source/assets/contents/contents.json.bak)
from which the original state can be restored. Individual adjustments may be made to the file to add or change the content displayed. Both of the files exist in all three versions of the application (sub folder *assets/contents*).<br/>
The contents is then selected by the application in pseudo-random order.

### System Requirements

The following Python libraries are needed to run the script in folder *source*:
 - json
 - PyQt6
 - random
