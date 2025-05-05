import subprocess

# Big list of popular Windows apps and their Winget IDs
known_apps = {
    "vlc": "VideoLAN.VLC",
    "chrome": "Google.Chrome",
    "firefox": "Mozilla.Firefox",
    "brave": "Brave.Brave",
    "edge": "Microsoft.Edge",
    "opera": "Opera.Opera",
    "notepad++": "Notepad++.Notepad++",
    "vscode": "Microsoft.VisualStudioCode",
    "visual studio code": "Microsoft.VisualStudioCode",
    "discord": "Discord.Discord",
    "spotify": "Spotify.Spotify",
    "zoom": "Zoom.Zoom",
    "whatsapp": "WhatsApp.WhatsApp",
    "telegram": "Telegram.TelegramDesktop",
    "obs": "OBSProject.OBSStudio",
    "steam": "Valve.Steam",
    "epic games": "EpicGames.EpicGamesLauncher",
    "battle.net": "Blizzard.BattleNet",
    "gimp": "GIMP.GIMP",
    "krita": "KDE.Krita",
    "audacity": "Audacity.Audacity",
    "blender": "BlenderFoundation.Blender",
    "python": "Python.Python.3.11",
    "java": "Oracle.JavaRuntimeEnvironment",
    "node.js": "OpenJS.NodeJS",
    "git": "Git.Git",
    "docker": "Docker.DockerDesktop",
    "xampp": "ApacheFriends.Xampp",
    "7zip": "7zip.7zip",
    "winrar": "RARLab.WinRAR",
    "postman": "Postman.Postman",
    "android studio": "Google.AndroidStudio",
    "mysql": "Oracle.MySQL",
    "mongodb compass": "MongoDB.Compass.Full",
    "powershell": "Microsoft.PowerShell",
    "teams": "Microsoft.Teams",
    "skype": "Microsoft.Skype",
    "qbittorrent": "qBittorrent.qBittorrent",
    "tor browser": "TorProject.TorBrowser",
    "obsidian": "Obsidian.Obsidian"
}

def install_app(app_name):
    app_id = known_apps.get(app_name.lower())

    if app_id:
        print(f"📦 Installing {app_name}...")
        try:
            subprocess.run(["winget", "install", "--id", app_id, "-e", "--silent"])
            print("✅ Done installing.")
        except Exception as e:
            print("❌ Error installing:", e)
    else:
        print("❌ I don’t know this app. Maybe add it to known_apps.")
