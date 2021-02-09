#!/usr/local/bin/python3

import minecraft_launcher_lib
import subprocess

desired_version = "1.12.2"

# Your email, username and password below
login = "yourEmailUsername"
password = "seekritPasswordHere"

# Get Minecraft directory
minecraft_directory = minecraft_launcher_lib.utils.get_minecraft_directory()

library_directory = minecraft_directory + "/libraries/"

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

real_command = ['/usr/local/jdk-11/bin/java', '-Djava.library.path=/usr/local/share/lwjgl/', '-Xms1G', '-Xmx2G', '-XX:-UseAdaptiveSizePolicy', '-Xmn256M', '-cp', library_directory + 'com/mojang/patchy/1.1/patchy-1.1.jar:' + library_directory + 'oshi-project/oshi-core/1.1/oshi-core-1.1.jar:' + library_directory + 'net/java/dev/jna/jna/4.4.0/jna-4.4.0.jar:' + library_directory + 'net/java/dev/jna/platform/3.4.0/platform-3.4.0.jar:' + library_directory + 'com/ibm/icu/icu4j-core-mojang/51.2/icu4j-core-mojang-51.2.jar:' + library_directory + 'net/sf/jopt-simple/jopt-simple/5.0.3/jopt-simple-5.0.3.jar:' + library_directory + 'com/paulscode/codecjorbis/20101023/codecjorbis-20101023.jar:' + library_directory + 'com/paulscode/codecwav/20101023/codecwav-20101023.jar:' + library_directory + 'com/paulscode/libraryjavasound/20101123/libraryjavasound-20101123.jar:' + library_directory + 'com/paulscode/librarylwjglopenal/20100824/librarylwjglopenal-20100824.jar:' + library_directory + 'com/paulscode/soundsystem/20120107/soundsystem-20120107.jar:' + library_directory + 'io/netty/netty-all/4.1.9.Final/netty-all-4.1.9.Final.jar:' + library_directory + 'com/google/guava/guava/21.0/guava-21.0.jar:' + library_directory + 'org/apache/commons/commons-lang3/3.5/commons-lang3-3.5.jar:' + library_directory + 'commons-io/commons-io/2.5/commons-io-2.5.jar:' + library_directory + 'commons-codec/commons-codec/1.10/commons-codec-1.10.jar:' + library_directory + 'net/java/jinput/jinput/2.0.5/jinput-2.0.5.jar:' + library_directory + 'net/java/jutils/jutils/1.0.0/jutils-1.0.0.jar:' + library_directory + 'com/google/code/gson/gson/2.8.0/gson-2.8.0.jar:' + library_directory + 'com/mojang/authlib/1.5.25/authlib-1.5.25.jar:' + library_directory + 'com/mojang/realms/1.10.22/realms-1.10.22.jar:' + library_directory + 'org/apache/commons/commons-compress/1.8.1/commons-compress-1.8.1.jar:' + library_directory + 'org/apache/httpcomponents/httpclient/4.3.3/httpclient-4.3.3.jar:' + library_directory + 'commons-logging/commons-logging/1.1.3/commons-logging-1.1.3.jar:' + library_directory + 'org/apache/httpcomponents/httpcore/4.3.2/httpcore-4.3.2.jar:' + library_directory + 'it/unimi/dsi/fastutil/7.1.0/fastutil-7.1.0.jar:' + library_directory + 'org/apache/logging/log4j/log4j-api/2.8.1/log4j-api-2.8.1.jar:' + library_directory + 'org/apache/logging/log4j/log4j-core/2.8.1/log4j-core-2.8.1.jar:/usr/local/share/lwjgl/lwjgl.jar:/usr/local/share/lwjgl/lwjgl_util.jar:/usr/local/share/lwjgl/jinput.jar:' + library_directory + 'com/mojang/text2speech/1.10.3/text2speech-1.10.3.jar:' + minecraft_directory + '/versions/1.12.2/1.12.2.jar', 'net.minecraft.client.main.Main', '--username', username, '--version', '1.12.2', '--gameDir', minecraft_directory, '--assetsDir', minecraft_directory + '/assets', '--assetIndex', '1.12', '--uuid', uuid, '--accessToken', token, '--userType', 'mojang', '--versionType', 'release']

# Start Minecraft
subprocess.call(real_command)
