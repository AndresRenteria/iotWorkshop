import time
import pyupm_grove as grove
import pyupm_buzzer as upmBuzzer
# Create the button object using GPIO pin 0
button = grove.GroveButton(4)
# Read the input and print, waiting one second between readings
while 1:
    print button.name(), ' value is ', button.value()
    time.sleep(1)
buzzer = upmBuzzer.Buzzer(5)

chords = [upmBuzzer.DO, upmBuzzer.RE, upmBuzzer.MI, upmBuzzer.FA, 
          upmBuzzer.SOL, upmBuzzer.LA, upmBuzzer.SI, upmBuzzer.DO, 
          upmBuzzer.SI];

# Print sensor name
print buzzer.name()

# Play sound (DO, RE, MI, etc.), pausing for 0.1 seconds between notes
if(button.value() == 1){
	for chord_ind in range (0,7):
    # play each note for one second
    	print buzzer.playSound(chords[chord_ind], 1000000)
    	time.sleep(0.1)
    }

print "exiting application"


del button
del buzzer
