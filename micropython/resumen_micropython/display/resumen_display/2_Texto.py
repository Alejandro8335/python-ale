import vga1_16x16 as font
import machine
import st7789py as st7789

st7789_res = 5
st7789_dc  = 4
pin_st7789_res = machine.Pin(st7789_res, machine.Pin.OUT)
pin_st7789_dc = machine.Pin(st7789_dc, machine.Pin.OUT)

disp_width = 240
disp_height = 240

spi = machine.SPI(
    2,
    baudrate=20_000_000,# Es la frecuencia del reloj SPI (SCK)   
    polarity=1,
    phase=1,
    sck=machine.Pin(18),
    mosi=machine.Pin(23),
    miso=None
)
display = st7789.ST7789(spi, disp_width, disp_width,
                          reset=pin_st7789_res,
                          dc=pin_st7789_dc,
                          rotation=1)

display.fill(st7789.RED)
display.text(
    font,
    "Hola ESP32",
    20,
    100,
    st7789.WHITE
)
