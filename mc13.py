#!/usr/local/bin/python3

import minecraft_launcher_lib
import subprocess

desired_version = "1.13.2"

# Your email, username and password below
login = "yourEmailUsername"
password = "seekritPasswordHere"

# Get Minecraft directory
minecraft_directory = minecraft_launcher_lib.utils.get_minecraft_directory()

# Make sure the desired version of Minecraft is installed
print("Installing version " + desired_version + " if needed")
minecraft_launcher_lib.install.install_minecraft_version(desired_version,minecraft_directory)

minecraft_libs = minecraft_directory + '/libraries'

# Login
print("logging in")
login_data = minecraft_launcher_lib.account.login_user( login, password )

#Get Minecraft command
#options = {
#    "username": login_data["selectedProfile"]["name"],
#    "uuid": login_data["selectedProfile"]["id"],
#    "token": login_data["accessToken"]
#}
#minecraft_command = minecraft_launcher_lib.command.get_minecraft_command(desired_version,minecraft_directory,options)

#print(minecraft_command)

username = login_data["selectedProfile"]["name"]
uuid = login_data["selectedProfile"]["id"]
token = login_data["accessToken"]

real_command = ['/usr/local/jdk-11/bin/java', '-Xms1G', '-Xmx2G', '-Djava.library.path=/usr/local/share/lwjgl3/', '-Dminecraft.launcher.brand=minecraft-launcher-lib', '-Dord.lwjgl.util.Debug=true', '-Dminecraft.launcher.version=0.5', '-Dos.version=OpenBSD_6.7', '-cp', '/usr/local/share/lwjgl3/lwjgl.jar:/usr/local/share/lwjgl3/lwjgl-jemalloc.jar:/usr/local/share/lwjgl3/lwjgl-openal.jar:/usr/local/share/lwjgl3/lwjgl-glfw.jar:/usr/local/share/lwjgl3/lwjgl-opengl.jar:/usr/local/share/lwjgl3/lwjgl-stb.jar:/usr/local/share/lwjgl3/lwjgl-natives-openbsd.jar:/usr/local/share/lwjgl3/lwjgl-glfw-natives-openbsd.jar:/usr/local/share/lwjgl3/lwjgl-opengl-natives-openbsd.jar:/usr/local/share/lwjgl3/lwjgl-stb-natives-openbsd.jar:' + minecraft_libs + '/com/mojang/patchy/1.1/patchy-1.1.jar:' + minecraft_libs + '/oshi-project/oshi-core/1.1/oshi-core-1.1.jar:' + minecraft_libs + '/net/java/dev/jna/jna/4.4.0/jna-4.4.0.jar:' + minecraft_libs + '/net/java/dev/jna/platform/3.4.0/platform-3.4.0.jar:' + minecraft_libs + '/com/ibm/icu/icu4j-core-mojang/51.2/icu4j-core-mojang-51.2.jar:' + minecraft_libs + '/net/sf/jopt-simple/jopt-simple/5.0.3/jopt-simple-5.0.3.jar:' + minecraft_libs + '/com/paulscode/codecjorbis/20101023/codecjorbis-20101023.jar:' + minecraft_libs + '/com/paulscode/codecwav/20101023/codecwav-20101023.jar:' + minecraft_libs + '/com/paulscode/libraryjavasound/20101123/libraryjavasound-20101123.jar:' + minecraft_libs + '/com/paulscode/soundsystem/20120107/soundsystem-20120107.jar:' + minecraft_libs + '/io/netty/netty-all/4.1.25.Final/netty-all-4.1.25.Final.jar:' + minecraft_libs + '/com/google/guava/guava/21.0/guava-21.0.jar:' + minecraft_libs + '/org/apache/commons/commons-lang3/3.5/commons-lang3-3.5.jar:' + minecraft_libs + '/commons-io/commons-io/2.5/commons-io-2.5.jar:' + minecraft_libs + '/commons-codec/commons-codec/1.10/commons-codec-1.10.jar:' + minecraft_libs + '/net/java/jinput/jinput/2.0.5/jinput-2.0.5.jar:' + minecraft_libs + '/net/java/jutils/jutils/1.0.0/jutils-1.0.0.jar:' + minecraft_libs + '/com/mojang/brigadier/1.0.14/brigadier-1.0.14.jar:' + minecraft_libs + '/com/mojang/datafixerupper/1.0.19/datafixerupper-1.0.19.jar:' + minecraft_libs + '/com/google/code/gson/gson/2.8.0/gson-2.8.0.jar:' + minecraft_libs + '/com/mojang/authlib/1.5.25/authlib-1.5.25.jar:' + minecraft_libs + '/org/apache/commons/commons-compress/1.8.1/commons-compress-1.8.1.jar:' + minecraft_libs + '/org/apache/httpcomponents/httpclient/4.3.3/httpclient-4.3.3.jar:' + minecraft_libs + '/commons-logging/commons-logging/1.1.3/commons-logging-1.1.3.jar:' + minecraft_libs + '/org/apache/httpcomponents/httpcore/4.3.2/httpcore-4.3.2.jar:' + minecraft_libs + '/it/unimi/dsi/fastutil/8.2.1/fastutil-8.2.1.jar:' + minecraft_libs + '/org/apache/logging/log4j/log4j-api/2.8.1/log4j-api-2.8.1.jar:' + minecraft_libs + '/org/apache/logging/log4j/log4j-core/2.8.1/log4j-core-2.8.1.jar:' + minecraft_libs + '/com/mojang/realms/1.13.9/realms-1.13.9.jar:' + minecraft_libs + '/com/mojang/text2speech/1.10.3/text2speech-1.10.3.jar:' + minecraft_directory + '/versions/1.13.2/1.13.2.jar', 'net.minecraft.client.main.Main', '--username', username, '--version', '1.13.2', '--gameDir', minecraft_directory, '--assetsDir', minecraft_directory + '/assets', '--assetIndex', '1.13.1', '--uuid', uuid, '--accessToken', token, '--userType', 'mojang', '--versionType', 'release']

# Start Minecraft
subprocess.call(real_command)
