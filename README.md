# 🗣️ AlexCipher: Your Digital Voice Companion

**AlexCipher** is an interactive, Python-based digital voice assistant designed to perform encryption and decryption tasks using classical ciphers.

## ✨ Introduction

In an era where secure communication is vital, AlexCipher combines the timeless principles of classical cryptography with modern, cutting-edge voice interaction technology. By leveraging voice recognition, this application offers users a seamless, hands-free experience for secure communication while fostering a deeper understanding of algorithmic complexity.

## 🎯 Project Objective

The primary goal is to develop a Python-based digital voice assistant, named **Alex**, capable of performing encryption and decryption tasks using voice commands.

### Detailed Objectives:

**Voice-Activated Interaction:** Implement functionality for hands-free command execution.
**Encryption and Decryption Algorithms:** Integrate multiple classical ciphers.
**User Experience and Interaction:** Ensure a user-friendly and accessible tool.
**Educational Value:** Provide insights into the intricacies of encryption.
**Security and Privacy:** Provide practical tools for secure communication.

## 🔑 Integrated Algorithms

AlexCipher integrates the following four classical encryption and decryption algorithms:

1.  **Caesar Cipher** 
2.  **Atbash Cipher** 
3.  **ROT13 Cipher** 
4.  **Affine Cipher** 

## 🛠️ How It Works

The application is built in **Python** and implemented using **PyCharm**. It follows a simple, voice-command-driven workflow:

### Step 1: Set Up the Development Environment
Ensure **Python** is installed.
Install required libraries using `pip:
    ```bash
    pip install speechrecognition pyaudio pyttsx3
    ```

### Step 2: Implement Voice Recognition and Synthesis
**Voice Recognition:** Uses the `speech_recognition` library to convert user speech into text commands.
**Voice Synthesis:** Uses the `pyttsx3` library to convert the system's text responses back into speech (the voice of Alex).

### Step 3: Implement Encryption and Decryption Algorithms
Individual functions are developed for the Caesar, Atbash, ROT13, and Affine Ciphers.

### Step 4: Integrate Voice Commands
Voice commands are parsed to trigger the appropriate encryption or decryption function.
* Users can initiate a request by saying, for example:
    > "Alex, what is the encrypted/decrypted word of (your word) using Cipher A, Cipher B, Cipher C, or Cipher D, where Cipher A is Caesar, B Atbash, C is Rot13, and Cipher D is Affine".

### Step 5: Test and Refine
* The application is tested with various inputs to ensure each function works correctly, followed by debugging.
