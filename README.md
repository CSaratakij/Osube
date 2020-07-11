# Osube
- Extract multiple [Osu!](https://osu.ppy.sh/)'s beatmaps (.osz)

# Dependencies
- python3

# Getting Started
1. Clone this repository
2. Make osube.py executable
- (optional) add 'osube.py' to PATH environment variable, alias or create symbolic link for better usage.

# Example
assume we alias to 'osube'
- Extract all .osz from current working directory to 'ExtractDir' and keep .osz file
```sh
osube ExtractDir -k
```
- Extract 'ABC.osz' to 'ExtractDir' and keep .osz file
```sh
osube ABC.osz ExtractDir -k
```

# For Linux user
- To better integate with linux, you need to add the custom mimetype for the osu beatmap.
The file manager will recognize the new file type and run osube to extract our beatmap.
Please do the following
1. Symbolic link 'osube.py' to 'osube' (example, link to /usr/local/bin)
```sh
sudo ln -s /path/to/osube.py /usr/local/bin/osube
```
2. Modify 'osube.desktop' to make osube extract to the osu! Song directory. (Inside the 'Exec' section)
```
Exec=osube %F "/absolute/path/to/osu/Song/Directory"
```
3. run 'linux-integration.sh' script.
4. Enjoy :D

### Osube-Watcher
- To better extract beatmap without osu! direct, you need 'osube-watcher.sh'. It's a little shell script to detect .osz file in the directory.
You can run this watcher in your default browser download directory (ex. ~/Download) and it will auto extract beatmap for you. Really handy when you download beatmap by a web browser.

(need to alias or symbolic link 'osube.py' to 'osube')\
(alias this to 'osube-watcher' is recommend)

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

