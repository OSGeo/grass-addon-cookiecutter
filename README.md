# GRASS Addon Cookiecutter
GRASS addon template powered by
[Cookiecutter](https://github.com/cookiecutter/cookiecutter)
helps you get started with developing a GRASS addon.

## How to use it
1. Install cookicutter e.g. with `pipx install cookiecutter`.
2. Go to a folder where you want the addon template to be generated.
3. Run `cookiecutter gh:OSGeo/grass-addon-cookiecutter`.
4. It will prompt you with several questions (addon name, your name, ...)
5. Done, your addon template is ready for development!

## Code structure
Example code structure for a generated addon:
```
r.myaddon
├── Makefile
├── r.myaddon.html
├── r.myaddon.ipynb
├── r.myaddon.py
└── testsuite
    └── test_r_myaddon.py

```

## License
This program is free software; you can redistribute it and/or modify it
under the terms of the GNU General Public License as published by the
Free Software Foundation; either version 2 of the License, or (at your
option) any later version.

SPDX-License-Identifier: GPL-2.0-or-later


