# import time

UVEL32_RESOLUTION = 0.000000059604644775390625
UACC32_RESOLUTION = 0.00000095367431640625

def split_24bit_to_components(value):
    # Convert float value to scaled integer using velocity resolution
    scaled_value = int(value / UVEL32_RESOLUTION)

    scaled_value = scaled_value & 0xFFFFFF # 24 bits 
    
    # Extract 8-bit high part (bits 16-23)
    eight_bit = (scaled_value >> 16) & 0xFF
    # Extract 16-bit low part (bits 0-15)
    sixteen_bit = scaled_value & 0xFFFF
    
    return sixteen_bit, eight_bit

def split_20bit_to_components(value):
    # Convert float value to scaled integer using acceleration resolution
    scaled_value = int(value / UACC32_RESOLUTION)
    
    scaled_value = scaled_value & 0xFFFFF # 20 bits 

    # Extract 4-bit high part (bits 16-19)
    four_bit = (scaled_value >> 16) & 0x0F
    # Extract 16-bit low part (bits 0-15)
    sixteen_bit = scaled_value & 0xFFFF
    
    return sixteen_bit, four_bit

def combine_to_24bit(sixteen_bit, eight_bit):
    # Ensure inputs are within their bit limits
    sixteen_bit = sixteen_bit & 0xFFFF
    eight_bit = eight_bit & 0xFF      
    
    # Shift the 8-bit number 16 positions left and OR it with the 16-bit number
    result = (eight_bit << 16) | sixteen_bit
    
    return result

def combine_to_20bit(sixteen_bit, four_bit):
    # Ensure inputs are within their bit limits
    sixteen_bit = sixteen_bit & 0xFFFF
    four_bit = four_bit & 0x0F 
    
    # Shift the 4-bit number 16 positions left and OR it with the 16-bit number
    result = (four_bit << 16) | sixteen_bit
    
    return result
