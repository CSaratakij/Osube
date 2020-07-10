# Osube
Extract multiple [Osu!](https://osu.ppy.sh/)'s beatmaps (.osz)

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

# Linux users
- To better intregate with linux, we will add the custom mimetype for the
osu beatmap


# License
- [MIT](LICENSE)

