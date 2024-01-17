import GPUtil
import platform
import subprocess

def get_gpu_info_windows():
    try:
        result = subprocess.run(["wmic", "path", "win32_videocontroller", "get", "/format:list"], capture_output=True, text=True)
        print("GPU Information on Windows:")
        print(result.stdout)

    except Exception as e:
        print(f"Error retrieving GPU information on Windows: {e}")

def get_gpu_info_linux():
    try:
        result = subprocess.run(["lspci", "-v", "-nn"], capture_output=True, text=True)
        print("GPU Information on Linux:")
        print(result.stdout)

    except Exception as e:
        print(f"Error retrieving GPU information on Linux: {e}")

def get_gpu_info_macos():
    try:
        result = subprocess.run(["system_profiler", "SPDisplaysDataType"], capture_output=True, text=True)
        gpu_info_start = result.stdout.find("Graphics/Displays:") + len("Graphics/Displays:")
        gpu_info_end = result.stdout.find("USB 3.0 Bus:")
        gpu_info = result.stdout[gpu_info_start:gpu_info_end].strip()
        print("GPU Information on MacOS:")
        print(gpu_info)

    except Exception as e:
        print(f"Error retrieving GPU information on MacOS: {e}")

def get_gpu_info():
    system = platform.system()

    if system == "Windows":
        get_gpu_info_windows()
    elif system == "Linux":
        get_gpu_info_linux()
    elif system == "Darwin":
        get_gpu_info_macos()
    else:
        print(f"Unsupported operating system: {system}")

if __name__ == "__main__":
    get_gpu_info()
