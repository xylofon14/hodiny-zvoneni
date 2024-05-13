<h1>Hodiny</h1>
<h2>s 16x2 LCD I2C displej a Piezo Buzzer - PS1240</h2>
Jedná se o ukázku praktického využití mikrokontroleru v podobě hodin s alarmem.
<h3>Schéma zapojení</h3>
<img src="https://github.com/xylofon14/hodiny-zvoneni/blob/main/schema%20zapojeni.png" alt="zapojení">
<h3>Programy</h3>
<a href="https://github.com/xylofon14/hodiny-zvoneni/blob/main/lcd_api.py" target="_blank" rel="noopener norefferer">lcd_api.py</a> +
<a href="https://github.com/xylofon14/hodiny-zvoneni/blob/main/pico_i2c_lcd.py" target="_blank" rel="noopener norefferer">pico_i2c_lcd.py</a> - knihovny pro práci s LCD I2C displejem.

<a href="https://github.com/xylofon14/hodiny-zvoneni/blob/main/main.py" target="_blank" rel="noopener norefferer">main.py</a> - hlavní kód

<h3>Použité komponenty</h3>
<ul>
<li><a href="https://rpishop.cz/bzucaky/813-piezo-buzzer-ps1240.html" target="_blank" rel="noopener norefferer">Piezo Buzzer PS1240</a>
<li><a href="https://rpishop.cz/radkove-displeje/1428-16x2-lcd-i2c-displej-modry.html" target="_blank" rel="noopener norefferer">16x2 LCD I2C displej</a>
<li>Nepájivé pole
<li>Propojovací kabely Male/Female
<li>Programovací a napájecí kabel - programovací kabel USB-A na microUSB
</ul>

<h3>Foto</h3>
<img src="https://github.com/xylofon14/hodiny-zvoneni/blob/main/image0.jpg" alt="foto">

<h3>Návrhy na vylepšení</h3>
<ul>
  <li>Vytvořit pro hodiny krabičku/obal.
  <li>Předělat na bateriové napájení.
  <li>Přidat specifikou melodii pro buzzer.
</ul>

<h3>Literatura</h3>
<li><a href="https://github.com/T-622/RPI-PICO-I2C-LCD" target="_blank" rel="noopener norefferer">Knihovny</a>
<li><a href="https://www.youtube.com/watch?v=bXLgxEcT1QU&ab_channel=NerdCave" target="_blank" rel="noopener norefferer">Pomocné video k prvnímu zapojení displeje</a>
<li><a href="https://www.waveshare.com/wiki/RP2040-Zero" target="_blank" rel="noopener norefferer">RP2040</a>
