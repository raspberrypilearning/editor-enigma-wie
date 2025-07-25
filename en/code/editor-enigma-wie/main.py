from enigma.machine import EnigmaMachine

# Sheet settings
ROTORS = "V I II"
RINGS = "12 21 7"
PLUGBOARD = "AV BS CG DL FU HZ IN KM OW RX"

def use_enigma_machine(msg, rotor_start):
  # Set up the Enigma machine 
  machine = EnigmaMachine.from_key_sheet(rotors=ROTORS, reflector="B", ring_settings=RINGS, plugboard_settings=PLUGBOARD)
  # Set the initial position of the rotors
  machine.set_display(rotor_start)
  # Encrypt or decrypt the message
  transformed_msg = machine.process_text(msg)
  return(transformed_msg)

def main():
  text_in = "I love coding"
  rotor_start = "abc"
  text_out = use_enigma_machine(text_in, rotor_start)
  print(text_out)

main()