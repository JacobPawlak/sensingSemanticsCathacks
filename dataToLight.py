import sys

def main():

	args = sys.argv
        if(len(args) != 2):
                print('usage: \"python dataToLight.py filename\"')
                return -1
	
	greens = []
	reds = []
	yellow = []
	blue = []

	txtData = open(args[1], 'r')
	
	counter = 0

	for row in txtData:
		if(counter != 0):	
			vals = row.split(',')
			greens.append( int((float(vals[0]) * 16) + .5))
			reds.append( int((float(vals[1]) * 16) + .5))
			counter += 1
		else:
			vals = row.split(',')
			blue.append( int((float(vals[0]) * 16) + .5))
			yellow.append( int((float(vals[1]) * 16) + .5))
			counter += 1
#	print(greens)
#	print(reds)
#	print(yellow)
#	print(blue)
	
	namer = args[1].split('.')
	lightFile = open('lightDisplay-' + str(namer[0]) + '.pde', 'w')
	
	lightFile.write("//Jacob Pawlak and Ryan Shah\n")
	lightFile.write("//Cathacks and EKU Symposium 2016\n")
	lightFile.write("#include <avr/pgmspace.h>" + "\n \n" + "#define CUBESIZE 4" + "\n" + "#define PLANESIZE 16" + "\n" + "#define PLANETIME 3333" + "\n" + "#define TIMECONST 5" + "\n \n")
	lightFile.write("int LEDPin[16] = {0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15}; \n")
	lightFile.write("int LEDPinCount = 16; \n")
	lightFile.write("int PlanePin[4] = {16,17,18,19}; \n")
	lightFile.write("int PlanePinCount = 4; \n \n")
	GR = "{"
	for val in greens:
		GR += str(greens[val]) + ","
	GR = GR[:-1]
	GR += "}"
	lightFile.write("int greens[" + str(len(greens)) + "] = " + GR + ";" + "\n")

	RD = "{"
        for val in reds:
                RD += str(reds[val]) + ","
	RD = RD[:-1]
        RD += "}"
        lightFile.write("int reds[" + str(len(reds)) + "] = " + RD + ";" + "\n")
	
	YE = "{" + str(yellow[0]) + "}"
        lightFile.write("int yellow[" + str(len(yellow)) + "] = " + YE + ";" + "\n")

	BL = "{" + str(blue[0]) + "}"
        lightFile.write("int blue[" + str(len(blue)) + "] = " + BL + ";" + "\n")

	lightFile.write("void setup(){" + "\n" + "\t int pin;" + "\n" + "\t for(pin = 0; pin < LEDPinCount; pin++){" + "\n" + "\t\t pinMode( LEDPin[pin], OUTPUT ); }" + "\n" + "\t for(pin = 0; pin < PlanePinCount; pin++){" + "\n" + "\t\t pinMode( PlanePin[pin], OUTPUT); }" + "\n" + "}" + "\n \n")
	
	lightFile.write("void loop(){" + "\n" + "\t displayTotal();" + "\n" + "\t delay(2000);" + "\n" + "\t loopFor();" + "\n" + "\t delay(2000);" + "\n" + "}" + "\n \n")

	loopFor = ""
	displayTotal = ""
	planesOff = ""

	loopFor += "void loopFor(){" + "\n"
	loopFor += "\t planesOff();" + "\n"
	loopFor += "\t digitalWrite(PlanePin[0], HIGH);" + "\n" + "\t digitalWrite(PlanePin[3], HIGH);" + "\n"
	loopFor += "\t for(int i = 0; i < sizeof(greens); i++){" + "\n"
	loopFor += "\t\t if(greens[i] < reds[i]){" + "\n"
	loopFor += "\t\t\t digitalWrite(PlanePin[0], LOW);" + "\n"
	loopFor += "\t\t\t for(int j = 0; j < reds[i]; j++){" + "\n"
	loopFor += "\t\t\t\t digitalWrite(LEDPin[j], HIGH);" + "\n"
	loopFor += "\t\t\t } \n"
	loopFor += "\t\t } \n"
	loopFor += "\t\t else{ \n"
	loopFor += "\t\t\t digitalWrite(PlanePin[3], LOW);" + "\n"
	loopFor += "\t\t\t for(int j = 0; j < greens[i]; j++){" + "\n"
	loopFor += "\t\t\t\t digitalWrite(LEDPin[j], HIGH); \n"
	loopFor += "\t\t\t } \n"
	loopFor += "\t\t } \n"
	loopFor += "\t\t delay(500); \n"
 	loopFor += "\t\t if(greens[i] < reds[i]){" + "\n"
        loopFor += "\t\t\t digitalWrite(PlanePin[0], HIGH);" + "\n"
        loopFor += "\t\t\t for(int j = 0; j < reds[i]; j++){" + "\n"
        loopFor += "\t\t\t\t digitalWrite(LEDPin[j], LOW);" + "\n"
        loopFor += "\t\t\t } \n"
        loopFor += "\t\t } \n"
        loopFor += "\t\t else{ \n"
        loopFor += "\t\t\t digitalWrite(PlanePin[3], HIGH);" + "\n"
        loopFor += "\t\t\t for(int j = 0; j < greens[i]; j++){" + "\n"
        loopFor += "\t\t\t\t digitalWrite(LEDPin[j], LOW); \n"
        loopFor += "\t\t\t } \n"
        loopFor += "\t\t } \n"
	loopFor += "\t } \n"
	loopFor += "} \n\n\n"

	displayTotal += "void displayTotal(){ \n"
	displayTotal += "\t planesOff(); \n"
	displayTotal += "\t digitalWrite(PlanePin[1], HIGH); \n\t\t digitalWrite(PlanePin[2], HIGH); \n"
	displayTotal += "\t if(sizeof(blue) >= 0){ \n"
	displayTotal += "\t\t digitalWrite(PlanePin[2], LOW); \n"
	displayTotal += "\t\t for(int i = 0; i < blue[0]; i++){ \n"
	displayTotal += "\t\t\t digitalWrite(LEDPin[i], HIGH); \n"
	displayTotal += "\t\t } \n"
	displayTotal += "\t } \n"
	displayTotal += "\t if(sizeof(yellow) >= 0){ \n"
        displayTotal += "\t\t digitalWrite(PlanePin[1], LOW); \n"
        displayTotal += "\t\t for(int i = 0; i < yellow[0]; i++){ \n"
        displayTotal += "\t\t\t digitalWrite(LEDPin[i], HIGH); \n"
        displayTotal += "\t\t } \n"
        displayTotal += "\t } \n"
	displayTotal += "\t delay(15000); \n"
	displayTotal += "\t if(sizeof(blue) >= 0){ \n"
        displayTotal += "\t\t digitalWrite(PlanePin[2], HIGH); \n"
        displayTotal += "\t\t for(int i = 0; i < blue[0]; i++){ \n"
        displayTotal += "\t\t\t digitalWrite(LEDPin[i], LOW); \n"
        displayTotal += "\t\t } \n"
        displayTotal += "\t } \n"
	displayTotal += "\t if(sizeof(yellow) >= 0){ \n"
        displayTotal += "\t\t digitalWrite(PlanePin[1], HIGH); \n"
        displayTotal += "\t\t for(int i = 0; i < yellow[0]; i++){ \n"
        displayTotal += "\t\t\t digitalWrite(LEDPin[i], LOW); \n"
        displayTotal += "\t\t } \n"
        displayTotal += "\t } \n"
 	displayTotal += "} \n\n\n"

	planesOff += "void planesOff(){ \n"
	planesOff += "\t for(int i = 0; i < PlanePinCount; i++){ \n"
	planesOff += "\t\t digitalWrite(PlanePin[i], HIGH); \n"
	planesOff += "\t } \n"
	planesOff += "} \n"
	
	lightFile.write(loopFor)
	lightFile.write(displayTotal)
	lightFile.write(planesOff)	

	lightFile.close()
main()
