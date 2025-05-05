import os

def create_file(file_path):
    with open(file_path, 'w') as f:
        f.write('')
    print(f"✅ Created file: {file_path}")

def delete_file(file_path):
    try:
        os.remove(file_path)
        print(f"🗑️ Deleted file: {file_path}")
    except FileNotFoundError:
        print("⚠️ File not found.")
    except Exception as e:
        print(f"❌ Error deleting file: {e}")

def create_folder(folder_path):
    os.makedirs(folder_path, exist_ok=True)
    print(f"📁 Created folder: {folder_path}")

def delete_folder(folder_path):
    try:
        os.rmdir(folder_path)
        print(f"🗑️ Deleted folder: {folder_path}")
    except FileNotFoundError:
        print("⚠️ Folder not found.")
    except Exception as e:
        print(f"❌ Error deleting folder: {e}")

def list_contents(folder_path):
    try:
        files = os.listdir(folder_path)
        print("📂 Folder contents:")
        for f in files:
            print(f" - {f}")
    except FileNotFoundError:
        print("⚠️ Folder not found.")
