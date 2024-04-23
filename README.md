Task

Log Analysis and Monitoring Script
Objective:
Create a script that automates the analysis and monitoring of log files
Requirements:
● Write the script using bash shell / Python scripting.
● Implement basic log analysis and monitoring functionalities.
● Include error handling and logging to provide feedback on script execution.
Tasks:
Log File Monitoring:
● Write a script that continuously monitors a specified log file for new entries.
● Use tail or similar commands to track and display new log entries in real time.
● Implement a mechanism to stop the monitoring loop (e.g., using a signal like Ctrl+C).
Log Analysis:
● Enhance the script to perform basic analysis on log entries:
● Count occurrences of specific keywords or patterns (e.g., error messages, HTTP status codes).
● Generate summary reports (e.g., top error message)



To run the Python script:

Open a terminal or command prompt.
Navigate to the directory containing the downloaded github repo.
Run the script by typing python log_monitor.py.


What the script does:

It sets up logging configuration to log information to a file named "monitor.log".
It defines a function signal_handler to handle the Ctrl+C signal, which logs a message and exits gracefully when the user interrupts the program.
It defines a function monitor_log to monitor a specified log file (log_file) for new entries, count occurrences of specific keywords (in this case, the word "ERROR"), and generate summary reports of error messages.
Within the monitor_log function, it continuously reads lines from the log file, checks for the presence of the keyword "ERROR", and if found, it appends the error message to a list.
If any errors are detected, it generates a summary report of the most common error message and its occurrence count.
If the specified log file is not found, it logs an error message and exits.
If any other unexpected errors occur during execution, it logs an error message and exits.
