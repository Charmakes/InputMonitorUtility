import input_monitor

# Initialize and configure the InputMonitor with an interval of 10 seconds, email, and password
monitor = input_monitor.InputMonitor(10, 'completeinputmonitorproject@gmail.com', 'YourSecurePassword')

# Start monitoring input and sending periodic reports
monitor.start()
