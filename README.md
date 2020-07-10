# Osube
- Extract multiple [Osu!](https://osu.ppy.sh/)'s beatmaps (.osz)

# Dependencies
- python3

# Getting Started
1. Clone this repository
2. Make osube.py executable
- (optional) add alias or create symbolic link for better usage.

# Example
- Extract all .osz from current working directory to 'ExtractDir' and keep .osz file
```sh
./osube.py ExtractDir -k
```
- Extract 'ABC.osz' to 'ExtractDir' and keep .osz file
```sh
./osube.py ABC.osz ExtractDir -k
```

# For Linux user
- To better intregate with linux, we will add the custom mimetype for the osu beatmap.
The file manager will recognize the new file type and run osube to extract our beatmap.
Please do the following
1. Symbolic link 'osube.py' to 'osube'
2. Modify 'osube.desktop' to make osube extract to the osu! Song directory.
3. run 'linux-intregate.sh' script.
4. Enjoy :D

# License
- [MIT](LICENSE)

