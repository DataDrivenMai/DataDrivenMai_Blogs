"""
Description: A simple template for a well-structured Python script.
"""

import sys  # Standard library imports
import time

# Constants
DEFAULT_NAME = "World"

def greet(name):
    """Returns a greeting string."""
    return f"Hello, {name}!"

def main():
    """Main entry point for the script."""
    user_name = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_NAME
    print(greet(user_name))
    print(f"Current time: {time.ctime()}")

if __name__ == "__main__":
    main()
