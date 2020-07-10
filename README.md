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
- To better integate with linux, you need to add the custom mimetype for the osu beatmap.
The file manager will recognize the new file type and run osube to extract our beatmap.
Please do the following
1. Symbolic link 'osube.py' to 'osube' (example, link to /usr/local/bin)
2. Modify 'osube.desktop' to make osube extract to the osu! Song directory.
3. run 'linux-integration.sh' script.
4. Enjoy :D

### Osube-Watcher
- To better extract beatmap without osu! direct, you need 'osube-watcher.sh'. It's a little shell script to detect .osz file in the directory.
You can run this watcher in your default browser download directory (ex. ~/Download) and it will auto extract beatmap for you. (alias this to 'osube-watcher' is recommend)

### dependencies
- grep
- inotifywait
- osube

#### example
- See the help entry
```sh
osube-watcher -h
```

- Watching Download directory and extract beatmap to 'ExtractDir'
```sh
osube-watcher ~/Download ~/ExtractDir
```

- Watching the current working directory and extract beatmap to 'ExtractDir' specify by 'OSU_BEATMAP_SONGDIR' environment variable. (path in variable should be the absolute path)
```sh
OSU_BEATMAP_SONGDIR=/home/user/ExtractDir osube-watcher
```
# License
- [MIT](LICENSE)

