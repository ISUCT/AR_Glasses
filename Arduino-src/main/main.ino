#include <SPI.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>


#define SCREEN_WIDTH 128 // OLED display width, in pixels
#define SCREEN_HEIGHT 64 // OLED display height, in pixels

#define OLED_RESET     4 // Reset pin # (or -1 if sharing Arduino reset pin)
#define SCREEN_ADDRESS 0x3C ///< See datasheet for Address; 0x3D for 128x64, 0x3C for 128x32
Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);
String currentString = "";
String name = "";
String surname = "";

void setup() {
  Serial.begin(9600);
  display.setRotation(2);
  display.setTextSize(1);
  display.setTextColor(SSD1306_WHITE); // Draw white text
  display.cp437(true);         // Use full 256 char 'Code Page 437' font


  if (!display.begin(SSD1306_SWITCHCAPVCC, SCREEN_ADDRESS)) {
    Serial.println(F("SSD1306 allocation failed"));
    for (;;); // Don't proceed, loop forever
  }
}

void GetSerialData()
{
  if (Serial.available() != 0)
  {
    String data = Serial.readString();
    if (data == "null")
    {
      currentString = " ";
    }
    else
    {
      currentString = data;
    }
  }
}
void SplitName()
{
  int deliIndex = currentString.indexOf(' ');
  name = currentString.substring(0, deliIndex);
  surname = currentString.substring(deliIndex + 1);
}

void DrawText(byte x, byte y, String text, bool haveClear)
{
  if (haveClear)
  {
    display.clearDisplay();
  }
  display.setCursor(x, y);
  display.println(name);
  display.println(surname);
  display.display();
}

void loop()
{
  GetSerialData();
  SplitName();
  DrawText(0, 0, currentString, true);

}
