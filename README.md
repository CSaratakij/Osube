# Osube
Extract multiple [Osu!](https://osu.ppy.sh/)'s beatmaps (.osz)

# Note
- This is a command line program.

# Getting Start
You can use program in these ways.
(just my suggest.)
(pick the one you like. ^^)

1. Copy osube.py in your common beatmap's download folder and run this program in terminal with python.
2. Create the bash file with specify extract folder, place that script to your common download folder and chmod +x that script ([See this example](osube.sh))
3. Set this program in your environment. In case of linux, edit your /etc/environment ( edit with sudo :) )

# To Use Program
Command :
```
python osube.py [extract directory]
```
1. Run this program in the folder that have osu!'s beatmaps file (.osz)
2. Make sure you specify the extract folder. (It's a 2nd command line argument)
Replace "extract directory" to your Songs folder in your osu! directory.
3. Wait for the extraction to complete.
4. Have fun with Osu! ( Great game by the way :) )

# FAQ
- Q: Why create this?
- A : Well, The extraction achrive program in my os (Lubuntu) doesn't create the folder after you extracted the file and extract the multiple beatmaps is painful- -.

- Q: But Osu! didn't support linux natively, Are you using [Wine](https://www.winehq.org/)?
- A : Wine is awesome but I prefer not to use it anymore. There's a alternative Osu! Client in desktop, It's call [Opsu!](https://itdelatrisu.github.io/opsu/).

# Todo List
- [x] Extract multiple beatmaps.
- [ ] Auto remove beatmaps when successful extracted.
