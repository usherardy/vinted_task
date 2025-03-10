# Vinted Shipment Discount Processor

## Overview
This project processes shipment transactions and applies discount rules according to predefined business logic. It ensures correct discount application while maintaining a monthly discount cap.

---

## Features
- Automated discount calculation for shipments.
- Handles different shipment providers and sizes dynamically.
- Modular and structured code with separation of concerns.
- Exception handling for invalid or malformed inputs.
- Configurable discount rules without modifying core logic.
- Includes unit tests to ensure correctness.

---

## Installation & Setup

### 1. Clone the Repository
```sh
git clone https://github.com/usherardy/vinted_task_2025.git
cd vinted-task
```

## How to Use

### 1. Prepare the Input File (`input.txt`)
Each line should be formatted as:
```
YYYY-MM-DD Size Provider
```
**Example Input (`input.txt`):**
```
2025-01-01 S LP
2025-01-02 L MR
2025-01-03 M LP
2025-01-04 S MR
2025-01-05 L LP
```

### 2. Run the Script
```sh
python main.py
```
This will read `input.txt`, process each shipment, and save the results in `output.txt`.

### 3. Check the Output
**Example Output (`output.txt`):**
```
2025-01-01 S LP 1.50 -
2025-01-02 L MR 4.00 -
2025-01-03 M LP 4.90 -
2025-01-04 S MR 2.00 -
2025-01-05 L LP 0.00 6.90
```
(The **third "L" shipment from LP is free** due to the discount rule.)

---

## Discount Rules Implemented
### 1. Cheapest "S" Package Discount
   - If the same size is available from another provider at a lower price, the customer is charged the lowest available price.

### 2. Every 3rd "L" Size Shipment from LP is Free
   - The third "L" size shipment from "LP" in a given month is free.

### 3. Monthly Discount Cap
   - Discounts are capped at **€10 per month** to prevent excessive deductions.

---

## Project Structure
```
vinted-task/
│── constants.py              # Stores predefined constants (prices, providers, etc.)
│── discount_engine.py        # Handles discount logic
│── shipment_processor.py     # Processes input and applies discounts
│── transaction.py            # Represents a single shipment transaction
│── main.py                   # Main script for reading input and writing output
│── input.txt                 # Sample input file
│── output.txt                # Processed output file
│── test_input_validation.py  # Unit tests for validation
│── README.md                 # Project documentation
```

---

## Running Tests
To verify that the program functions correctly, you can run the unit tests:

```sh
python -m unittest discover tests
```

