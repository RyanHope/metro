[collect ./stage/container.spec]

[section target]

name: lxc-$[:subarch]-$[:build]-$[:version]
sys: lxc 
realname: Linux Containers
url: http://lxc.sourceforge.net

[section path/mirror]

target: $[:target/lxc/subpath]/$[target/name].tar.$[target/compression]

[section steps]

chroot/run: [
$[[steps/chroot/run/container/base]]
	rm /etc/fstab || exit 1
	touch /etc/fstab || exit 2
	# enabling one console by default:
	echo "Updating inittab..."
	mv /etc/inittab /etc/inittab.orig || exit 2
	cat /etc/inittab.orig | sed -e '/^#c1:/s/^#c1:/c1:/' > /etc/inittab || exit 3
	rm -f /etc/inittab.orig || exit 4
	echo "Creating /etc/fstab.lxc (to be used by host...)"
	cat > /etc/fstab.lxc << EOF || exit 20
none /lxc/funtoo/dev/pts devpts defaults 0 0
none /lxc/funtoo/proc proc defaults 0 0
none /lxc/funtoo/sys sysfs defaults 0 0
none /lxc/funtoo/dev/shm tmpfs defaults 0 0
none /lxc/funtoo/libexec/rc/init.d tmpfs defaults 0 0
EOF
]


