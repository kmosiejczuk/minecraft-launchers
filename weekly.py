#!/usr/local/bin/python3

import minecraft_launcher_lib
import subprocess

desired_version = "21w06a"

# Your email, username and password below
login = "yourEmailUsername"
password = "seekritPasswordHere"

# Get Minecraft directory
minecraft_directory = minecraft_launcher_lib.utils.get_minecraft_directory()

minecraft_libs = minecraft_directory + "/libraries"

# Make sure the desired version of Minecraft is installed
print("Installing version " + desired_version + " if needed")
minecraft_launcher_lib.install.install_minecraft_version(desired_version,minecraft_directory)

# Login
print("logging in")
login_data = minecraft_launcher_lib.account.login_user( login, password )

# Useful figuring out new minecraft versions

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

real_command = ['/usr/local/jdk-11/bin/java', '-Xms1G', '-Xmx2G', '-Djava.library.path=' + minecraft_directory + '/versions/21w06a/natives', '-Dminecraft.launcher.brand=minecraft-launcher-lib', '-Dminecraft.launcher.version=2.1', '-cp', '' + minecraft_libs + '/com/mojang/patchy/1.1/patchy-1.1.jar:' + minecraft_libs + '/oshi-project/oshi-core/1.1/oshi-core-1.1.jar:' + minecraft_libs + '/net/java/dev/jna/jna/4.4.0/jna-4.4.0.jar:' + minecraft_libs + '/net/java/dev/jna/platform/3.4.0/platform-3.4.0.jar:' + minecraft_libs + '/com/ibm/icu/icu4j/66.1/icu4j-66.1.jar:' + minecraft_libs + '/com/mojang/javabridge/1.1.23/javabridge-1.1.23.jar:' + minecraft_libs + '/net/sf/jopt-simple/jopt-simple/5.0.3/jopt-simple-5.0.3.jar:' + minecraft_libs + '/io/netty/netty-all/4.1.25.Final/netty-all-4.1.25.Final.jar:' + minecraft_libs + '/com/google/guava/guava/21.0/guava-21.0.jar:' + minecraft_libs + '/org/apache/commons/commons-lang3/3.5/commons-lang3-3.5.jar:' + minecraft_libs + '/commons-io/commons-io/2.5/commons-io-2.5.jar:' + minecraft_libs + '/commons-codec/commons-codec/1.10/commons-codec-1.10.jar:' + minecraft_libs + '/net/java/jinput/jinput/2.0.5/jinput-2.0.5.jar:' + minecraft_libs + '/net/java/jutils/jutils/1.0.0/jutils-1.0.0.jar:' + minecraft_libs + '/com/mojang/brigadier/1.0.17/brigadier-1.0.17.jar:' + minecraft_libs + '/com/mojang/datafixerupper/4.0.26/datafixerupper-4.0.26.jar:' + minecraft_libs + '/com/google/code/gson/gson/2.8.0/gson-2.8.0.jar:' + minecraft_libs + '/com/mojang/authlib/2.1.28/authlib-2.1.28.jar:' + minecraft_libs + '/org/apache/commons/commons-compress/1.8.1/commons-compress-1.8.1.jar:' + minecraft_libs + '/org/apache/httpcomponents/httpclient/4.3.3/httpclient-4.3.3.jar:' + minecraft_libs + '/commons-logging/commons-logging/1.1.3/commons-logging-1.1.3.jar:' + minecraft_libs + '/org/apache/httpcomponents/httpcore/4.3.2/httpcore-4.3.2.jar:' + minecraft_libs + '/it/unimi/dsi/fastutil/8.2.1/fastutil-8.2.1.jar:' + minecraft_libs + '/org/apache/logging/log4j/log4j-api/2.8.1/log4j-api-2.8.1.jar:' + minecraft_libs + '/org/apache/logging/log4j/log4j-core/2.8.1/log4j-core-2.8.1.jar:/usr/local/share/lwjgl3/lwjgl.jar:/usr/local/share/lwjgl3/lwjgl-openal.jar:/usr/local/share/lwjgl3/lwjgl-opengl.jar:/usr/local/share/lwjgl3/lwjgl-glfw.jar:/usr/local/share/lwjgl3/lwjgl-stb.jar:/usr/local/share/lwjgl3/lwjgl-tinyfd.jar:/usr/local/share/lwjgl3/lwjgl-natives-openbsd.jar:/usr/local/share/lwjgl3/lwjgl-opengl-natives-openbsd.jar:/usr/local/share/lwjgl3/lwjgl-tinyfd-natives-openbsd.jar:/usr/local/share/lwjgl3/lwjgl-stb-natives-openbsd.jar:' + minecraft_libs + '/com/mojang/text2speech/1.11.3/text2speech-1.11.3.jar:' + minecraft_libs + '/com/mojang/text2speech/1.11.3/text2speech-1.11.3-natives-linux.jar:' + minecraft_directory + '/versions/21w06a/21w06a.jar', 'net.minecraft.client.main.Main', '--username', username, '--version', '21w06a', '--gameDir', '' + minecraft_directory + '', '--assetsDir', '' + minecraft_directory + '/assets', '--assetIndex', '1.17', '--uuid', uuid, '--accessToken', token, '--userType', 'mojang', '--versionType', 'snapshot']

# Start Minecraft
subprocess.call(real_command)
