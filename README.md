# Restrict Tablet

This python script allows you to interactively select a screen region and will restrict the pointer given as argument to that screen region.

# Dependencies

- **xrandr / xorg-xrandr**: Install with your distro's package manager
- **xinput / xorg-xinput**: Install with your distro's package manager
- **slop** (https://github.com/naelstrof/slop): Install with your distro's package manager
- **pymatrix** (https://github.com/dmulholland/pymatrix): `sudo pip install pymatrix`

# Install

If you meet the dependencies, You can copy the main.py file and rename it as you wish. There is also an Arch Linux PKGBUILD to install as a system-wide package.

# Usage

```
$ xinput --list # Get the name of the pointer you want to restrict
$ python main.py "Bamboo PAD Pen" # The first device partially matching 
                                  # the supplied screen will be restricted
```
