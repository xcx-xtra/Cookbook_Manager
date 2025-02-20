# Cookbook_Manager
Hipster Cookbook Database 

## Features Implemented
This project implements the following features:

1. **Cookbook Borrowing Tracker**
   - Tracks borrowed cookbooks, including the friend's name and borrowing date.
   - Stores records in a separate `borrowed_cookbooks` table.
   - Allows for tracking return dates (future enhancement).

2. **Aesthetic Photoshoot Planning**
   - Generates Instagram-worthy photo layout suggestions based on cover color and aesthetic rating.
   - Suggests ideal photo angles.
   - Recommends props based on the cookbook theme.
   - Provides relevant hashtags for social media sharing.

## Additional Features
- **Database Setup:** Automatically creates necessary SQLite tables upon execution.
- **Error Handling & Input Validation:** Prevents invalid inputs and handles database errors gracefully.
- **Pre-populated Test Data:** Example function calls are included for easy testing.

## How to Run the Code
1. **Ensure you have Python installed** (version 3.6 or later recommended).
2. **Install SQLite** if not already included with Python.
3. **Run the script** in a terminal or command prompt:
   ```bash
   python script_name.py
   ```
4. The program will:
   - Create the required database tables if they don't exist.
   - Track a borrowed cookbook.
   - Generate a photoshoot plan.
   - Close the database connection upon completion.

## Known Limitations or Issues
- **No User Interface:** Currently, interaction is through function calls within the script.
- **Limited Borrowing Tracker Features:** No function yet to update return dates.
- **Photoshoot Plan Improvements:** Does not yet consider multiple cover color themes per book.
- **Database Persistence:** Uses a local SQLite database, which may not be suitable for web-based applications.



