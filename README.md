# minecraft-launchers
OpenBSD Minecraft launchers based upon minecraft-launcher-lib

You will need the py3-minecraft-launcher-lib, jdk-11, lwjgl 3, and
lwjgl ports installed to be able to use these to launch Minecraft on
OpenBSD. Will work on 6.9 or later except for snapshots and the upcoming
1.17 release. Snapshots and the imminenet 1.17 release require jdk-16
which is in OpenBSD 6.9-current.

These are still pretty crude (having edit them to put in your username
and password), but they _work_.

(Technically, you only need the lwjgl ports for 1.12.2 or earlier. Also,
one only needs lwjgl3 for >= 1.13)
