# 🚀 Distributed Factorial Computing System

This project demonstrates a **distributed high-performance computing system** for calculating extremely large factorials.  
Instead of letting one machine compute `N!` (which becomes very slow for huge N), the workload is **split across multiple clients**.  
Each client handles a portion of the factorial, and the server combines the results.

---

## 🔧 How It Works

### **1. Server**
- Accepts:
  - Target number **N**
  - Number of client machines
- Splits the range (1..N) into equal parts
- Sends each client a task using compressed serialized data
- Waits for partial results from all clients
- Merges the results using `math.prod()`
- Saves the final factorial into `distributed_result.txt`
- Logs performance metrics in `stats.txt`

### **2. Clients**
- Wait for a task from the server
- Compute the partial factorial for their assigned range
- Send the result back to the server
- Support compressed & serialized communication for efficiency

---

## 📌 Features
- ⚡ Distributed parallel computation  
- 📡 Client-server architecture using `socket`  
- 🗜️ Efficient data transfer (`pickle` + `zlib`)  
- 🧮 Handles extremely large integers  
- 📊 Performance logging  
- 🔐 Stable communication protocol  

---

## 🧠 Why This Project Matters
Calculating large factorials (e.g., 100,000!) is extremely slow on a single machine.  
This project solves that by **splitting the computation among multiple devices**, making it faster and scalable.

This is similar to how large systems like cloud services and scientific simulations distribute workloads.

---

## 🛠️ Technologies Used
- Python  
- Sockets (TCP)  
- Multithreading  
- Zlib compression  
- Pickle serialization  

---

## 📂 Project Structure
