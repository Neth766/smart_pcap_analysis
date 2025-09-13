---

# 📦 PacketProbe – Smart PCAP Analyzer  

PacketProbe is a simple yet powerful Python tool to analyze `.pcap` files (packet capture files).  
It’s built using **Scapy** and designed with a **colorful CLI** for an engaging experience.  

This tool is perfect for learning **network analysis basics**, exploring traffic in a `.pcap` file,  
and showcasing a clean, well-documented project.  

---

## 🚀 Features

- ✅ Counts total number of packets  
- ✅ Lists unique IP addresses (top 10 shown)  
- ✅ Displays protocol distribution (TCP/UDP/ICMP/Other)  
- ✅ Finds **Top 5 talkers** (most active IPs)  
- ✅ Shows **packet size stats** (smallest, largest, average)  
- ✅ Colorful, human-friendly terminal output  
- ✅ Built-in dependency checker (auto-installs missing modules if you want)  
- ✅ Uses a default `sample.pcap` if no file is provided  

---

## 📂 Repository Structure

```

PacketProbe/
│── PacketProbe.py         # Main script
│── sample.pcap            # Example PCAP file for testing
│── requirements.txt       # Dependencies
│── README.md              # Project documentation

````

---

🛠 Installation

Clone this repository:

```bash
git clone https://github.com/yourusername/PacketProbe.git
cd PacketProbe
```

You can install dependencies in two ways:

Manual installation
```bash
pip install -r requirements.txt
```

Auto-install feature (recommended)
Just run the script normally:
```bash
python PacketProbe.py sample.pcap
```

If modules like scapy or colorama are missing, the script will detect it.

It will then ask:

Missing dependencies detected:
  - scapy
  - colorama
Do you want to auto-install them now? (y/n):

If you type y, it will auto-install the required modules for you.

If you type n, it will exit gracefully with instructions to install manually.

This makes life easier for reviewers and ensures nobody gets stuck on “ModuleNotFoundError.” ✅

***
OR
***
All required modules are listed in `requirements.txt`. You can install them manually with:
```bash
pip install -r requirements.txt
```
---

## ▶️ Usage

### Option 1 – Analyze your own `.pcap` file

```bash
python PacketProbe.py path/to/yourfile.pcap
```

### Option 2 – Use the included `sample.pcap`

```bash
python PacketProbe.py
```

---
## ⚙️ How PacketProbe Works

PacketProbe follows a simple step-by-step workflow:

1. **Load the PCAP file**  
   - If you provide a file path (`python PacketProbe.py yourfile.pcap`), it uses that.  
   - If not, it defaults to `sample.pcap` in the same folder.  
   - Scapy’s `rdpcap()` function reads all packets into memory.

2. **Go through each packet**  
   - For every packet, it checks if the **IP layer** exists.  
   - If yes, it extracts the **source and destination IPs**.  
   - It also checks which **protocol** the packet belongs to (TCP, UDP, ICMP, or Other).

3. **Keep counts with Counters**  
   - A **Counter** object keeps track of how many times each IP address appears.  
   - Another Counter stores how many packets belong to each protocol.  

4. **Calculate stats**  
   - Total packets in the file  
   - Unique IPs seen (top 10 printed for clarity)  
   - Protocol distribution  
   - Top 5 “talkers” (most active IPs)  
   - Packet size statistics: smallest, largest, average  

5. **Present results nicely**  
   - Uses **Colorama** to make text colorful and easy to read.  
   - Organizes the output into sections (IP list, protocols, top talkers, stats).  
   - Ends with a friendly completion message ✅  

---

### 📝 Example in Plain English

Imagine your PCAP has 100 packets:
- 70 are TCP, 20 are UDP, 10 are ICMP.  
- 192.168.1.2 sends 50 packets, 192.168.1.3 sends 30, and others send fewer.  
- The smallest packet is 60 bytes, the largest is 1514, and the average is ~300.  

PacketProbe will summarize this for you in a **clear, colorful report** instead of dumping raw packet data.



## 📊 Example Output

Here’s how PacketProbe looks in action:

```
=======================================================
🔍 Welcome to PacketProbe - Smart PCAP Analyzer
=======================================================

📂 File loaded: sample.pcap
[*] Total packets: 105

🌐 Unique IP addresses: 6
   192.168.1.2
   192.168.1.3
   8.8.8.8
   142.250.77.14
   ...

📊 Protocol distribution:
   TCP: 65
   UDP: 30
   ICMP: 10

💬 Top 5 Talkers (most packets):
   192.168.1.2 -> 55 packets
   192.168.1.3 -> 25 packets
   8.8.8.8     -> 10 packets
   ...

📏 Packet size stats:
   Smallest: 60 bytes
   Largest : 1514 bytes
   Average : 278.45 bytes

✅ Analysis complete! Thanks for using PacketProbe 🚀
```

---

## 🧑‍💻 Behind the Scenes

PacketProbe uses [Scapy](https://scapy.net/) to parse packets and extract IP + protocol details.
It’s intentionally written at an **intermediate level**:

* Easy enough to understand for students or beginners in cybersecurity
* Structured and documented like a real-world project

---

## 📌 Requirements

* Python 3.8+
* Modules: `scapy`, `colorama`

You can install them manually:

```bash
pip install scapy colorama
```

Or just use:

```bash
pip install -r requirements.txt

```
*Recommended for most beginners:
Use auto-install_requirements.py to avoid complications.
---

## ⚠️ Notes

* If required modules are missing, using the auto-install_requirements.py will **detect and prompt you** to install them.
* Works best in a terminal that supports Unicode + colors.
* This is a **learning project**, not a full-fledged IDS/IPS.

---

## 🎯 Why this project?

This project was made as part of a **Cybersecurity Club Task** to analyze PCAP files.
Instead of just writing a bare minimum script, the goal was to create something:

* **Professional-looking**
* **Easy to use**
* **Visually appealing**
* **Educational for others who read the code**

---

📌 Note from the Author

This project is part of my student learning journey in cybersecurity and Python programming.
It is designed to be both educational and practical, but please keep in mind:

Some errors may occur depending on your system setup or Python environment.

I’ve included features like the auto-install script to make it easier to get started, but issues can still happen on different devices.

If something doesn’t work as expected, it’s not you — it’s probably me still learning 😊.

💡 If you face any problems:

Feel free to open an issue in the repository.

You can also raise questions, and I’ll respond as soon as possible.

Your feedback not only helps improve this project but also helps me learn and grow as a developer.

---
## 🙌 Acknowledgements

* [Scapy](https://scapy.net/) – the backbone for packet parsing
* [Colorama](https://pypi.org/project/colorama/) – for colorful terminal output
* Inspired by tools like Wireshark and tshark

---

## 📜 License

This project is licensed under the **MIT License** — see the [LICENSE](./LICENSE) file for details.

Feel free to fork, modify, and share your improvements! 🚀


---


