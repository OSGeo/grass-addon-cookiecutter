#!/usr/bin/env python

"""
MODULE:    {{ cookiecutter.tool }}

AUTHOR(S): {{ cookiecutter.author_name }} <{{ cookiecutter.email }}>

PURPOSE:   {{ cookiecutter.description }}

COPYRIGHT: (C) {% now 'utc', '%Y' %} by {{ cookiecutter.author_name }} and the GRASS Development Team

This program is free software under the GNU General Public
License (>=v2). Read the file COPYING that comes with GRASS
for details.
"""

# %module
# % description: {{ cookiecutter.description }}
# % keyword: raster
# % keyword: algebra
# % keyword: random
# %end
# %option G_OPT_R_INPUT
# %end
# %option G_OPT_R_OUTPUT
# %end


import sys
import atexit
import grass.script as gs


def clean(name):
    gs.run_command("g.remove", type="raster", name=name, flags="f", superquiet=True)


def main():
    # get input options
    options, flags = gs.parser()
    input_raster = options["input"]
    output_raster = options["output"]

    # crete a temporary raster that will be removed upon exit
    temporary_raster = gs.append_node_pid("gauss")
    atexit.register(clean, temporary_raster)

    # if changing computational region is needed, uncomment
    # gs.use_temp_region()

    # verbose message with translatable string
    gs.verbose(_("Generating temporary raster {tmp}").format(tmp=temporary_raster))
    # run analysis
    gs.run_command("r.surf.gauss", output=temporary_raster)
    gs.mapcalc(f"{output_raster} = {input_raster} + {temporary_raster}")

    # save history into the output raster
    gs.raster_history(output_raster, overwrite=True)


if __name__ == "__main__":
    sys.exit(main())
