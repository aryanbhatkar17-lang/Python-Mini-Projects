# Simple Inventory Management System

A lightweight, terminal-based Command Line Interface (CLI) application built in Python to track, manage, and persist product inventory. This project utilizes Python's built-in dictionaries for efficient in-memory data management and the `csv` module for local data permanence.

## 🚀 Features

- **Add Products:** Easily insert new products with quantities and prices. If a product already exists, the system automatically aggregates the stock.
- **View Inventory:** Displays a clean, tabular view of all stored items, their current quantities, and unit prices formatted in USD.
- **Update Stock:** Directly modify the inventory level of any existing product.
- **Delete Products:** Permanently remove items from the registry.
- **Search Functionality:** Quickly look up a single product's stock levels and pricing details.
- **Data Persistence:** Automatically saves the entire inventory to a local `inventory.csv` file upon exiting, ensuring data isn't lost between sessions.

## 🛠️ Tech Stack

- **Language:** Python 3.x
- **Storage Format:** CSV (Comma-Separated Values)

## 📋 Prerequisites

No external dependencies or third-party libraries are required to run this project. You only need to have Python installed on your machine.

## 💻 How to Run

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git](https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git)
   cd YOUR_REPOSITORY_NAME

2. **Execute the script:**

    ```bash
    python inventory.py


## 🔍 Usage Example
When you run the application, you will be greeted with a terminal menu:

1. Add Product
2. View Inventory
3. Update Stock
4. Delete Product
5. Search Product
6. Save & Exit

Sample Inventory View:
Current inventory:
Name            Quantity        Price
BRASS_LIGHT     50              $45.00
LED_PENDANT     120             $15.50
CHANDELIER      12              $350.00

## 💾 Data Storage
Upon choosing option 6, the program creates or updates an inventory.csv file in the same directory, structured as follows:

Product Name,Quantity,Price
BRASS_LIGHT,50,45.0
LED_PENDANT,120,15.5
CHANDELIER,12,350.0

## 📝 License
This project is open-source and available under the MIT License.