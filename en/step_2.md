<h2 class="c-project-heading--task">STEP 1</h2>
--- task ---
Enigma is a cipher machine that was used by the German military during World War II for secret communications. The cipher was famously broken during the war at Bletchley Park, the forerunner of GCHQ.
--- /task ---

<h2 class="c-project-heading--explain">SUB-HEADING</h2>
Look at the file enigma.py. 

The code uses a built-in library enigma.machine to do most of the work. 
Three key settings for the machine must be changed at the start of each day. 
Change them to match those shown in the code snippet below. 


<div class="c-project-code">
--- code ---
---
language:python
filename:enigma.py
line_numbers:true
line_number_start:
line_highlights:
---
ROTORS = 'IV I V'

RINGS = '20 5 10'

PLUGBOARD = 'AV BS CG DL FU HZ IN KM OW RX'
--- /code ---
</div>

<div class="c-project-callout c-project-callout--tip">
- make sure you leave spaces between the numbers.
</div>

<div class="c-project-callout c-project-callout--debug">
- how you can mess this up is beyond me
- just follow the instructions
</div>