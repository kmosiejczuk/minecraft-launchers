#!/usr/local/bin/python3 -u

import minecraft_launcher_lib as mll
import subprocess

# Minecraft version
mc_version = "1.18.2-pre3"

# Asset index is same but without final revision
asset_index = "1.18"

# Your email, username and password below
login =    "yourEmailUsername"
password = "seekritPasswordHere"

# Get Minecraft directory
mc_directory = mll.utils.get_minecraft_directory()

libdir = mc_directory + "/libraries/"

lwjgl3_libs = '/usr/local/share/lwjgl3/lwjgl.jar:' \
  + '/usr/local/share/lwjgl3/lwjgl-openal.jar:' \
  + '/usr/local/share/lwjgl3/lwjgl-opengl.jar:' \
  + '/usr/local/share/lwjgl3/lwjgl-glfw.jar:' \
  + '/usr/local/share/lwjgl3/lwjgl-stb.jar:' \
  + '/usr/local/share/lwjgl3/lwjgl-tinyfd.jar:' \
  + '/usr/local/share/lwjgl3/lwjgl-natives-openbsd.jar:' \
  + '/usr/local/share/lwjgl3/lwjgl-opengl-natives-openbsd.jar:' \
  + '/usr/local/share/lwjgl3/lwjgl-tinyfd-natives-openbsd.jar:' \
  + '/usr/local/share/lwjgl3/lwjgl-stb-natives-openbsd.jar:'

# Make sure the desired version of Minecraft is installed
print("Installing version " + mc_version + " if needed... ", end="")
mll.install.install_minecraft_version(mc_version,mc_directory)
print("Done")

# Login
print("Logging in... ", end="")
login_data = mll.account.login_user( login, password )
print("Done")

# Useful figuring out new minecraft versions

# Get Minecraft command
#options = {
#    "username": login_data["selectedProfile"]["name"],
#    "uuid":     login_data["selectedProfile"]["id"],
#    "token":    login_data["accessToken"]
#}
#minecraft_command = mll.command.get_minecraft_command(mc_version,mc_directory,options)

#print(minecraft_command)

username = login_data["selectedProfile"]["name"]
uuid =     login_data["selectedProfile"]["id"]
token =    login_data["accessToken"]

real_command = [
  '/usr/local/jdk-17/bin/java',
  '-Xms2G',
  '-Xmx6G',
  '-Djava.library.path=/usr/local/share/lwjgl3/',
  '-Dminecraft.launcher.brand=minecraft-launcher-lib',
  '-Dminecraft.launcher.version=2.1',
  '-cp',
  libdir + 'com/mojang/logging/1.0.0/logging-1.0.0.jar:'
  + libdir + 'com/mojang/blocklist/1.0.10/blocklist-1.0.10.jar:'
  + libdir + 'com/mojang/patchy/2.2.10/patchy-2.2.10.jar:'
  + libdir + 'com/github/oshi/oshi-core/5.8.5/oshi-core-5.8.5.jar:'
  + libdir + 'net/java/dev/jna/jna/5.10.0/jna-5.10.0.jar:'
  + libdir + 'net/java/dev/jna/jna-platform/5.10.0/jna-platform-5.10.0.jar:'
  + libdir + 'org/slf4j/slf4j-api/1.8.0-beta4/slf4j-api-1.8.0-beta4.jar:'
  + libdir + 'org/apache/logging/log4j/log4j-slf4j18-impl/2.17.0/log4j-slf4j18-impl-2.17.0.jar:'
  + libdir + 'com/ibm/icu/icu4j/70.1/icu4j-70.1.jar:'
  + libdir + 'com/mojang/javabridge/1.2.24/javabridge-1.2.24.jar:'
  + libdir + 'net/sf/jopt-simple/jopt-simple/5.0.4/jopt-simple-5.0.4.jar:'
  + libdir + 'io/netty/netty-all/4.1.68.Final/netty-all-4.1.68.Final.jar:'
  + libdir + 'com/google/guava/failureaccess/1.0.1/failureaccess-1.0.1.jar:'
  + libdir + 'com/google/guava/guava/31.0.1-jre/guava-31.0.1-jre.jar:'
  + libdir + 'org/apache/commons/commons-lang3/3.12.0/commons-lang3-3.12.0.jar:'
  + libdir + 'commons-io/commons-io/2.11.0/commons-io-2.11.0.jar:'
  + libdir + 'commons-codec/commons-codec/1.15/commons-codec-1.15.jar:'
  + libdir + 'com/mojang/brigadier/1.0.18/brigadier-1.0.18.jar:'
  + libdir + 'com/mojang/datafixerupper/4.1.27/datafixerupper-4.1.27.jar:'
  + libdir + 'com/google/code/gson/gson/2.8.9/gson-2.8.9.jar:'
  + libdir + 'com/mojang/authlib/3.3.39/authlib-3.3.39.jar:'
  + libdir + 'org/apache/commons/commons-compress/1.21/commons-compress-1.21.jar:'
  + libdir + 'org/apache/httpcomponents/httpclient/4.5.13/httpclient-4.5.13.jar:'
  + libdir + 'commons-logging/commons-logging/1.2/commons-logging-1.2.jar:'
  + libdir + 'org/apache/httpcomponents/httpcore/4.4.14/httpcore-4.4.14.jar:'
  + libdir + 'it/unimi/dsi/fastutil/8.5.6/fastutil-8.5.6.jar:'
  + libdir + 'org/apache/logging/log4j/log4j-api/2.17.0/log4j-api-2.17.0.jar:'
  + libdir + 'org/apache/logging/log4j/log4j-core/2.17.0/log4j-core-2.17.0.jar:'
  + lwjgl3_libs
  + libdir + 'com/mojang/text2speech/1.12.4/text2speech-1.12.4.jar:'
  + mc_directory + '/versions/' + mc_version + '/' + mc_version + '.jar',
  'net.minecraft.client.main.Main',
  '--username', username,
  '--version', mc_version,
  '--gameDir', mc_directory,
  '--assetsDir', mc_directory + '/assets',
  '--assetIndex', asset_index,
  '--uuid', uuid,
  '--accessToken', token,
  '--userType', 'mojang',
  '--versionType', 'snapshot'
]

# Start Minecraft
subprocess.call(real_command)
