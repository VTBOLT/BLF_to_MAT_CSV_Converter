# BLF_to_MAT_Converter
BLF to MAT (and now CSV!) file conversion using Python

`.blf input`: a logging file proprietary to Vector products (i.e. CANoe, CANalyzer, LoggerConfigurator, etc.) This format keeps track of the exact moment each variable (defined by the .dbc file) was sent on the physical CAN bus.

`.mat output`: one-to-one conversion, each variable is paired with the exact timestamp it was sent on CAN.

`.csv output`: interpolated data (default 10ms timestep), so each variable shares the same time axis.

## On Windows:
Download python 3.11 online, then: <br>
Open up command prompt: (might have to use 'py' instead of 'python')
```
git clone https://github.com/VTBOLT/BLF_to_MAT_CSV_Converter
cd BLF_to_MAT_CSV_Converter
python -m venv converter-venv
./converter-venv/Scripts/activate.bat
pip install -r requirements.txt
python blf_to_csv.py 
```
## On Linux:
Open up your preferred shell:
```
sudo apt install python3
sudo apt install python3-venv
git clone https://github.com/VTBOLT/BLF_to_MAT_CSV_Converter
cd BLF_to_MAT_CSV_Converter
python3 -m venv converter-venv
source ./converter-venv/bin/activate
pip install -r requirements.txt
python3 blf_to_csv.py 
```

## Updating the CAN variable database
Replace the database (.dbc and .ini) files in `./put-database-here` 

## Viewing more detailed progress & reading error messages
View the terminal during execution, it has more details than the GUI window.
