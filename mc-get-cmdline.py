#!/usr/local/bin/python3

import minecraft_launcher_lib as mll
import subprocess

# Minecraft version
mc_version = "fabric-loader-0.11.3-1.16.5"

# Asset index is same but without final revision
asset_index = "1.16"

# Your email, username and password below
login    = "yourEmailUsername"
password = "seekritPasswordHere"

# Get Minecraft directory
mc_directory = mll.utils.get_minecraft_directory()

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
options = {
    "username": login_data["selectedProfile"]["name"],
    "uuid":     login_data["selectedProfile"]["id"],
    "token":    login_data["accessToken"]
}
minecraft_command = mll.command.get_minecraft_command(mc_version,mc_directory,options)

print(minecraft_command)
