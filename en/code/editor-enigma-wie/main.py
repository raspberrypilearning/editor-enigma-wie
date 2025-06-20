from enigma.machine import EnigmaMachine

# Sheet settings
ROTORS = "IV I V"
RINGS = "20 5 10"
PLUGBOARD = "SX KU QP VN JG TC LA WM OB ZF" 

def use_enigma_machine(msg, rotor_start):
  # Set up the Enigma machine 
  machine = EnigmaMachine.from_key_sheet(rotors=ROTORS, reflector="B", ring_settings=RINGS, plugboard_settings=PLUGBOARD)
  # Set the initial position of the rotors
  machine.set_display(rotor_start)
  # Encrypt or decrypt the message
  transformed_msg = machine.process_text(msg)
  return(transformed_msg)

def main():
  text_in = "Ada Lovelace would be proud of your code"
  rotor_start = "JOY"
  text_out = use_enigma_machine(text_in, rotor_start)
  print(text_out)

main()