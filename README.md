# AES - Student #2 Substitute Bytes

This project implements the SubBytes step of AES (Advanced Encryption Standard).

Student: #2  
Topic: Substitute Bytes  

## What is AES?

AES (Advanced Encryption Standard) is a symmetric encryption algorithm used to protect data.

It works with blocks of 16 bytes (4x4 matrix) and applies different transformations in rounds.

One of these transformations is SubBytes.

## What is SubBytes?

SubBytes is a substitution step.

It replaces each byte in the 4x4 state matrix using a special table called S-Box.

The S-Box contains 256 values (16x16 table).

Each byte is divided into:
- First hex digit → row
- Second hex digit → column

Then the value in that position replaces the original byte.

Example:

If the byte is:
0x53

Row = 5  
Column = 3  

We look in the S-Box at position [5][3].


## How the Program Works

1. The program defines an initial 4x4 matrix (state).
2. It loads the AES S-Box.
3. For each byte in the matrix:
   - It calculates the row (first 4 bits).
   - It calculates the column (last 4 bits).
   - It replaces the value using the S-Box.
4. It prints the matrix before and after SubBytes.


## Project Structure

aes-subbytes/
│
├── main.py
├── sbox.py
├── utils.py
└── README.md

## Files Description

main.py  
Contains the main function and the SubBytes implementation.

sbox.py  
Contains the AES S-Box and creates the 16x16 matrix.

utils.py  
Contains helper functions to print and manage matrices

## How to Run

Open terminal inside the project folder and run:

python main.py

## Example Output

The program prints:

- State before SubBytes
- State after SubBytes


## Conclusion

This project demonstrates how the SubBytes step works in AES encryption.

It shows how each byte is substituted using the S-Box table.

This is one of the four main transformations in AES.
