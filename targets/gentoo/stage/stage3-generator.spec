# This file defines common settings for all stage3 generators. Stage3
# generators are targets that produce a literal stage3 -- currently these
# targets are stage3, stage3-quick, and stage3-freshen.

[section path/mirror]

target: $[:target/subpath]/$[target/name].tar.$[target/compression]

# "current" symlink:
link: $[]/$[target/build]/$[target/subarch]/$[target/name/current].tar.$[target/compression]
link/dest: $[target/build]-$[target/subarch]-$[target/version]/$[target/name].tar.$[target/compression]

[section target]

name: stage3-$[target/subarch]-$[target/version]
name/current: stage3-$[target/subarch]-current

[section trigger]

ok/run: [
#!/bin/bash

# We completed a successful stage3 build, so record the version of this build in our
# .control/version/stage3 file so that other builds can see that this new version is
# available.

install -d $[path/mirror/control]/version || exit 1
echo "$[target/version]" > $[path/mirror/control]/version/stage3 || exit 1

# CREATE current symlink for the stage3
rm -f $[path/mirror/link]
ln -s $[path/mirror/link/dest] $[path/mirror/link] || exit 3
]

