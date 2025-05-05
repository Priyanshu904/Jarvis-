from brain import ask_warp
from executor import smart_executor
from modules import file_manager, app_installer, youtube_tools
from modules import ocr_tools
import socket

def is_connected():
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=3)
        return True
    except OSError:
        return False

def main():
    print("🤖 Hello Boss. Jarvis++ online and listening...\n")

    while True:
        user_input = input("🟢 Command me:\n> ").lower()

        if user_input in ["exit", "quit", "shutdown"]:
            print("👋 Shutting down. Bye boss.")
            break

        # File management
        elif "create file" in user_input:
            filename = user_input.replace("create file", "").strip()
            if filename:
                file_manager.create_file(filename)
            else:
                print("⚠️ Please provide a filename.")

        elif "delete file" in user_input:
            filename = user_input.replace("delete file", "").strip()
            if filename:
                file_manager.delete_file(filename)
            else:
                print("⚠️ Please provide a filename.")

        elif "create folder" in user_input or "make folder" in user_input:
            folder = user_input.replace("create folder", "").replace("make folder", "").strip()
            if folder:
                file_manager.create_folder(folder)
            else:
                print("⚠️ Folder name missing. Try: 'create folder MyFolder'")

        elif "delete folder" in user_input:
            folder = user_input.replace("delete folder", "").strip()
            if folder:
                file_manager.delete_folder(folder)
            else:
                print("⚠️ Please provide a folder name.")

        elif "list folder" in user_input or "show files in" in user_input:
            folder = user_input.replace("list folder", "").replace("show files in", "").strip()
            if folder:
                file_manager.list_contents(folder)
            else:
                print("⚠️ Please specify a folder to list.")

        # App installation
        elif "install" in user_input:
            app = user_input.replace("install", "").strip()
            if app:
                app_installer.install_app(app)
            else:
                print("⚠️ Please provide an app name.")

        # YouTube tools (requires internet)
        elif "download youtube" in user_input:
            if is_connected():
                link = user_input.replace("download youtube", "").strip()
                if link:
                    youtube_tools.download_video(link)
                else:
                    print("⚠️ Please provide a YouTube link.")
            else:
                print("❌ No internet connection for YouTube download.")
               
               
                # OCR: Extract text from an image
        elif "extract text from image" in user_input:
            image_path = user_input.replace("extract text from image", "").strip()
            text = ocr_tools.extract_text_from_image(image_path)
            print(f"\nExtracted Text:\n{text}")

        # Default: let Warp handle it
        else:
            print("🤔 Thinking locally with Warp...")
            system_prompt = """
You're a personal AI assistant on Windows. Take natural language and return:
- A shell command (PowerShell/CMD) if needed
- A Python code snippet for tasks like file handling or hacking
- A short spoken answer if no action is needed
"""
            prompt = f"{system_prompt}\nUser: {user_input}"
            response = ask_warp(prompt).strip()

            print(f"\n💡 Warp says:\n{response}")
            confirm = input("⚠️ Run this? (yes/no): ").lower()
            if confirm == "yes":
                smart_executor(response)
            else:
                print("❌ Skipped.")

if __name__ == "__main__":
    main()
