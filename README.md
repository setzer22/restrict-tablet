# Restrict Tablet

This python script allows you to interactively select a screen region and will restrict the pointer given as argument to that screen region.

# Dependencies

- xrandr
- xinput 
- slop (https://github.com/naelstrof/slop)
- pymatrix (https://github.com/dmulholland/pymatrix)

# Install

If you meet the dependencies, You can copy the main.py file and rename it as you wish. There is also an Arch Linux PKGBUILD to install as a system-wide package.

# Usage

```
$ xinput --list # Get the name of the pointer you want to restrict
$ python main.py "Bamboo PAD Pen" # The first device partially matching 
                                  # the supplied screen will be restricted
```
