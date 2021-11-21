# hot_chocolate

## Setup

To setup the repo to work with Python3, you need to do the following.

```
cd /home # Go to home directory
sudo mkdir python-envs # Create folder for virtual python environment
sudo chown -R <your-linux-username> python_envs # Makes you the owner of the folder
sudo python3 -m venv ros-melodic # Create python virtual environment
source ros-melodic/bin/activate # Source the python version in the virtual environment
```

To install the required python dependencies, run the following.

```
pip install --upgrade pip  # Upgrade pip
pip install opencv-python  # Install opencv
pip install rospkg         # Install ros packages
```