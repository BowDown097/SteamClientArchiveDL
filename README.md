# SteamClientArchiveDL
Easily download archived Steam clients from the Internet.

## Motivation
The Linux client zips have broken paths and broken permissions, which makes them difficult to install manually. Besides, downloading and extracting everything manually is tedious by itself. This little script gets rid of those annoyances.

## Usage
Make sure you have Python and the `tqdm` package installed.

Pass in a file containing a list of client links as an argument and watch it go. Example provided in the `linklists` folder, which is the last build to have the `-no-browser` flag.

Move the extracted files over to the Steam root folder [(see here for locations)](https://www.pcgamingwiki.com/wiki/Glossary:Game_data#Steam_client) as necessary. Automatic installation is not included to avoid potential problems related to version changes.
