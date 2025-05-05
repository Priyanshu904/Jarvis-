import subprocess
import sys
import socket
import traceback

def is_connected():
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=3)
        return True
    except OSError:
        return False

def run_shell(command):
    try:
        print(f"📟 Running shell command:\n{command}\n")
        result = subprocess.run(command, shell=True, text=True, capture_output=True)
        if result.stdout:
            print(f"✅ Output:\n{result.stdout}")
        if result.stderr:
            print(f"⚠️ Error:\n{result.stderr}")
    except Exception as e:
        print(f"❌ Failed to run shell command: {e}")

def run_python_code(code):
    try:
        print("🐍 Executing Python code...\n")
        exec(code, globals())
    except Exception:
        print("❌ Python execution error:")
        traceback.print_exc()

def smart_executor(response):
    response = response.strip()

    if response.startswith("python") or response.startswith("```python"):
        # Clean and extract the Python code
        code = response.replace("```python", "").replace("```", "").replace("python", "").strip()
        run_python_code(code)

    elif any(response.startswith(cmd) for cmd in ["cd", "dir", "del", "copy", "move", "pip", "curl", "wget", "echo", "mkdir", "rmdir", "start", "cls", "powershell", "winget"]):
        if any(net_tool in response for net_tool in ["pip", "curl", "wget", "winget"]) and not is_connected():
            print("🚫 This command requires internet, but you're offline.")
        else:
            run_shell(response)

    elif "\n" in response and "import " in response:
        # Likely multiline Python code
        run_python_code(response)

    elif response:
        print(f"🧠 Just a response:\n{response}")

    else:
        print("🤷‍♂️ Warp didn't return anything useful.")
