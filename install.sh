#!/bin/bash

# Function to install Python and pip if not already installed
install_python_and_pip() {
    if ! command -v python3 &>/dev/null; then
        echo "Python not found on board. Beginning Installation..."
        echo "Debian based os. Installing Python now..."
        # Add commands to install Python here
        sudo apt-get update && sudo apt-get install -y python3
    fi

    if ! command -v pip3 &>/dev/null; then
        echo "pip not found on board. Beginning Installation..."
        # Add commands to install pip here
        sudo apt-get install -y python3-pip
    fi
}

# Function to install project dependencies using setup.py
install_dependencies() {
    echo "Installing project dependencies..."
    pip3 install .
}

# Function to run Python script to create SQLite database
run_python_script() {
    echo "Running Python script to create SQLite database..."
    python3 /home/pi/osage/db.py
}

# Function to add cron job to run the Python program on startup
add_cron_job() {
    echo "Adding cron job..."
    (crontab -l ; echo "@reboot sleep 45 && /home/pi/osage/main.py") | crontab -
}

# Function to reboot the system
reboot_system() {
    echo "Rebooting system..."
    sudo reboot
}

# Main function to orchestrate the deployment process
main() {
    install_python_and_pip
    install_dependencies
    run_python_script
    add_cron_job
    reboot_system
}

# Execute main function
main
