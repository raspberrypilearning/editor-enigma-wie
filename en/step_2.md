<h2 class="c-project-heading--task">STEP 1</h2>
--- task ---
**Enigma** is a cipher machine that was used by the German military during World War II for secret communications. The cipher was famously broken during the war at Bletchley Park, the forerunner of GCHQ.
--- /task ---
<h2 class="c-project-heading--explain">SUB-HEADING</h2>
Click the file `enigma.py` to look at the code. 

The code uses a built-in library `enigma.machine` to do most of the work. 
Three key settings for the machine must be changed at the start of each day. Currently it is set as follows: 

`ROTORS = 'IV I V'`

`RINGS = '20 5 10'`

`PLUGBOARD = 'AV BS CG DL FU HZ IN KM OW RX'`
<div class="c-project-code">
--- code ---
---
language:python
filename:main.py
line_numbers:true
line_number_start:
line_highlights: 4-7
---
print('hello Di')
answer = input('HOW ARE YOU?')

</div>

<div class="c-project-callout c-project-callout--tip">
- make sure you type answer = input()
</div>

<div class="c-project-callout c-project-callout--debug">
- how you can mess this up is beyond me
- just follow the instructions
</div>