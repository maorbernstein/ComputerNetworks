#!/usr/bin/python
# Example using a character LCD connected to a Raspberry Pi or BeagleBone Black.
import math
import time

import Adafruit_CharLCD as LCD



def LCD_Write(string, blink_cursor=False):
	# Raspberry Pi pin configuration:
	lcd_rs        = 27  # Note this might need to be changed to 21 for older revision Pi's.
	lcd_en        = 22
	lcd_d4        = 25
	lcd_d5        = 24
	lcd_d6        = 23
	lcd_d7        = 18
	lcd_backlight = 4


	# Define LCD column and row size for 16x2 LCD.
	lcd_columns = 16
	lcd_rows    = 2

	# Initialize the LCD using the pins above.
	lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows, lcd_backlight)
	#Clear the LCD
	lcd.clear()
	lcd.show_cursor(False)
	lcd.blink(False)
	#Write the message
	lcd.message(string)
	if blink_cursor:
		lcd.blink(True)

	time.sleep(10)
	lcd.clear()

if __name__ == "__main__":
	LCD_Write("Pants Are Cool!", True)



