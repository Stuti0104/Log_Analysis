#ECHO is on
import os
import signal
import time
import logging
from collections import Counter

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s', filename='monitor.log')

# Function to handle Ctrl+C signal
def signal_handler(sig, frame):
    logging.info("Monitoring stopped by user")
    exit(0)

# Function to monitor log file, count occurrences of specific keywords, and generate summary reports
def monitor_log(log_file):
    logging.info("Monitoring started for file: {}".format(log_file))
    
    # Define keywords or patterns to count occurrences
    error_messages = []

    try:
        with open(log_file, 'r') as file:
            while True:
                where = file.tell()
                line = file.readline()
                if not line:
                    time.sleep(0.1)
                    file.seek(where)
                else:
                    logging.info("New log entry: {}".format(line.strip()))
                    
                    # Check for specific keywords or patterns
                    if "ERROR" in line:
                        error_messages.append(line.strip())

                    # Generate summary reports
                    if len(error_messages) > 0:
                        error_counts = Counter(error_messages)
                        top_error_message, top_error_count = error_counts.most_common(1)[0]
                        logging.info("Top error message: '{}' ({} occurrences)".format(top_error_message, top_error_count))
    except FileNotFoundError:
        logging.error("Log file not found: {}".format(log_file))
        exit(1)
    except Exception as e:
        logging.error("An error occurred: {}".format(str(e)))
        exit(1)

if __name__ == "__main__":
    try:
        # Register signal handler for Ctrl+C
        signal.signal(signal.SIGINT, signal_handler)

        # Specify the log file to monitor
        log_file = "example.log"

        # Start monitoring the log file
        monitor_log(log_file)
    except Exception as e:
        logging.error("An error occurred: {}".format(str(e)))
        exit(1)
