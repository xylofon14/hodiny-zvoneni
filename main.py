import utime                          
import machine
from machine import I2C, Pin, PWM
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd           #Importují se potřebné knihovny a moduly.
 
I2C_ADDR = 0x27
I2C_NUM_ROWS = 4
I2C_NUM_COLS = 20                         #Nastavují se parametry pro LCD displej a I2C komunikaci.
 
i2c = I2C(0, sda=machine.Pin(0), scl=machine.Pin(1), freq=400000)
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)                   #Inicializuje se I2C komunikace a LCD displej.
 
buzzer = PWM(Pin(16))   #Určení GPIO pinu pro buzzer.
buzzer.freq(500)        #Nastavení frekvence buzzeru. (od 31 Hz do 65535 Hz)
 
alarm_times = [
    {"hour": 7, "minute": 45, "second": 0},
    {"hour": 8, "minute": 30, "second": 0},
    {"hour": 8, "minute": 35, "second": 0},
    {"hour": 9, "minute": 20, "second": 0},
    {"hour": 9, "minute": 25, "second": 0},
    {"hour": 10, "minute": 10, "second": 0},
    {"hour": 10, "minute": 30, "second": 0},
    {"hour": 11, "minute": 15, "second": 0},
    {"hour": 11, "minute": 25, "second": 0},
    {"hour": 12, "minute": 10, "second": 0},
    {"hour": 12, "minute": 20, "second": 0},
    {"hour": 13, "minute": 5, "second": 0},
    {"hour": 13, "minute": 15, "second": 0},
    {"hour": 14, "minute": 0, "second": 0},
    {"hour": 14, "minute": 10, "second": 0},
    {"hour": 14, "minute": 55, "second": 0},
    {"hour": 15, "minute": 0, "second": 0},
    {"hour": 15, "minute": 45, "second": 0}]     #Definují se časy alarmu.
 
global alarm
alarm = False   #Vytvoření globální proměnné "alarm".
 
def alarm_callback(timer):
    global alarm
    current_time = utime.localtime()
    alarm = any(
        current_time[3] == time_point["hour"] and
        current_time[4] == time_point["minute"] and
        current_time[5] == time_point["second"]
        for time_point in alarm_times)              #Je definována funkce "alarm_callback". Kontroluje, zda je časový bod nastavený v proměnné "alarm_times" aktuálním časem, pokud ano - "alarm" = True.
 
alarm_timer = machine.Timer()
alarm_timer.init(period=60, mode=machine.Timer.PERIODIC, callback=alarm_callback)  #Je vytvořen timer, který volá "alarm_callback" každých 60 sekund.
 
while True:
    if alarm:
        for i in range(5):
            buzzer.duty_u16(1000)
            utime.sleep(0.5)
            buzzer.duty_u16(0)
            utime.sleep(0.5)
            alarm = False     #Hlavní smyčka programu kontroluje, zda má být alarm spuštěn. Pokud ano, zvuk se opakuje 5krát s intervaly 0.5 sekundy, pak se "alarm" nastaví zpět na False.
 
    utime.sleep(1) #Aktualizace displeje každou sekundu.
    lcd.clear()   #Vymazaní displeje při prvním zapnutí.
    day_of_week = utime.localtime()[6]    #Vytvoření proměnné pro dny v týdnu.
    days = ["Pondeli", "Utery", "Streda", "Ctvrtek", "Patek", "Sobota", "Nedele"]      #Seznam dnů v týdnu, ze kterého se pak bude vybírat pro zobrazení.
    time = utime.localtime() #Při spuštění se vezme lokální čas z internetu, pak už se používá built-in RTC modul.
    lcd.move_to(0,0)
    lcd.putstr("{}".format(days[day_of_week]))
    lcd.move_to(8,0)
    lcd.putstr("{HH:>02d}:{MM:>02d}:{SS:>02d}".format(HH=time[3], MM=time[4],SS=time[5]))
    lcd.move_to(0,1)
    lcd.putstr("{DY:>02d}".format(DY=time[7]))
    lcd.move_to(6,1)
    lcd.putstr("{day:>02d}/{month:>02d}/{year:>04d}".format( 
        year=time[0], month=time[1], day=time[2]))           #Výpis hodnot na displej. (HH = hodiny, MM = minuty, SS = sekundy, DY = den v roce)
 
