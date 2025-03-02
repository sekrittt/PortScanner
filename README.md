# 🔍 Port Scanner

![Python](https://img.shields.io/badge/Python-3.x-blue) ![License](https://img.shields.io/badge/License-MIT-green) ![Status](https://img.shields.io/badge/Status-Active-brightgreen)

A **fast and simple TCP port scanner** written in Python. This tool allows you to scan a target for open ports within a specified range.

## ⚡ Features
- Scan **single ports, multiple ports, or port ranges**.
- Uses **multithreading** for faster scanning.
- Detects open ports and retrieves basic **HTTP headers** (if applicable).
- Gracefully handles `Ctrl + C` interruption.

## 🚀 Installation
Make sure you have **Python 3** installed. You also need to install the required dependencies:

```bash
pip install termcolor
```

## 🛠️ Usage
Run the script with **root privileges** for better results.

```bash
python3 portscaner.py -t <TARGET> -p <PORTS>
```

### 📌 Examples
#### Scan a single port:
```bash
python3 portscaner.py -t 192.168.1.1 -p 80
```

#### Scan multiple ports:
```bash
python3 portscaner.py -t 192.168.1.1 -p 22,80,443
```

#### Scan a range of ports:
```bash
python3 portscaner.py -t 192.168.1.1 -p 1-1000
```

## ⚙️ How It Works
1. Creates a **TCP socket** and attempts to connect to the specified ports.
2. If the port is open, it **prints the status**.
3. If the port is HTTP-related (`80`, `443`, `8080`), it sends an **HTTP HEAD request** and prints the response headers.
4. Uses **ThreadPoolExecutor** to speed up the scanning process.

## 🚑 Stopping the Scan
To stop the scanner at any time, press **`Ctrl + C`**.

## 🐜 License
This project is licensed under the **MIT License**.

## 🤝 Contributing
Pull requests are welcome! If you find a bug or have a feature request, feel free to open an issue.

---
Made with ❤️ by [FJLdx](https://github.com/FJLdx)
