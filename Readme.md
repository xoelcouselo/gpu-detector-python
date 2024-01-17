# GPU Information Retrieval Script

This Python script provides a cross-platform solution to retrieve information about the GPU(s) installed on your system. It supports Windows, Linux, and MacOS.

## Prerequisites

- Python 3.x
- For Windows: No additional prerequisites.
- For Linux: `lspci` command-line tool.
- For MacOS: `system_profiler` command-line tool.

## Installation

```bash
pip install gputil
```

## Usage

1. Save the script (gpu_info_script.py) to your local machine.
2. Open a terminal in the script's directory.

## For Windows

```bash
python gpu_info_script.py
```

## For Linux

```bash
python gpu_info_script.py
```

## For MacOs

```bash
python gpu_info_script.py
```

## Features

- Retrieves GPU information such as name, ID, memory usage, load percentage, temperature, and more.
- Supports Windows, Linux, and MacOS.

## Troubleshooting

- If you encounter issues, ensure that Python is installed on your system.
- For Linux, make sure the lspci tool is available.
- For MacOS, ensure that the system_profiler tool is available.

## Known Issues

- The script may need adjustments based on the specific output format of the system commands.

## Contributions

Contributions are welcome! Feel free to submit issues or pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
is project is licensed under the MIT License - see the LICENSE file for details.
